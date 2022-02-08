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
from subprocess import run, PIPE, CalledProcessError


def shrun(bash_comand):
    """Запуск run вывод stdout"""
    return run(bash_comand,
               shell=True,
               stdout=PIPE,
               encoding='utf-8'
               ).stdout


def shcheck(bash_comand):
    """Запуск run вывод stdout с проверкой check=True
    возбуждение исключния CalledProcessError"""
    return run(bash_comand,
               shell=True,
               check=True,
               stdout=PIPE,
               encoding='utf-8'
               ).stdout.rstrip()


def shcom(bash_comand):
    """Запуск run без вывода"""
    return run(bash_comand, shell=True).stdout
