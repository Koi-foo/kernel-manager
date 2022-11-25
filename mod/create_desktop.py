#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
def text_desktop():
    """Содержание файла desktop"""
    text = """[Desktop Entry]
Categories=SystemClub;Settings;System;X-Kernel-Manager;
Keywords=Configuration;Utility;
Name=Kernel indicator
Comment=Kernel indicator for the kernel manager program
Type=Application
Terminal=false
StartupNotify=true
X-DBUS-StartupType=none
X-KDE-SubstituteUID=false
X-GNOME-Autostart-enabled=true
Icon=/opt/kernel-manager/icons/kernel-manager.png
Exec=/opt/kernel-manager/kernel_indicator.py"""
    return text

def autostart_desktop(path_dir):
    """Создать файл автозапуска desktop"""
    with open(f'{path_dir}/autostart-kernel-indicator.desktop', 'w') as f:
        f.write(text_desktop())
