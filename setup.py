#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import argparse
import shutil
import os

parser = argparse.ArgumentParser(allow_abbrev=True, description='installation kernel-manager')
required = parser.add_argument_group('required arguments')
parser.add_argument('-v', '-version', action='version', version='v0.1 Project page https://github.com/Koi-foo/kernel-manager')
required.add_argument('--prefix', metavar='', type=str, nargs=1, required=True, help='example --prefix=/usr')
required.add_argument('--sysv', metavar='', type=str, nargs=1, required=True, help='example --sysv=/initdir_dir')
required.add_argument('--sysd', metavar='', type=str, nargs=1, required=True, help='example --systemd=/unit_dir')
required.add_argument('--polkit', metavar='', type=str, nargs=1, required=True, help='example --polkit=/path')
required.add_argument('--buildroot', metavar='', type=str, nargs=1, required=True, help='example --buildroot=/path')
required.add_argument('--bindir', metavar='', type=str, nargs=1, required=True, help='example --bindir=/path')
args = parser.parse_args()

modules = [
    '/mod/create_desktop.py',
    '/mod/load_config.py',
    '/mod/shell.py'
    ]

directories = [
    '/data',
    '/sound',
    '/form',
    '/icons',
    '/locale'
    ]

files = [
    '/kernel_manager.py',
    '/kernel-indicator',
    '/resources.py'
    ]

desktop = [
    '/kernel-indicator.desktop',
    '/kernel-manager.desktop'
    ]

executant = [
    '/kernel-service',
    '/kernel-manager'
    ]

build_dir = os.getcwd()
prefix = args.prefix[0]
buildroot = args.buildroot[0]

bin_dir = f'{buildroot}{args.bindir[0]}'
polkit_dir = f'{buildroot}{args.polkit[0]}'
sysv_dir = f'{buildroot}{args.sysv[0]}'
systemd_dir = f'{buildroot}{args.sysd[0]}'
share_dir = f'{buildroot}/usr/share/applications'
install_dir = f'{buildroot}{prefix}/kernel-manager'

# раскидать и не париться
os.makedirs(f'{install_dir}/mod')
for item in modules:
    shutil.copy(f'{build_dir}{item}', f'{install_dir}{item}')

os.makedirs(share_dir)
for item in desktop:
    shutil.copy(f'{build_dir}/desktop{item}', f'{share_dir}{item}')

for item in directories:
    shutil.copytree(f'{build_dir}{item}', f'{install_dir}{item}')

for item in files:
    shutil.copy(f'{build_dir}{item}', f'{install_dir}{item}')

os.makedirs(bin_dir)
for item in executant:
    shutil.copy(f'{build_dir}/bin{item}', f'{bin_dir}{item}')

os.makedirs(polkit_dir)
polkit_file = '/org.freedesktop.pkexec.kernel-manager.policy'
shutil.copy(f'{build_dir}/polkit{polkit_file}', f'{polkit_dir}{polkit_file}')

os.makedirs(systemd_dir)
shutil.copy(f'{build_dir}/service/kernel-service.service', f'{systemd_dir}/kernel-service.service')

os.makedirs(sysv_dir)
shutil.copy(f'{build_dir}/service/kernel-service', f'{sysv_dir}/kernel-service')

os.chmod(f'{install_dir}/data/config.json', 0o666)
