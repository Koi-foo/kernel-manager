#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python
import os
import re
import sys
import datetime
import gettext
from subprocess import run, PIPE, Popen
from platform import release
from threading import Thread
from time import sleep
# PyQt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem
# Forms
from form.main_win import Ui_MainWindow
from form.process_win import Ui_InfoProcessWin
# Language localization
gettext.install('kernel_manager', '/opt/kernel-manager/locale')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Главное окно"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.proc_win = ProcessWindow()

        self.bar()
        self.combobox_flavour()
        self.combobox_repo()

        Thread(target=self.systemic_kernel).start()
        Thread(target=self.update_cache).start()

        # Кнопки
        # Исправление не верного растяжения кнопки в греческой локали
        greek_lang = run('printenv LANG', shell=True, stdout=PIPE, encoding='utf-8').stdout
        if greek_lang.rstrip() == 'el_GR.UTF-8':
            self.pushButton_KERN.setMinimumSize(0, 0)

        self.pushButton_DISTR.clicked.connect(self.distribution_up)
        self.pushButton_DELK.clicked.connect(self.del_kernel_old)
        self.pushButton_Clean.clicked.connect(self.cache_clear_apt)
        self.pushButton_KERN.clicked.connect(self.upgrade_kernel)
        self.pushButton_ChangeFlavour.clicked.connect(self.change_flavour)

        # Сигналы
        self.proc_win.closeWindow.connect(self.update_list_kernel)
        self.listWidget_Kernel.installEventFilter(self)


    def update_cache(self):
        """Обновление кэша"""
        try:
            current_date = datetime.date.today()
            date_change = datetime.date.fromtimestamp(
                os.path.getmtime('/var/lib/apt/lists/lock'))
            compare_dates = current_date > date_change
        except PermissionError:
            pass
        else:
            if compare_dates:
                self.button_switch(True)
                self.bar(messages='U')
                self.button_switch(False)

        Thread(target=self.search_kernel).start()


    def bar(self, messages='0', new_version=None):
        """Передача информации в статус бар"""
        # U - Обновление кэша
        # N - Доступна новая версия ядра
        # 0 - Сообщение по умолчанию активное ядро
        if messages == 'U':
            self.statusbar.showMessage(_('Updating cache wait for completion ...'))

            up_cache = Popen("LANG=en apt-get update", shell=True, stdout=PIPE, encoding='utf-8')

            search_number = re.compile(r':([1-9]{1})\s')
            fulfilled = 0

            for line in up_cache.stdout.readlines():
                num_repo = "".join(search_number.findall(line))

                try:
                    if int(num_repo) > int(fulfilled):
                        fulfilled = num_repo
                        self.statusbar.showMessage(_('Updating cache:') + ' ' + fulfilled + "5%")
                        sleep(1)

                except ValueError:
                    if 'Could' in line:
                        self.statusbar.showMessage(_('No access to repository'))
                        sleep(3)

                    elif 'Building' in line:
                        self.statusbar.showMessage(_('Updating completed:') + ' ' + "100%")
                        sleep(2)

        elif messages == 'N':
            self.statusbar.showMessage("kernel " + release() + " ➤ " + new_version)
        else:
            self.statusbar.showMessage("kernel " + release())


    def search_kernel(self):
        """Поиск ядра для обновления"""
        flavour = self.search_re(kernel_flavour=release())
        real_number = self.search_re(kernel_num=release())
        new_version = real_number

        search_version = run(
            f"apt-cache pkgnames kernel-image-{flavour}#",
            shell=True, stdout=PIPE, encoding='utf-8').stdout

        for x in search_version.splitlines():
            act = self.search_re(kernel_num=x).split(".")

            if int(act[0]) > int(new_version.split(".")[0]):
                new_version = ".".join(act)

            if int(act[1]) > int(new_version.split(".")[1]):
                new_version = ".".join(act)

            if int(act[2]) > int(new_version.split(".")[2]):
                new_version = ".".join(act)

        self.compare_kernel(new_version, real_number) 


    def search_re(self, kernel_num=None, kernel_flavour=None, prefix=None):
        """Извлечение элементов"""
        search_num = re.compile(r'[2-9]\.[0-9]{1,2}\.?[0-9]{0,3}(?=-)')
        search_flavour = re.compile(r'[a-z]+-[def]{3}')
        search_prefix = re.compile(r'-alt.*')

        if kernel_num:
            num_version = "".join(search_num.findall(kernel_num))
            return num_version

        elif kernel_flavour:
            flavour_type = "".join(search_flavour.findall(kernel_flavour))
            return flavour_type

        elif prefix:
            del_prefix = search_prefix.sub("", prefix).replace('f-', 'f | grep ')
            return del_prefix


    def compare_kernel(self, new_version, real_number):
        """Сравнения версий ядер"""
        if new_version == real_number:
            self.bar()
        else:
            self.bar(messages='N', new_version=new_version)


    def systemic_kernel(self):
        """Системные ядра"""
        real_number = self.search_re(kernel_num=release())

        raw_list_kernel = run(
            'rpm -qa | grep kernel-image-', \
                shell=True, stdout=PIPE, encoding='utf-8').stdout.splitlines()

        kernel_list = []
        platform = re.compile(r': ([a-zA-Z0-9]+)')

        for line in raw_list_kernel:
            kernel_info = run(f'rpm -qi {line} | grep Install', shell=True, stdout=PIPE, \
            encoding='utf-8').stdout

            dist_tag = str(platform.findall(run(f'rpm -qi {line} | grep DistTag', \
            shell=True, stdout=PIPE, encoding='utf-8').stdout))

            kernel_list.append(line + "  ➞  " + kernel_info.rstrip() + "  ➞  " + dist_tag)

        for line in kernel_list:
            if real_number in line:
                kernel_list.remove(line)

        if not kernel_list:
            kernel_list.append(_('No kernels found to be removed'))

        self.show_list_kernel_gui(kernel_list)


    def combobox_flavour(self):
        """Widget comboBox и список flavour в нем"""
        self.comboBox_ChangeKernel.addItem(_('Flavor - not selected'))
        self.comboBox_ChangeKernel.addItem(_('STD-DEF kernel (main kernel)'))
        self.comboBox_ChangeKernel.addItem(_('OLD-DEF kernel (old std-def branch)'))
        self.comboBox_ChangeKernel.addItem(_('UN-DEF kernel (experimental kernel)'))
        self.comboBox_ChangeKernel.addItem(_('Sisyphus (kernel un-def)'))


    def combobox_repo(self):
        """Widget comboBox и список репозиториев в нем"""
        current_repo = run('apt-repo', shell=True, stdout=PIPE, \
            encoding='utf-8').stdout.splitlines()[1]
        list_repo = ["p9", "Sisyphus"]

        for name_repo in list_repo:
            if name_repo in current_repo:
                self.comboBox_ChangeRepo.addItem(name_repo)
                list_repo.remove(name_repo)

                for name_repo in list_repo:
                    self.comboBox_ChangeRepo.addItem(name_repo)


    def show_list_kernel_gui(self, kernel_list):
        """Показать список ядер в listwidget"""
        self.listWidget_Kernel.clear()
        self.listWidget_Kernel.setIconSize(QSize(30, 12))

        for line in kernel_list:
            if "std" in line:
                icon = ":/picture/icons/std-p.png"

            elif "un" in line:
                icon = ":/picture/icons/un-p.png"

            elif "old" in line:
                icon = ":/picture/icons/old-p.png"

            else:
                icon = ":/picture/icons/no-p.png"

            item = QListWidgetItem(QIcon(icon), line)
            self.listWidget_Kernel.addItem(item)

        self.listWidget_Kernel.itemDoubleClicked.connect(self.signal_list_kernel)


    def signal_list_kernel(self, item):
        """Обработка сигнала списка"""
        if "kernel" in item.text():
            self.remove_kernel(item)
        else:
            pass


    def eventFilter(self, source, event):
        """Фильтр событий виджета listWidget и контекстное меню"""
        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.listWidget_Kernel):
            menu = QtWidgets.QMenu()

            remove = menu.addAction(
                QIcon(":/picture/icons/list-remove.svg"), _('Remove the selected kernel'))

            default = menu.addAction(
                QIcon(":/picture/icons/go-up.svg"), _('Install the default kernel'))

            action = menu.exec_(event.globalPos())
            item = source.itemAt(event.pos())

            try:
                for i in ["std-", "un-", "old-"]:
                    if i in item.text():
                        if action == remove:
                            self.signal_list_kernel(item)

                        elif action == default:
                            self.boot_default(item)
                    else:
                        pass
            except AttributeError:
                pass

            return True

        return super().eventFilter(source, event)


    def button_switch(self, btn_off_on):
        """Выключатель кнопок"""
        self.pushButton_DISTR.setDisabled(btn_off_on)
        self.pushButton_DELK.setDisabled(btn_off_on)
        self.pushButton_Clean.setDisabled(btn_off_on)
        self.pushButton_KERN.setDisabled(btn_off_on)
        self.pushButton_ChangeFlavour.setDisabled(btn_off_on)


    def update_list_kernel(self):
        """Обновление виджета listwidget"""
        Thread(target=self.systemic_kernel).start()


    def branches(self):
        """Смена репозиториев"""
        current_repo = run('apt-repo', shell=True, stdout=PIPE, \
            encoding='utf-8').stdout.splitlines()[1]
        combobox_text = self.comboBox_ChangeRepo.currentText()

        if combobox_text in current_repo:
            list_command = ("/bin/sh -c "
                '"apt-get dist-upgrade"')
            return list_command

        elif combobox_text == 'Sisyphus' and combobox_text not in current_repo:
            list_command = ("/bin/sh -c "
                '"apt-get dist-upgrade ; "'
                '"apt-repo rm all ; "'
                '"apt-repo add Sisyphus ; "'
                '"apt-get clean ; "'
                '"apt-get update ; "'
                '"apt-get install apt rpm ; "'
                '"apt-get dist-upgrade ; "'
                '"update-kernel"')
            return list_command

        elif combobox_text not in current_repo:
            change_repo = run(f'apt-repo rm all ; apt-repo add {combobox_text}', shell=True)
            self.bar()

            list_command = ("/bin/sh -c "
                '"apt-get update ; "'
                '"apt-get dist-upgrade"')
            return list_command


    # Функции кнопок
    def boot_default(self, item):
        """Установка загрузки ядра по умолчанию"""
        kernel = item.text().split(None, 1)[0].replace(
            'kernel-image-', '').rsplit('.', 1)[0].split('-')

        kernel[0], kernel[1], kernel[2] = kernel[2], kernel[0], kernel[1]
        kernel_num = kernel[0] 
        kernel = "-".join(kernel)

        text = _('Set default kernel boot') + f": {kernel_num}?"

        command = (self.dialog(text)
            + f'"installkernel {kernel}"')

        self.proc_win.show()
        self.proc_win.setWindowTitle(
            _('Setting the default kernel boot') + f': v{kernel_num}')
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def dialog(self, text):
        """Текстовый диалог для окна выполнения процессов"""
        script = ("/bin/sh -c "
            f'"echo {text} ; read answer ; "'
            '"if [ "$answer" == "n" ]; then exit; fi ; "')
        return script


    def remove_kernel(self, item):
        """Удаление ядра из списка listwidget """
        release = re.search(r'alt[0-9]', item.text()).group()
        kernel_select = run("apt-cache pkgnames" + " " \
            + self.search_re(prefix=item.text().split(None, 1)[0]) + f"-{release}", \
            shell=True, stdout=PIPE, encoding='utf-8').stdout.rstrip()

        version = re.split('[: -]', kernel_select)[4]

        command = ("/bin/sh -c "
            f'"apt-get remove {kernel_select}"')

        self.proc_win.update_kernel = True
        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Removing the kernel') + " " + version)
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def change_flavour(self):
        """Изменить тип ядра"""
        combobox_item = self.comboBox_ChangeKernel.currentIndex()

        if 0 == combobox_item:
            pass

        elif 1 == combobox_item:
            flavour = 'std-def'

        elif 2 == combobox_item:
            flavour = 'old-def'

        elif 3 == combobox_item:
            flavour = 'un-def'

        elif 4 == combobox_item:
            self.sisyphus_flavour()

        try:
            self.branches()

            command = f"update-kernel -t {flavour}"

            self.proc_win.update_kernel = True
            self.proc_win.show()
            self.proc_win.setWindowTitle(_('Installation') + " " + f'flavour-{flavour}')
            self.proc_win.start_qprocess(command)
            self.proc_win.textEdit.clear()

        except UnboundLocalError:
            pass


    def sisyphus_flavour(self):
        """Замена ядра на ядро UN-DEF из Sisyphus"""
        combobox_text = self.comboBox_ChangeRepo.currentText()
        flavour = 'un-def'

        command = ("/bin/sh -c "
            '"apt-repo rm all ; "'
            '"apt-repo add Sisyphus ; "'
            '"apt-get\" \"update" + "; "'
            f'"update-kernel -t {flavour} ; "'
            '"apt-repo rm all ; "'
            f'"apt-repo add {combobox_text} ; "'
            '"apt-get update"')

        self.proc_win.update_kernel = True
        self.proc_win.show()
        self.proc_win.setWindowTitle(f'Sisyphus flavour-{flavour}')
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def distribution_up(self):
        """Обновить дистрибутив"""
        command = self.branches()

        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Distribution update'))
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def del_kernel_old(self):
        """Удаление старых ядер"""
        command = "remove-old-kernels"

        self.proc_win.update_kernel = True
        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Removing old kernels'))
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def cache_clear_apt(self):
        """Очистка кэша пакетов"""
        command = ("/bin/sh -c "
            '"apt-get autoclean ; "'
            '"apt-get dedup"')

        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Cleaning apt-cache'))
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def upgrade_kernel(self):
        """Обновление ядра"""
        self.branches()

        command = "update-kernel"

        self.proc_win.update_kernel = True
        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Kernel update'))
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


