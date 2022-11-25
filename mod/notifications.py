#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Напоминания себе.
# Полезные справки:
# Документация по dbus: https://dbus.freedesktop.org/doc/dbus-python/index.html
# Пример с qt: https://wiki.qt.io/Qt_for_Python_DBusIntegration
#
import dbus
import dbus.mainloop.glib
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QObject
from mod.shell import Shell

class TrayNotifications(QObject):
    distUpdate = pyqtSignal()
    """Собщения уведомлений на основе dbus"""
    def __init__(self):
        super().__init__()
        self.bash = Shell()
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        session_bus = dbus.SessionBus()
        target_notifi = 'org.freedesktop.Notifications'
        path_notifi = '/org/freedesktop/Notifications'
        notifi = session_bus.get_object(target_notifi, path_notifi)
        self.notifi_iface = dbus.Interface(notifi, 'org.freedesktop.Notifications')

        # Сигналы
        self.notifi_iface.connect_to_signal('ActionInvoked', self.signal_button_update)

        self.name_app = 'kernel_indicator.py'
        self.icon = '/opt/kernel-manager/icons/kernel-manager.png'

    def signal_button_update(self, num, signal):
        """Сигнал от кнопки обновления"""
        Thread(target=self.update_message).start()
        self.distUpdate.emit()

    def update_completed(self):
        """Сообщение завершения обновления"""
        summary = _('Update completed')
        body = _('Distribution update completed. For correct operation of all updated libraries, it is recommended to restart the computer.')

        self.notifi_iface.Notify(self.name_app, 0, self.icon, summary, body, [], {'urgency': 1}, 20000)
        self.message_sound()

    def update_message(self):
        """Сообщение о начале обновления"""
        summary = _('Update started')
        body = _('Software update in progress. This may take some time. When the update is complete, you will receive a notification and the taskbar icon will stop animating.')

        self.notifi_iface.Notify(self.name_app, 0, self.icon, summary, body, [], {'urgency': 1}, 20000)
        self.message_sound()

    def disable_button(self):
        """Сообщение отключения кнопки обновления"""
        summary = _('Button disabled')
        body = _('The Update button for new packages will no longer appear in update messages.')

        self.notifi_iface.Notify(self.name_app, 0, self.icon, summary, body, [], {'urgency': 1}, 20000)
        self.message_sound()

    def enable_button(self):
        """Сообщение включения кнопки обновления"""
        summary = _('Button enabled')
        body = _('Messages will now show a button to update rpm packages.')

        self.notifi_iface.Notify(self.name_app, 0, self.icon, summary, body, [], {'urgency': 1}, 20000)
        self.message_sound()

    def autostart_message(self, dir_autostart):
        """Показать сообщение при включении автостарта"""
        summary = _('Autostart directory:')
        body = dir_autostart

        self.notifi_iface.Notify(self.name_app, 0, self.icon, summary, body, [], {'urgency': 1}, 20000)
        self.message_sound()

    def kernel_message(self, config):
        """Отправить сообщение об налиции нового ядра системы"""
        summary = _('Kernel update')
        body = _('A new version of the kernel is available: ') + config['version']

        self.notifi_iface.Notify(self.name_app, 0, self.icon, summary, body, [], {'urgency': 1}, 20000)
        self.message_sound()

    def software_message(self, config):
        """Отправить уведомление об обновлении пакетов"""
        summary = _('Updating packages')
        button = _('Update RPM packages')

        if self.config['upbutton']:
            action = ['True', button]
            if self.bash.run('pgrep -o "apt-get dist-upgrade"'):
                action = []
        else: action = []

        if config['pkg'][0] >= 300: urg = 2
        else: urg = 1

        update = _('Packages to update: ') + config['pkg'][0]
        install = _('Newly installed: ') + config['pkg'][1]
        remove = _('For removing: ') + config['pkg'][2]
        not_update = _('Will not be updated: ') + config['pkg'][3]

        body = f'{update}\n{install}\n{remove}\n{not_update}'

        self.notifi_iface.Notify(self.name_app, 0, self.icon, summary, body, action, {'urgency': urg}, 20000)
        self.message_sound()

    def message_sound(self):
        """Звук обычных сообщений через ALSA"""
        self.bash.run('aplay -q /opt/kernel-manager/sound/message.wav')
