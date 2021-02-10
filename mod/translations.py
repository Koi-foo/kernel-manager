#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Скрипт для разметки перевода.

import os
import sys


class MarkupLine():
    """Класс для разметки перевода"""
    def __init__(self):
        
        files = [
            "../form/main_win.py", 
            "../form/process_win.py"]
        
        self.search_strings(files)
        
    
    def search_strings(self, files):
        """Поиск и замена строк"""
                
        for path in files:
            
            if 'main' in path:
                    window = 'MainWindow'
            elif 'process' in path:
                    window = 'InfoProcessWin'
            
            with open(path, 'rt') as file_obj:
                contents = file_obj.read()
                
                contents = contents.replace(
                    f'_translate("{window}", "', \
                    f'_translate("{window}", _("').replace('"))', \
                    '")))').replace('resources_rc', 'resources')
                
            with open(path, 'wt') as file_obj:
                file_obj.write(contents)

start_script = MarkupLine()
