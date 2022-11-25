#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PyQt
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
# Form
from form.indicator_win import Ui_IndicatorWindow

class IndicatorSettings(QtWidgets.QMainWindow, Ui_IndicatorWindow):
    autoLoad = pyqtSignal()
    kernelMessage = pyqtSignal()
    softwareMessage = pyqtSignal()
    notifiButton = pyqtSignal()
    """Настройки для окна ондикатора"""
    def __init__(self, config):
        super().__init__()
        self.setupUi(self)
        self.config = config

        # Установка позиций
        self.checkBoxAutostart.setChecked(self.config['start'])
        self.checkBoxKernel.setChecked(self.config['kernel'])
        self.checkBoxSoftware.setChecked(self.config['software'])
        self.comboBoxTime.setCurrentText(str(config['time']))
        self.spinBoxDays.setValue(self.config['days'])
        self.checkBoxMessageButton.setChecked(self.config['upbutton'])

        #Сигналы
        self.checkBoxAutostart.stateChanged.connect(self.check_autostart)
        self.checkBoxKernel.stateChanged.connect(self.check_kernel)
        self.checkBoxSoftware.stateChanged.connect(self.check_software)
        self.comboBoxTime.currentTextChanged.connect(self.time_delay)
        self.spinBoxDays.valueChanged.connect(self.day_update)
        self.checkBoxMessageButton.stateChanged.connect(self.check_button)

    def check_button(self, status):
        """Изменить флажок в отображении кнопки в уведомлениях"""
        if status:
            self.config['upbutton'] = True
        else:
            self.config['upbutton'] = False

        self.notifiButton.emit()

    def check_software(self, status):
        """Исменение флажка обновления ПО"""
        if status:
            self.config['software'] = True
            self.softwareMessage.emit()
        else:
            self.config['software'] = False

    def check_kernel(self, status):
        """Изменение флажка проверки ядра системы"""
        if status:
            self.config['kernel'] = True
            self.kernelMessage.emit()
        else:
            self.config['kernel'] = False

    def day_update(self, day):
        """Период обновления в днях"""
        self.config['days'] = day

    def time_delay(self, delay):
        """Установка задержки старта"""
        self.config['time'] = int(delay)

    def check_autostart(self, status):
        """Изменние статуса флажка автостарта"""
        if status:
            self.config['start'] = True
        else:
            self.config['start'] = False

        self.autoLoad.emit()

