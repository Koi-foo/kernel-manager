#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Python
import os
import re
import sys
import json
import datetime
import gettext
from subprocess import run, PIPE, Popen
from platform import release
from threading import Thread
from time import sleep
from mod.shell import shrun, shcom
from mod.load_config import loadConfig, saveFileConfig
# PyQt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem
# Forms
from form.main_win import Ui_MainWindow
from form.process_win import Ui_InfoProcessWin
from form.info_win import Ui_DialogInfo
# Изменить рабочий путь
os.chdir(os.path.dirname(sys.argv[0]))
# Языковая локализация
gettext.install('kernel_manager', 'locale')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    modulesList = pyqtSignal()
    kernelList = pyqtSignal(list)
    """Главное окно"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.proc_win = ProcessWindow()
        self.infoWin = DialogInformation()
        self.window_size()
        self.message_bar = QtWidgets.QLabel()
        self.message_bar.setMargin(4)
        self.statusbar.addWidget(self.message_bar)
        self.config = loadConfig()

        self.bar()
        self.combobox_flavour()
        self.combobox_repo()
        self.spinBox()
        self.comboBoxService()
        self.comboBoxTime()

        Thread(target=self.systemic_kernel).start()
        Thread(target=self.modules_system).start()
        Thread(target=self.update_cache).start()

        self.pushButton_DISTR.clicked.connect(self.distribution_up)
        self.pushButton_DELK.clicked.connect(self.del_kernel_old)
        self.pushButton_Clean.clicked.connect(self.cache_clear_apt)
        self.pushButton_KERN.clicked.connect(self.upgrade_kernel)
        self.pushButton_ChangeFlavour.clicked.connect(self.change_flavour)
        self.pushButton_Autoremove.clicked.connect(self.autoremove)
        self.pushButton_Rpmrebuild.clicked.connect(self.rpm_rebuild)

        # Сигналы
        self.proc_win.closeWindow.connect(self.update_list_kernel)
        self.modulesList.connect(self.signal_combobox_modules)
        self.kernelList.connect(self.show_list_kernel_gui)
        self.listWidget_Kernel.customContextMenuRequested.connect(self.kernel_context_menu)
        self.comboBox_ModulesSystem.currentIndexChanged.connect(self.signal_combobox_modules)
        self.listWidget_Kernel.itemDoubleClicked.connect(self.double_clicked_kernel)
        self.listWidget_Modules.itemDoubleClicked.connect(self.double_clicked_module)
        self.listWidget_Modules.currentItemChanged.connect(self.modules_tooltip_bar)
        self.listWidget_Modules.customContextMenuRequested.connect(self.modules_context_menu)
        self.spinBoxDayUpdate.valueChanged.connect(self.dayUpdate)
        self.comboBoxTimeStart.currentTextChanged.connect(self.timeStart)
        self.comboBoxStartService.currentIndexChanged.connect(self.initService)


    def comboBoxTime(self):
        """Комбобокс для изменения время отсрочки старта"""
        index = self.comboBoxTimeStart.findText(str(self.config['time']))
        self.comboBoxTimeStart.setCurrentIndex(index)


    def dayUpdate(self, value):
        """Установка интервала обновления"""
        self.config = loadConfig()
        self.config['days'] = value
        saveFileConfig(self.config)


    def timeStart(self, value):
        """Установка время задержки старта"""
        self.config = loadConfig()
        self.config['time'] = value
        saveFileConfig(self.config)


    def comboBoxService(self):
        """Комбобокс для установки загрузки сервиса"""
        index = 0 if self.config['service'] else 1
        self.comboBoxStartService.setCurrentIndex(index)


    def initService(self, value):
        """Включение и выключение сервивы kernel-service"""
        self.config = loadConfig()
        if value:
            shrun('chkconfig kernel-service on')
            self.config['service'] = False
        else:
            shrun('chkconfig kernel-service off')
            self.config['service'] = True
        saveFileConfig(self.config)


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


    def spinBox(self):
        """Настройки переключателя"""
        self.spinBoxDayUpdate.setValue(self.config['days'])


    def bar(self, messages='0', new_version=None):
        """Передача информации в статус бар"""
        if messages == 'U':
            self.message_bar.setText(_('Updating cache wait for completion ...'))
            up_cache = Popen("LANG=en apt-get update", shell=True, stdout=PIPE, encoding='utf-8')
            search_number = re.compile(r':([1-9]{1})\s')
            fulfilled = 0
            for line in up_cache.stdout.readlines():
                num_repo = "".join(search_number.findall(line))
                try:
                    if int(num_repo) > int(fulfilled):
                        fulfilled = num_repo
                        self.message_bar.setText(_('Updating cache:') + ' ' + fulfilled + "5%")
                        sleep(1)
                except ValueError:
                    if 'Could' in line:
                        self.message_bar.setText(_('No access to repository'))
                        sleep(3)
                    elif 'Building' in line:
                        self.message_bar.setText(_('Updating completed:') + ' ' + "100%")
                        sleep(2)
        elif messages == 'N':
            self.message_bar.setText("kernel " + release() + " ➤ " + new_version)
        else:
            self.message_bar.setText("kernel " + release())


    def search_kernel(self):
        """Поиск ядра для обновления"""
        flavour = re.search(r'.*-(.+-.+)-', release()).group(1)
        real_number = release().split('-')[0]
        new_version = real_number.split('.')
        search_version = shrun(f"apt-cache pkgnames kernel-image-{flavour}#")
        for line in search_version.splitlines():
            act = re.search(r':(.+)-alt' ,line).group(1).split(".")
            if int(act[0]) > int(new_version[0]): new_version[0] = act[0]
            if int(act[1]) > int(new_version[1]): new_version[1] = act[1]
            if int(act[2]) > int(new_version[2]): new_version[2] = act[2]

        new_version = ".".join(new_version)
        self.compare_kernel(new_version, real_number)


    def compare_kernel(self, new_version, real_number):
        """Сравнения версий ядер"""
        if new_version == real_number: self.bar()
        else: self.bar(messages='N', new_version=new_version)


    def systemic_kernel(self):
        """Системные ядра"""
        kernel_list = []
        real_number = release().split('-')[0]
        raw_list_kernel = shrun('rpm -qa | grep kernel-image-').splitlines()
        for line in raw_list_kernel:
            kernel_info = shrun(f'rpm -qi {line} | grep Install')
            dist_tag = str(re.compile(r': ([a-zA-Z0-9]+)').findall(shrun(
                f'rpm -qi {line} | grep DistTag')))
            kernel_list.append(line + "  ➞  " + kernel_info.rstrip() + "  ➞  " + dist_tag)

        for line in kernel_list:
            if real_number in line:
                kernel_list.remove(line)

        if not kernel_list:
            kernel_list.append(_('No kernels found to be removed'))

        self.kernelList.emit(kernel_list)


    def combobox_flavour(self):
        """Widget comboBox и список flavour в нем"""
        self.comboBox_ChangeKernel.addItem(_('Flavor - not selected'))
        self.comboBox_ChangeKernel.addItem(_('STD-DEF kernel (main kernel)'))
        self.comboBox_ChangeKernel.addItem(_('OLD-DEF kernel (old std-def branch)'))
        self.comboBox_ChangeKernel.addItem(_('UN-DEF kernel (experimental kernel)'))
        self.comboBox_ChangeKernel.addItem(_('Sisyphus (kernel un-def)'))


    def combobox_repo(self):
        """Widget comboBox и список репозиториев в нем"""
        current_repo = shrun('apt-repo').splitlines()[1]
        list_repo = ["p9", "p10", "Sisyphus"]

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
            if "std" in line: icon = ":/picture/icons/std-p.png"
            elif "un" in line: icon = ":/picture/icons/un-p.png"
            elif "old" in line: icon = ":/picture/icons/old-p.png"
            else: icon = ":/picture/icons/no-p.png"

            item = QListWidgetItem(QIcon(icon), line)
            self.listWidget_Kernel.addItem(item)


    def double_clicked_kernel(self, item):
        """Обработка двойного клика listWidget_Kernel"""
        kernel = item.text().split()[0]
        if "kernel" in kernel: self.remove_kernel(kernel)
        else: pass


    def double_clicked_module(self, item):
        """Обработка двойного клика listWidget_Modules"""
        module = item.text()
        self.remove_kernel(module)


    def kernel_context_menu(self, pos):
        """Котекстное меню listWidget_Kernel"""
        menu = QtWidgets.QMenu(self)
        iconRemove = ":/picture/icons/list-remove.svg"
        iconUp = ":/picture/icons/go-up.svg"
        iconHelp = ":/picture/icons/help-about.svg"

        remove = menu.addAction(QIcon(iconRemove), _('Remove the selected kernel'))
        default = menu.addAction(QIcon(iconUp), _('Install the default kernel'))
        kernel_info = menu.addAction(QIcon(iconHelp), _('Kernel information'))
        action = menu.exec_(self.listWidget_Kernel.mapToGlobal(pos))

        try:
            kernel = self.listWidget_Kernel.currentItem().text().split()[0]
        except AttributeError:
            pass

        if len(kernel) < 10: pass
        elif action == remove: self.remove_kernel(kernel)
        elif action == default: self.boot_default(kernel)
        elif action == kernel_info:
            description = shrun(f'rpm -qi {kernel}')
            messages = kernel

            self.information_window(description, messages)


    def button_switch(self, btn_off_on):
        """Выключатель кнопок"""
        self.pushButton_DISTR.setDisabled(btn_off_on)
        self.pushButton_DELK.setDisabled(btn_off_on)
        self.pushButton_Clean.setDisabled(btn_off_on)
        self.pushButton_KERN.setDisabled(btn_off_on)
        self.pushButton_ChangeFlavour.setDisabled(btn_off_on)
        self.pushButton_Autoremove.setDisabled(btn_off_on)
        self.pushButton_Rpmrebuild.setDisabled(btn_off_on)


    def update_list_kernel(self):
        """Обновление виджета listwidget"""
        Thread(target=self.systemic_kernel).start()
        Thread(target=self.modules_system).start()


    def branches(self):
        """Смена репозиториев"""
        current_repo = shrun('apt-repo').splitlines()[1]
        combobox_text = self.comboBox_ChangeRepo.currentText()

        if combobox_text in current_repo:
            list_command = ("/bin/sh -c "
                '"apt-get dist-upgrade"')
            return list_command

        elif combobox_text == 'Sisyphus' and combobox_text not in current_repo:
            list_command = ("/bin/sh -c "
                '"apt-get dist-upgrade ; "'
                '"apt-repo set Sisyphus ; "'
                '"apt-get clean ; "'
                '"apt-get update ; "'
                '"apt-get install apt rpm ; "'
                '"apt-get dist-upgrade ; "'
                '"update-kernel"')
            return list_command

        elif combobox_text == 'p10' and combobox_text not in current_repo:
            list_command = ("/bin/sh -c "
                '"apt-get dist-upgrade ; "'
                '"apt-repo set p10 ; "'
                '"apt-get clean ; "'
                '"apt-get update ; "'
                '"apt-get install apt rpm ; "'
                '"apt-get dist-upgrade ; "'
                '"update-kernel -t std-def"')
            return list_command

        elif combobox_text not in current_repo:
            change_repo = shrun(f'apt-repo set {combobox_text}')
            self.bar()

            list_command = ("/bin/sh -c "
                '"apt-get update ; "'
                '"apt-get dist-upgrade"')
            return list_command


    def information_window(self, description, messages):
        """Окно информации"""
        self.infoWin.show()
        self.infoWin.setWindowTitle(messages)
        self.infoWin.textEdit_Info.setPlainText(description)


    def modules_system(self):
        """Список установленных модулей"""
        combobox_list = []
        name_modules = re.compile(r'kernel-modules-(.*)-.+-.+-.+-alt')
        modules = shrun(f'rpm -qa | grep kernel-modules').splitlines()

        with open('data/modules.json', 'w') as file_modules:
            json.dump(modules, file_modules)

        for line in modules:
            combobox_item = name_modules.search(line).group(1)
            if combobox_item not in combobox_list:
                combobox_list.append(combobox_item)

        if self.comboBox_ModulesSystem.count() == 1:
                self.comboBox_ModulesSystem.addItems(combobox_list)

        self.modulesList.emit()


    def signal_combobox_modules(self):
        """Обработка сигнала comboBox_ModulesSystem"""
        index_item = self.comboBox_ModulesSystem.currentIndex()
        text_item = self.comboBox_ModulesSystem.currentText()

        with open('data/modules.json') as file_modules:
            modules = json.load(file_modules)

        if index_item == 0: item_filter=""
        elif text_item: item_filter = text_item

        selected_modules = [x for x in modules if item_filter in x]
        self.show_list_modules_gui(selected_modules)


    def show_list_modules_gui(self, item_list):
        """Показывает список модулей на вкладке Фильтр пакетов"""
        self.listWidget_Modules.clear()
        self.listWidget_Modules.setIconSize(QSize(30, 12))

        if len(item_list) == 0:
            index = self.comboBox_ModulesSystem.currentIndex()
            self.comboBox_ModulesSystem.removeItem(index)

        for line in item_list:
            if "std" in line: icon = ":/picture/icons/std-p.png"
            elif "un" in line: icon = ":/picture/icons/un-p.png"
            elif "old" in line: icon = ":/picture/icons/old-p.png"
            else: icon = ":/picture/icons/no-p.png"

            item = QListWidgetItem(QIcon(icon), line)
            self.listWidget_Modules.addItem(item)


    def modules_tooltip_bar(self):
        """Краткое описание для модуля в статус баре"""
        try:
            module = self.listWidget_Modules.currentItem().text()

            if module == None:
                pass
            else:
                row = re.compile(r'Summary.*:.(.*)')
                summary = row.search(shrun(f'rpm -qi {module}')).group(1)

                self.statusbar.showMessage(_('Module') + ': ' + summary, 10000)
        except AttributeError:
            pass


    def modules_context_menu(self, pos):
        """Контекстное меню listWidget_Modules"""
        menu = QtWidgets.QMenu(self)
        iconRemove = ":/picture/icons/list-remove.svg"
        iconHelp = ":/picture/icons/help-about.svg"

        remove = menu.addAction(QIcon(iconRemove), _('Remove the selected module'))
        module_info = menu.addAction(QIcon(iconHelp), _('Module information'))
        action = menu.exec_(self.listWidget_Modules.mapToGlobal(pos))

        try:
            module = self.listWidget_Modules.currentItem().text()
            if action == remove:
                self.remove_kernel(module)
            elif action == module_info:
                description = shrun(f'rpm -qi {module}')
                messages = module
                self.information_window(description, messages)
        except(AttributeError, UnboundLocalError):
            pass


    def closeEvent(self, event):
        """Действия ри закрытии программы"""
        win_main_size = [
            int(self.geometry().width()),
            int(self.geometry().height())]
        settings.setValue('window_main', win_main_size)

        if self.config['service']:
            shrun('/etc/init.d/kernel-service start')


    def window_size(self):
        """Установка размера окна"""
        size = settings.value('window_main', type=int)
        if size != 0:
            self.resize(size[0], size[1])


    # Функции кнопок
    def rpm_rebuild(self):
        """Пересобрать базу"""
        text = _('Rebuild rpm database?')
        command = (self.dialog(text) +
                   '"rpm -v --rebuilddb"')

        self.proc_win.show()
        self.proc_win.setWindowTitle(_('rpm database recovery'))
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def autoremove(self):
        """Удаление ненужных пакетов используя autoremove"""
        text = _(
            'It is recommended to use for cleaning a fresh OS. If you have '
            'been using the OS for a long time, then the likelihood of removing '
            'the necessary packages increases. Continue?')

        command = (self.dialog(text) +
                   '"apt-get autoremove"')

        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Removing unnecessary dependencies'))
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def boot_default(self, item):
        """Установка загрузки ядра по умолчанию"""
        kernel = item.split(None, 1)[0].replace(
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
        package = shrun(f'rpm -qi {item}')
        name = re.compile(r'Name.*:\s(.*)').search(package).group(1) + "#"
        version = re.compile(r'Version.*:\s(.*)').search(package).group(1)
        release = re.compile(r'Release.*:\s(.*)').search(package).group(1)

        try:
            epoch = re.compile(r'Epoch.*:\s(.*)').search(package).group(1) + ":"
        except AttributeError:
            epoch = ""

        message_title = f"{name}-{version}"
        command = ("/bin/sh -c "
            f'"apt-get remove {name}{epoch}{version}-{release}*"')

        self.proc_win.update_kernel = True
        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Remove') + " " + message_title)
        self.proc_win.start_qprocess(command)
        self.proc_win.textEdit.clear()


    def change_flavour(self):
        """Изменить тип ядра"""
        combobox_item = self.comboBox_ChangeKernel.currentIndex()

        if 0 == combobox_item: pass
        elif 1 == combobox_item: flavour = 'std-def'
        elif 2 == combobox_item: flavour = 'old-def'
        elif 3 == combobox_item: flavour = 'un-def'
        elif 4 == combobox_item: self.sisyphus_flavour()

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
        text = _('Install un-def kernel from Sisyphus repository?')
        command = (self.dialog(text) +
            '"apt-repo set Sisyphus ; "'
            '"apt-get update ; "'
            f'"update-kernel -t {flavour} ; "'
            f'"apt-repo set {combobox_text} ; "'
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
        self.window_size()
        self.update_kernel = False

        #Кнопки
        self.close_button()
        self.pushButton_Cancel.clicked.connect(self.cancel_button)
        self.pushButton_Ok.clicked.connect(self.confirm_button)


    def closeEvent(self, event):
        """Переопределение события завершения"""
        for name_process in ["apt-get dist-upgrade"]:
            activ_process = shrun(f'pgrep -o "{name_process}"')

            if activ_process:
                close_process = shcom(f'kill {activ_process}')

        win_proc_size = [
            int(self.geometry().width()),
            int(self.geometry().height())]
        settings.setValue('window_proc', win_proc_size)

        if self.update_kernel:
            self.update_kernel = False
            self.closeWindow.emit()


    def window_size(self):
        """Установка размера окна"""
        size = settings.value('window_proc', type=int)
        if size != 0:
            self.resize(size[0], size[1])


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


class DialogInformation(QtWidgets.QMainWindow, Ui_DialogInfo):
    """Окно вывода информации"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window_size()


    def closeEvent(self, event):
        """Сохранение размера при закрытии"""
        win_dialog_size = [
            int(self.geometry().width()),
            int(self.geometry().height())]

        settings.setValue('window_dialog', win_dialog_size)


    def window_size(self):
        """Установка размера окна"""
        size = settings.value('window_dialog', type=int)
        if size != 0:
            self.resize(size[0], size[1])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    settings = QtCore.QSettings()
    k_m = MainWindow()
    k_m.show()

    sys.exit(app.exec_())
