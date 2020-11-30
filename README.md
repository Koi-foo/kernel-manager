#Specification

Name: kernel-manage
Version: 1.3
License: GPL3
Url: https://yadi.sk/d/zffFtRhhjjDUd

Summary: 
Kernel Manage - kernel update program

Summary(ru_RU): 
Kernel Manage - программа обновления ядра

Description:
Graphical shell for scripts: update-kernel, remove-old-kernels
Rendering the interface Qt5\PyQt5
Language logic Python 3
The program can update the kernel, change the build type, remove old kernels, clean the file storage, update the distribution.

Description (ru_RU):
Графическая оболочка для скриптов: update-kernel, remove-old-kernels
Отрисовка интерфейса Qt5\PyQt5
Языковая логика Python 3
Программа умеет обновлять ядро, изменять тип сборки, удалять старые ядра, очищать файловое хранилище, обновлять дистрибутив.

Modules to work properly:
Requires: xterm
Requires: python3-base
Requires: python3-module-PyQt5
Requires: xdg-utils
Requires: update-kernel

Changelog:
* Mon Nov 30 2020 Koi <eg.evgeniy@gmail.com> 1.4-alt1
- New version

* Thu Nov 26 2020 Koi <eg.evgeniy@gmail.com> 1.3-alt1
- initial build
