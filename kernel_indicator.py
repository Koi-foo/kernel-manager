#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Python
import os
import re
import sys
import gettext
import json
from datetime import date
from datetime import datetime
from threading import Thread
from mod.shell import Shell
from mod.create_desktop import autostart_desktop
from mod.indicator_settings import IndicatorSettings
from mod.notifications import TrayNotifications
import mod.default
from pathlib import Path
from time import sleep
# PyQt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QMovie, QPixmap
from PyQt5.QtCore import pyqtSignal
import resources
# рабочий путь
os.chdir(os.path.dirname(sys.argv[0]))
# Языковая локализация
gettext.install('kernel_manager', 'locale')

class SystemTrayWindows(QtWidgets.QMainWindow):
    endUpdate = pyqtSignal()
    """Окно настроек уведомлений на панели задач"""
    def __init__(self):
        super().__init__()
        self.path_config = mod.default.config_file()
        self.config = mod.default.load(self.path_config)
        self.bash = Shell()
        self.indicator = IndicatorSettings(self.config)
        self.notifi = TrayNotifications()

        # Значок трея
        self.icon = QIcon(":/picture/icons/kernel-manager.png")
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(self.icon)
        self.icon_movie = QMovie(':/picture/icons/kernel-manager.gif')
        self.trayIcon.setToolTip(_("Kernel update indicator"))

        # Сигналы
        self.trayIcon.activated.connect(self.open_kernel_manager)
        self.indicator.autoLoad.connect(self.autostart_check_signal)
        self.indicator.kernelMessage.connect(self.kernel_check_signal)
        self.indicator.softwareMessage.connect(self.soft_check_signal)
        self.indicator.notifiButton.connect(self.notifi_check_botton_signal)
        self.icon_movie.frameChanged.connect(self.icon_animation)
        self.notifi.distUpdate.connect(self.update_signal)
        self.endUpdate.connect(self.end_update)

        # Действия для меню
        iconExit = ":/picture/icons/application-exit.svg"
        quit_action = QAction(QIcon(iconExit), _("Close indicator"), self)
        quit_action.triggered.connect(self.close_app)

        iconMessages = ':/picture/icons/dialog-messages.svg'
        show_old_message = QAction(QIcon(iconMessages), _('Repeat message'), self)
        show_old_message.triggered.connect(self.show_message_signal)

        iconSetting = ':/picture/icons/configure.svg'
        setting_indicator = QAction(QIcon(iconSetting), _('Settings'), self)
        setting_indicator.triggered.connect(self.show_setting)

        # Меню
        tray_menu = QMenu()
        tray_menu.addAction(show_old_message)
        tray_menu.addAction(setting_indicator)
        tray_menu.addAction(quit_action)

        self.trayIcon.setContextMenu(tray_menu)
        self.trayIcon.setVisible(True)

        self.show_message_signal()

    def icon_animation(self):
        """Анимация значка трея"""
        self.icon_movie.setSpeed(250)
        self.trayIcon.setIcon(QIcon(QPixmap(self.icon_movie.currentPixmap())))

    def update_signal(self):
        """Обработка сигнала обновления"""
        self.icon_movie.start()
        Thread(target=self.update_distribution).start()

    def update_distribution(self):
        """Обновитьдистрибутив"""
        self.bash.run(f'pkexec kernel_service.py -p "{self.path_config}" -u')
        self.endUpdate.emit()

    def end_update(self):
        """Завершение обновления"""
        self.trayIcon.setIcon(self.icon)
        self.icon_movie.stop()
        self.config['pkg'] = False
        self.notifi.update_completed()

    def show_setting(self):
        """Открыть окно настроек индикатора"""
        self.indicator.show()

    def autostart_check_signal(self):
        """Сигнал от checkBoxAutostart"""
        Thread(target=self.set_autoload).start()

    def notifi_check_botton_signal(self):
        """Сигнал от checkBoxMessageButton"""
        Thread(target=self.notifi_check_botton).start()

    def notifi_check_botton(self):
        """Послать сообщение об установке кнопки в уведомления"""
        status = self.config['upbutton']

        if status:
            self.notifi.enable_button()
        else:
            self.notifi.disable_button()

    def soft_check_signal(self):
        """Сигнал от checkBoxSoftware"""
        Thread(target=self.check_soft).start()

    def kernel_check_signal(self):
        """Сигнал от checkBoxKernel"""
        Thread(target=self.check_kernel).start()

    def set_autoload(self):
        """вкл\выкл автозагрузка"""
        dir_home = Path.home()
        dir_autostart = f'{dir_home}/.config/autostart'

        if Path(dir_autostart).exists() is False:
            Path(dir_autostart).mkdir(parents=False)

        try:
            if self.config['start']:
                autostart_desktop(dir_autostart)
                self.notifi.autostart_message(dir_autostart)
            else:
                os.remove(f'{dir_autostart}/autostart-kernel-indicator.desktop')
        except(FileNotFoundError, FileExistsError):
            pass

    def close_app(self):
        """Закрыть и сохранить данные"""
        self.save_settings()
        sys.exit()


    def save_settings(self):
        """Сохранение настроек пользователя"""
        mod.default.save(self.path_config, self.config)

    def show_message_signal(self):
        """Сигнал от меню"""
        Thread(target=self.show_message).start()

    def show_message(self):
        """Общее сообщение"""
        self.check_kernel()
        self.check_soft()

    def check_kernel(self):
        """Обработка сигнала с триггера kern"""
        if self.config['kernel']:
            if self.config['version'] != False:
                self.notifi.kernel_message(self.config)

    def check_soft(self):
        """Обработка сигнала с триггера kern"""
        if self.config['software']:
            if self.config['pkg'] != False:
                self.notifi.software_message(self.config)

    def open_kernel_manager(self):
        """Открыть kernel manager"""
        activ_manager = self.bash.run("pgrep -o kernel-manager")

        if activ_manager: pass
        else: self.bash.popen("kernel-manager")

def wait_service():
    """Ждём окончания работы сервиса"""
    try:
        if sys.argv[1] == '--show':
            pass
    except:
        path_config = mod.default.config_file()
        config = mod.default.load(path_config)
        sleep(config['time'])

        current = date.today()
        update_date = datetime.strptime(config['update_date'], '%Y-%m-%d').date()
        difference = (current - update_date).days

        if difference >= config['days']:
            Shell().run(f'pkexec kernel_service.py -p "{path_config}"')

            config = mod.default.load(path_config)
            if not config['version'] and not config['pkg']: exit()
            elif not config['software'] and not config['kernel']: exit()
            elif not config['software'] and not config['version']: exit()
            elif not config['kernel'] and not config['pkg']: exit()
        else:
            sys.exit()

if __name__ == '__main__':
    mod.default.config_check()
    wait_service()
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    sys_tray = SystemTrayWindows()
    sys.exit(app.exec_())