class ProcessWindow(QtWidgets.QMainWindow, Ui_InfoProcessWin):
    closeWindow = pyqtSignal()
    """Окно выолнения процессов"""
    def __init__(self):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.update_kernel = False

        #Кнопки
        self.close_button()
        self.pushButton_Cancel.clicked.connect(self.cancel_button)
        self.pushButton_Ok.clicked.connect(self.confirm_button)


    def closeEvent(self, event):
        """Переопределение события завершения"""
        for name_process in ["apt-get dist-upgrade"]:
            activ_process = run(f'pidof {name_process}', shell=True, \
                stdout=PIPE, encoding='utf-8').stdout

            if activ_process:
                close_process = run(f'kill {activ_process}', shell=True)

        if self.update_kernel:
            self.update_kernel = False
            self.closeWindow.emit()


    def start_qprocess(self, command):
        """Запуск qprocess в окне process_win"""
        self.qproc = QtCore.QProcess()
        self.bar(messages=True)
        self.qproc.stateChanged.connect(self.signal_qprocess)
        self.qproc.finished.connect(self.bar)
        self.qproc.start(command)
        self.qproc.readyRead.connect(self.text_widget)


    def bar(self, messages):
        """Передача информации в статус бар"""
        if messages is True:
            self.statusbar.showMessage(_('Process started, please wait ...'))
        else:
            self.statusbar.showMessage(_('Completed successfully'))
            self.textEdit.insertPlainText(_('The process is complete. You can close the window.'))


    def text_widget(self):
        """Параметры виджета textEdit"""
        content = self.qproc.readAll().data().decode('utf-8')

        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)

        self.textEdit.insertPlainText(content)
        self.textEdit.ensureCursorVisible()


    def signal_qprocess(self, state):
        """Сигнал состояния запученного процесса"""
        if state >= 1:
            self.pushButton_Close.hide()
            self.pushButton_Ok.show()
        else:
            self.pushButton_Close.show()
            self.pushButton_Ok.hide()


    #Функции кнопок
    def close_button(self, state=None):
        """Закрыть окно выполнения процессов"""
        self.pushButton_Close = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Close.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.gridLayout_2.addWidget(self.pushButton_Close, 1, 2, 1, 1)
        self.pushButton_Close.setText(_("Close"))
        self.pushButton_Close.setToolTip(_("Close a window"))
        self.pushButton_Close.clicked.connect(lambda:self.close())


    def confirm_button(self):
        """Подтвердить установку"""
        command = 'y' + "\n"

        try:
            self.qproc.write(command.encode())
        except AttributeError:
            pass


    def cancel_button(self):
        """Отменить установку"""
        command = 'n' + "\n"

        try:
            self.qproc.write(command.encode())
        except AttributeError:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    k_m = MainWindow()
    k_m.show()

    sys.exit(app.exec_())
