#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import json
import argparse
import sys
import requests
from requests.adapters import Retry, PoolManager
from platform import release
from re import findall, search
from os import path, chmod
from datetime import date
from subprocess import run, PIPE

parser = argparse.ArgumentParser(allow_abbrev=True, description='Service for kernel_indicator')
required = parser.add_argument_group('required arguments')
parser.add_argument('-v', '--version', action='version', version='v0.2 Project page https://github.com/Koi-foo/kernel-manager')
parser.add_argument('-u', '--update', action='store_true', help='Update distribution')
required.add_argument('-p', '--path', metavar='', type=str, nargs=1, required=True, help='File path QSettings kernel_indicator')
args = parser.parse_args()

def update_cache():
    """Обновление кэша"""
    try:
        current = date.today()
        permission = date.fromtimestamp(path.getmtime(LOCK))
        difference = (current - permission).days
    except PermissionError:
        sys.exit(f'no access to file {LOCK}')

    if difference >= CONFIG['days']:
        shell('apt-get update')
    else:
        sys.exit()

def update_packages():
    """Список пакетов для обновления"""
    packages = []
    text = 'not upgraded.'
    command = 'echo "-n" | LANG=en apt-get dist-upgrade'
    update = shell(command).splitlines()

    for item in update:
        if len(packages) == 1:
            break

        if text in item:
            packages.append(item)

    packages = findall(r'[0-9]+', packages[0])

    if not int(packages[0]) \
        and not int(packages[1]) \
        and not int(packages[2]) \
        and not int(packages[3]):
            CONFIG['pkg'] = False
    else:
        CONFIG['pkg'] = packages

def shell(command):
    """Запуск run вывод stdout"""
    return run(
        command,
        shell=True,
        stdout=PIPE,
        encoding='utf-8'
        ).stdout

def save_settings():
    """Сохранение новых настроек"""
    with open(config_path, 'w') as f:
        json.dump(CONFIG, f)
    chmod(config_path, 0o666)

def main():
    """Старт"""
    connection_test()
    update_cache()

    if CONFIG['kernel']:
        version_kernel()

    if CONFIG['software']:
        update_packages()

    save_settings()

def version_kernel():
    """Проверка версии ядра"""
    flavour = search(r'.*-(.+-.+)-', release()).group(1)
    current = release().split('-')[0]
    new = current.split('.')
    search_version = shell(f"apt-cache pkgnames kernel-image-{flavour}#")

    for line in search_version.splitlines():
        act = search(r':(.+)-alt' ,line).group(1).split(".")
        if int(act[0]) > int(new[0]): new[0] = act[0]
        if int(act[1]) > int(new[1]): new[1] = act[1]
        if int(act[2]) > int(new[2]): new[2] = act[2]
    new_version = ".".join(new)

    if current == new_version:
        CONFIG['version'] = False
    else:
        CONFIG['version'] = new_version

def connection_test():
    """Тест интернета"""
    retries = Retry(connect=3, backoff_factor=60)
    http = PoolManager(retries=retries)

    try:
        http.request("HEAD", 'https://duckduckgo.com')
    except:
        sys.exit('Your internet is dead :-D')

def update_distribution():
    """Обновить дистрибутив"""
    shell('apt-get dist-upgrade -y')
    CONFIG['pkg'] = False
    save_settings()
    sys.exit()

def load(path, obj=None):
    """Чтение из файла"""
    with open(path) as f:
        obj = json.load(f)
    return obj

if __name__ == '__main__':
    config_path = args.path[0]
    CONFIG = load(config_path)
    LOCK = '/var/lib/apt/lists/lock'

    if type(CONFIG) is not dict:
        sys.exit('Invalid file format')

    if args.update:
        update_distribution()

    main()

