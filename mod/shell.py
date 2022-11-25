#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Module for running commands in bash linux
# An obvious reminder to import the modules already imported here into the main
# file is not needed.
#
# Python
import os
import sys
from subprocess import run, PIPE, CalledProcessError, Popen

class Shell():
    """Готовые шаблоны запуска команд в оболочке sh"""
    def __init__(self):
        pass

    def run(self, command):
        """Запуск run вывод stdout"""
        return run(
            command,
            shell=True,
            stdout=PIPE,
            encoding='utf-8'
            ).stdout

    def popen_connect(self, command):
        """Запустить и соединиться"""
        return Popen(
            command,
            shell=True,
            stdout=PIPE,
            encoding='utf-8'
            ).stdout

    def popen(self,command):
        """Запустить и отсоединится"""
        return Popen(
            command,
            shell=True).stdout

    def check(self, command):
        """Запуск run вывод stdout с проверкой check=True
        возбуждение исключния CalledProcessError"""
        return run(
            command,
            shell=True,
            check=True,
            stdout=PIPE,
            encoding='utf-8'
            ).stdout.rstrip()

    def no_output(self, command):
        """Запуск run без вывода"""
        return run(
            command,
            shell=True
            ).stdout
