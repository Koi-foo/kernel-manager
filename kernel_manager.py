#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python
import os
import re
import sys
import datetime
import gettext
from subprocess import run, PIPE
from getpass import getuser
from platform import release
from threading import Thread
# PyQt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal
# Forms
from form.main_win import Ui_MainWindow
from form.process_win import Ui_InfoProcessWin
# Language localization
gettext.install('kernel_manager', 'locale')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Главное окно"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.proc_win = ProcessWindow()
        
        self.bar()
        self.combobox_flavour()
        
        Thread(target=self.systemic_kernel).start()
        Thread(target=self.update_cache).start()
        
        # Кнопки
        self.pushButton_DISTR.clicked.connect(self.distribution_up)
        self.pushButton_DELK.clicked.connect(self.del_kernel_old)
        self.pushButton_Clean.clicked.connect(self.cache_clear_apt)
        self.pushButton_KERN.clicked.connect(self.upgrade_kernel)
        self.pushButton_ChangeFlavour.clicked.connect(self.change_flavour)
        
        # Сигналы
        self.proc_win.closeWindow.connect(self.close_window)
        
        
    def update_cache(self):
        """Обновление кэша"""
        user = getuser()
        if user != 'root':
            sys.exit(0)
        
        up_cache = "apt-get update"
        
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
            
                run(up_cache, shell=True)
                
                self.button_switch(False)
                                
        Thread(target=self.search_kernel).start()
        
            
    def bar(self, messages='0', new_version=''):
        """Передача информации в статус бар"""
        # U - Обновление кэша
        # N - Доступна новая версия ядра
        # 0 - Сообщение по умолчанию активное ядро
        if messages == 'U':
            self.statusbar.showMessage(_('Updating cache wait for completion ...'))
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
            act = self.search_re(kernel_num=x)
            if act > new_version:
                new_version = act
        
        self.compare_kernel(new_version, real_number) 
        
        
    def search_re(self, kernel_num='', kernel_flavour='', prefix=''):
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
            del_prefix = search_prefix.sub("", prefix).replace('f-', 'f#1:')
            return del_prefix
        
        
    def compare_kernel(self, new_version, real_number):
        """Сравнения версий ядер"""
        if new_version == real_number:
            self.bar()
        elif new_version > real_number:
            self.bar(messages='N', new_version=new_version)
            
            
    def systemic_kernel(self):
        """Системные ядера"""
        user = getuser()
        if user != 'root':
            sys.exit(0)
        
        real_number = self.search_re(kernel_num=release())
     
        kernel_sys = run(
            'rpm -qa | grep kernel-image-', \
                shell=True, stdout=PIPE, encoding='utf-8').stdout

        raw_list_kernel = self.search_re(prefix=kernel_sys)
        kernel_list = []
        
        for x in raw_list_kernel.splitlines():
            pkg = run(f'apt-cache pkgnames {x}', \
                shell=True, stdout=PIPE, encoding='utf-8').stdout
            
            if not pkg:
                for i in [2, 3, 4, 5]:
                    x = x.replace('f#1:', f'f#{i}:')
                    pkg = run(f'apt-cache pkgnames {x}', \
                        shell=True, stdout=PIPE, encoding='utf-8').stdout
                    if not pkg:
                        continue

            kernel_list.append(pkg.rstrip())
 
        for x in kernel_list:
            if real_number in x:
                kernel_list.remove(x)
                
        if not kernel_list:
            kernel_list.append(_('No kernels found to be removed'))
            
        self.show_list_kernel_gui(kernel_list)
        
        
    def combobox_flavour(self):
        """Widget comboBox и список flavour в нем"""
        self.comboBox_ChangeKernel.addItem(_('Flavor - not selected'))
        self.comboBox_ChangeKernel.addItem(_('STD-DEF kernel (main kernel)'))
        self.comboBox_ChangeKernel.addItem(_('OLD-DEF kernel (old std-def branch)'))
        self.comboBox_ChangeKernel.addItem(_('UN-DEF kernel (experimental kernel)'))
        
            
    def show_list_kernel_gui(self, kernel_list):
        """Показать список ядер в listwidget"""
        for x in kernel_list:
            self.listWidget_Kernel.addItem(x)
            
        self.listWidget_Kernel.itemDoubleClicked.connect(self.remove_kernel)


    def button_switch(self, btn_off_on):
        """Выключатель кнопок"""
        self.pushButton_DISTR.setDisabled(btn_off_on)
        self.pushButton_DELK.setDisabled(btn_off_on)
        self.pushButton_Clean.setDisabled(btn_off_on)
        self.pushButton_KERN.setDisabled(btn_off_on)
        self.pushButton_ChangeFlavour.setDisabled(btn_off_on)
        
        
    def update_list_kernel(self):
        """Обновление виджета listwidget"""
        self.listWidget_Kernel.clear()
        Thread(target=self.systemic_kernel).start()
        
        
    def close_window(self):
        """Cлот закрытия окна"""
        self.update_list_kernel()
 
 
    # Функции кнопок
    def remove_kernel(self, item):
        """Удаление ядра из списка listwidget """
        if 'Ядра' in item.text():
            pass
        else:            
            command = f"apt-get remove {item.text()}"
        
            self.proc_win.show()
            self.proc_win.setWindowTitle(_('Removing the kernel'))
      
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
        
        try:
            command = f"update-kernel -t {flavour}"
        
            self.proc_win.show()
            self.proc_win.setWindowTitle(f'Установка flavour-{flavour}')
      
            self.proc_win.start_qprocess(command)
        
            self.proc_win.textEdit.clear()
            
        except UnboundLocalError:
            pass
        
        
    def distribution_up(self):
        """Обновить дистрибутив"""
        command = "apt-get dist-upgrade"
        
        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Distribution update'))
        
        self.proc_win.start_qprocess(command)
        
        self.proc_win.textEdit.clear()
   
   
    def del_kernel_old(self):
        """Удаление старых ядер"""
        command = "remove-old-kernels"
        
        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Removing old kernels'))
        
        self.proc_win.start_qprocess(command)
        
        self.proc_win.textEdit.clear()
                
        
    def cache_clear_apt(self):
        """Очистка кэша пакетов"""
        command = "apt-get autoclean"
        
        self.proc_win.show()
        self.proc_win.setWindowTitle(_('Cleaning apt-cache'))

        self.proc_win.start_qprocess(command)
        
        self.proc_win.textEdit.clear()
        
        
    def upgrade_kernel(self):
        """Обновление ядра"""
        command = "update-kernel"
        
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
                                
        #Кнопки
        self.pushButton_Cancel.clicked.connect(self.cancel_button)
        self.pushButton_Ok.clicked.connect(self.confirm_button)
        
        
    def closeEvent(self, event):
        """Переопределение события"""
        self.closeWindow.emit()
        
        
    def start_qprocess(self, command=''):
        """Запуск qprocess в окне process_win"""
        self.qproc = QtCore.QProcess()
        
        self.bar(messages='W')
        
        self.qproc.finished.connect(self.bar)
        self.qproc.start(command)
            
        self.qproc.readyRead.connect(self.text_widget)
        
        
    def bar(self, messages='0'):
        """Передача информации в статус бар"""
        # W - Ждать завершения работы
        if messages == 'W':
            self.statusbar.showMessage(_('Process started, please wait ...'))
        else:
            self.statusbar.showMessage(_('Completed successfully'))
            self.textEdit.insertPlainText(_('The process is complete. You are multiplying to close the window.'))
   
   
    def text_widget(self):
        """Параметры виджета textEdit"""
        content = self.qproc.readAll().data().decode('utf-8')
        
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(content)
        self.textEdit.ensureCursorVisible()
        
        
    #Функции кнопок    
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
