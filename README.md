Kernel Manage

Source Code: https://github.com/Koi-foo/kernel-manager.git

Summary:
program for updating kernels in altlinux p9

Description:
Graphical shell for scripts: update-kernel, remove-old-kernels
Rendering the interface Qt5\PyQt5
Language logic Python 3
The program can update the kernel, change the build type, remove old kernels, clean the file storage, update the distribution.

Version Python 3

Requires:
xterm
python3-base
python3-module-PyQt5
xdg-utils
update-kernel

Install
kernel-manager.desktop %buildroot%_desktopdir
opt/kernel-manager

Files
#%_desktopdir/kernel-manager.desktop
/opt/kernel-manager/kernel_manager.py
/opt/kernel-manager/icons*
/opt/kernel-manager/form*
/opt/kernel-manager/mod*
/opt/kernel-manager/LICENSE
/opt/kernel-manager/README.md
/opt/kernel-manager/resources.py

Changelog
* Mon Nov 30 2020 1.4
- New version

* Thu Nov 26 2020 1.3
- initial build
