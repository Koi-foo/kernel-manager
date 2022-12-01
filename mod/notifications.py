#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Убрана реализация уведомлений напрямую через dbus, так как поведение функций
# в разных окружениях отличается, кроме того, многие окружения используют свои
# собственные демоны уведомлений, которые по-своему поддерживают
# функциональность dbus, что часто вызывает ошибки. Демоны, такие как
# mate-notifications, обычно имеют возможность отключиться от шины, вызывая
# ее повторный вызов и изменение уникального имени. В настоящее время разумной
# реализацией для всех популярных сред является libnotify.
#
import dbus
import dbus.mainloop.glib
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QSystemTrayIcon
from mod.shell import Shell

class TrayNotifications(QObject):
    distUpdate = pyqtSignal()
    """Собщения уведомлений на основе dbus"""
    def __init__(self):
        super().__init__()
        self.bash = Shell()
        send = 'notify-send'
        name_app = '-a kernel_indicator.py'
        icon = '-i /opt/kernel-manager/icons/kernel-manager.png'
        self.notify = f'{send} {name_app} {icon}'

    def signal_button_update(self):
        """Сигнал от кнопки обновления"""
        if not self.update_test():
            Thread(target=self.update_message).start()
            self.distUpdate.emit()

    def update_completed(self):
        """Сообщение завершения обновления"""
        summary = _('Update completed')
        body = _('Distribution update completed. For correct operation of all updated libraries, it is recommended to restart the computer.')

        self.bash.run(f'{self.notify} -u "normal" -t 30000 "{summary}" "{body}"')
        self.message_sound()

    def update_message(self):
        """Сообщение о начале обновления"""
        summary = _('Update started')
        body = _('Software update in progress. This may take some time. When the update is complete, you will receive a notification and the taskbar icon will stop animating.')

        self.bash.run(f'{self.notify} -u "normal" -t 30000 "{summary}" "{body}"')
        self.message_sound()

    def disable_button(self):
        """Сообщение отключения кнопки обновления"""
        summary = _('Button disabled')
        body = _('The Update button for new packages will no longer appear in update messages.')

        self.bash.run(f'{self.notify} -u "normal" -t 10000 "{summary}" "{body}"')
        self.message_sound()

    def enable_button(self):
        """Сообщение включения кнопки обновления"""
        summary = _('Button enabled')
        body = _('Messages will now show a button to update rpm packages.')

        self.bash.run(f'{self.notify} -u "normal" -t 10000 "{summary}" "{body}"')
        self.message_sound()

    def autostart_message(self, dir_autostart):
        """Показать сообщение при включении автостарта"""
        summary = _('Autostart directory:')
        body = dir_autostart

        self.bash.run(f'{self.notify} -u "normal" -t 15000 "{summary}" "{body}"')
        self.message_sound()

    def kernel_message(self, config):
        """Отправить сообщение об налиции нового ядра системы"""
        summary = _('Kernel update')
        body = _('A new version of the kernel is available: ') + config['version']

        self.bash.run(f'{self.notify} -u "normal" -r 5 -t 20000 "{summary}" "{body}"')
        self.message_sound()

    def software_message(self, config):
        """Отправить уведомление об обновлении пакетов"""
        summary = _('Updating packages')
        button = _('Update RPM packages')
        action = self.activ_action(config, button)
        urg = self.urgency_lvl(config)

        update = _('Packages to update: ') + config['pkg'][0]
        install = _('Newly installed: ') + config['pkg'][1]
        remove = _('For removing: ') + config['pkg'][2]
        not_update = _('Will not be updated: ') + config['pkg'][3]

        body = f'{update}\n{install}\n{remove}\n{not_update}'

        self.bash.popen('aplay -q /opt/kernel-manager/sound/message.wav')
        message = self.bash.run(f'{self.notify} -u {urg} -r 6 {action} -t 20000 "{summary}" "{body}"')
        self.start_update(message)

    def start_update(self, message):
        """Запустить обновление от кнопки и ее статуса"""
        if 'update' in message:
            self.signal_button_update()

    def urgency_lvl(self, config, lvl=None):
        """Установка статуса обновления"""
        if int(config['pkg'][0]) >= 300: lvl = 'critical'
        else: lvl = 'normal'

        return lvl

    def activ_action(self, config, button, activ=None):
        """Активность кнопки в сообщении обновления"""
        if config['upbutton']:
            activ = f'-A update="{button}"'
            if self.update_test():
                activ = ''
        else: activ = ''

        return activ

    def update_test(self, status=None):
        """роверка запущено ли обновление"""
        pid = self.bash.run('pgrep -fo "apt-get dist-upgrade"')

        if pid: status = True

        return status

    def message_sound(self):
        """Звук обычных сообщений через ALSA"""
        self.bash.run('aplay -q /opt/kernel-manager/sound/message.wav')
