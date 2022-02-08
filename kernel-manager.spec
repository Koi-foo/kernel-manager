Name: kernel-manager
Version: 1.7
Release: alt11

License: LGPL-3.0-only
Group: System/Base
Url: https://github.com/Koi-foo/kernel-manager
Packager: Koi <eg.evgeniy at gmail.com>
Source0: %{name}-%{version}.tar

BuildRequires: rpm-build-python3
Requires: python3-base >= 3.7.0
Requires: python3-module-PyQt5
Requires: python3-module-gettext
Requires: update-kernel
Requires: apt-repo
Requires: apt-scripts

Provides: oldproject = %{version}-%{release}
BuildArch: noarch
Obsoletes: oldproject <= 1.7

Summary: Kernel Manage - kernel update program
Summary(ru_RU.UTF-8): Kernel Manage - программа обновления ядра

%description
Graphical shell for scripts: update-kernel, remove-old-kernels
Rendering the interface Qt5\PyQt5
Language logic Python 3
The program can update the kernel, change the build type, remove old kernels,
clean the file storage, update the distribution.

%description -l ru_RU.UTF8
Графическая оболочка для скриптов: update-kernel, remove-old-kernels
Отрисовка интерфейса Qt5\PyQt5
Языковая логика Python 3
Программа умеет обновлять ядро, изменять тип сборки, удалять старые ядра,
очищать файловое хранилище, обновлять дистрибутив.

%add_findreq_skiplist /opt/kernel-manager/*

%prep
%setup

%install
mkdir -p %{buildroot}%{_desktopdir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_pixmapsdir}
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
mkdir -p %{buildroot}/opt/kernel-manager/mod

install -Dm644 *.desktop %{buildroot}%{_desktopdir}
install -Dm755 kernel-manager %{buildroot}%{_bindir}
install -Dm644 org.freedesktop.pkexec.kernel-manager.policy %{buildroot}%{_datadir}/polkit-1/actions

install -Dm755 kernel_manager.py %{buildroot}/opt/kernel-manager
install -Dm755 kernel-indicator %{buildroot}/opt/kernel-manager
install -Dm644 resources.py %{buildroot}/opt/kernel-manager
install -Dm755 mod/shell.py %{buildroot}/opt/kernel-manager/mod
cp -r {data,form,icons,locale} %{buildroot}/opt/kernel-manager

%files
%doc LICENSE README.md
%ghost /opt/kernel-manager/locale/kernel_manager.pot.old
%{_desktopdir}/*.desktop
/opt/kernel-manager
%{_datadir}/polkit-1/actions/org.freedesktop.pkexec.kernel-manager.policy
%{_bindir}/kernel-manager
%dir /opt/kernel-manager/data

%changelog
* Mon Nov 08 2021 Evgeny Chuck <koi@altlinux.org> 1.7-alt11
- Fixed translation (Russian)
- Added function to jump to p10
- Fixed bug with switching to p10

* Sat Jun 26 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt10
- Fixed display of the icon for cleaning unnecessary packages
- Fixed translation string before installing default kernel in Greek translation

* Wed May 19 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt9
- Added functionality for managing modules

* Sun May 02 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt8
- Improved the launch of polkit
- Fixed a bug with the unregistered release version

* Tue Apr 20 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt7
- Fixed crash when deleting empty list.
- Adding a Close Window Button.

* Tue Apr 20 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt6
- Added PolKit
- Fixed crash when list is empty
- Faster list and GUI updates.

* Fri Mar 19 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt5
- Updated app interface
- A context menu has been added to the kernel removal tab
- Added checking the status of the Internet connection

* Sun Feb 21 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt3
- Changed descriptions of buttons cleaning and distribution
- Replaced template for kernel lists
- Improved the logic for changing the branch
- Added images of kernels to the remove kernels list
- Updated translations

* Sun Feb 14 2021 Koi <eg.evgeniy@gmail.com> 1.7-alt2
- New panel status feature
- New widget for the list of kernel
- Updated interface

* Wed Feb 3 2021 Koi <eg.evgeniy@gmail.com> 1.6-alt6
- Improved search algorithms for kernels.
- Fixed a bug in the clear button interface.
- Fixed an incorrect message in the status bar about a new kernel.
- Added update of package cache when switching to different branches.
- Updated description in the program help for the Kernel Removal tab.
- Search for new kernels is accelerated

* Wed Feb 3 2021 Koi <eg.evgeniy@gmail.com> 1.6-alt5
- Added transition to Sisyphus repository.
- Added removal of duplicates

* Wed Jan 20 2021 Koi <eg.evgeniy@gmail.com> 1.6-alt4
- Added the ability to translate into different languages.
- Added a kernel from Sisyphus

* Sun Jan 17 2021 Koi <eg.evgeniy@gmail.com> 1.6-alt3
- Added the ability to translate into different languages.

* Tue Dec 15 2020 Koi <eg.evgeniy@gmail.com> 1.6-alt2
- Added the ability to translate into different languages.

* Sat Dec 12 2020 Koi <eg.evgeniy@gmail.com> 1.6-alt1
- New version

* Mon Nov 30 2020 Koi <eg.evgeniy@gmail.com> 1.4-alt1
- New version

* Thu Nov 26 2020 Koi <eg.evgeniy@gmail.com> 1.3-alt1
- initial build
