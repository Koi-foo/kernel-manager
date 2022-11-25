#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import json
from pathlib import Path

def config_dir():
    """Путь к конфигу индикатора"""
    _dir = f'{Path.home()}/.config/AltLinux Club'
    return _dir

def config_file():
    """Путь к файлу конфигурации"""
    _file = f'{config_dir()}/kernel_indicator.json'
    return _file

config = {
    'time': 150,
    'kernel': False,
    'software': False,
    'days': 1,
    'start': False,
    'pkg': False,
    'version': False,
    'upbutton': True,
    'home': config_file()
        }

def save(path, value):
    """Сохранение файла"""
    with open(path, 'w') as f:
        json.dump(value, f)

def load(path, obj=None):
    """Чтение из файла"""
    with open(path) as f:
        obj = json.load(f)
    return obj

def config_check():
    """Проверка существования файла"""
    _config = config['home']
    _dir = config_dir()

    if not Path(_config).exists():
        Path(_dir).mkdir(parents=True)
        save(_config, config)
