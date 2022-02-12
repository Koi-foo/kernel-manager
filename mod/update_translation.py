#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Обновление файлов перевода.
#
from pathlib import Path
from subprocess import run, PIPE

def shell(com):
    """Выполнение команд оболочки sh"""
    return run(com,
               shell=True,
               stdout=PIPE,
               encoding='utf-8'
               ).stdout

dir_locale = Path('../locale').resolve()

translations_path = [
    'ru/LC_MESSAGES',
    'el/LC_MESSAGES',
    'hi/LC_MESSAGES',
    'zh/LC_MESSAGES',
    'zh_TW/LC_MESSAGES'
    ]

for p in translations_path:
    shell(f'msgmerge -U --backup=off {dir_locale}/{p}/kernel_manager.po {dir_locale}/kernel_manager.pot')
    shell(f'msgfmt {dir_locale}/{p}/kernel_manager.po -o {dir_locale}/{p}/kernel_manager.mo')


