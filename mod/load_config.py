#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import json

pathConfig = '/opt/kernel-manager/data/config.json'

def loadConfig():
    """Загрузка файла конфигурации"""
    try:
        with open(pathConfig) as f:
            config = json.load(f)
            return config
    except:
        config = createDefaultConfig()
        return config

def createDefaultConfig():
    """Создать конфигурационный файл"""
    config = createConfigFile()
    saveFileConfig(config)
    return config

def saveFileConfig(config):
    """Сохранение файла конфигурации"""
    with open(pathConfig, 'w') as f:
        json.dump(config, f)

def createConfigFile():
    """Создать файл конфигурации"""
    configFile = {
        'time': 600,
        'kernel': False,
        'software': False,
        'days': 1,
        'start': False,
        'service': False}
    return configFile
