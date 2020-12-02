#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python
import os
import re
import sys
from subprocess import run, PIPE
from getpass import getuser
from platform import release
from threading import Thread
# PyQt
from PyQt5 import QtWidgets, QtGui
# Forms
from form.main_win import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Главное окно"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.combobox_flavour()
    
        Thread(target=self.update_cache).start()
        Thread(target=self.systemic_kernel).start()
        
        # Кнопки
        self.pushButton_DISTR.clicked.connect(self.distribution_up)
        self.pushButton_DELK.clicked.connect(self.del_kernel_old)
        self.pushButton_Clean.clicked.connect(self.cache_clear_apt)
        self.pushButton_KERN.clicked.connect(self.upgrade_kernel)
        self.pushButton_ChangeFlavour.clicked.connect(self.change_flavour)
        
    def update_cache(self):
        """Обновление кэша"""
        self.bar("kernel " + release())

        up_cache = "apt-get update"
        users = getuser()
        
        if users == 'root':
            self.button_switch(True)
            
            self.bar('Обновление cache ждите завершения...')            
            
            run(up_cache, shell=True)
            
            self.button_switch(False)
            
            Thread(target=self.search_kernel).start()
            
            
    def bar(self, messages):
        """Передача информации в статус бар"""
        self.statusbar.showMessage(messages)
            
            
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
            self.bar("kernel " + release())
        elif new_version > real_number:
            self.bar("kernel " + release() + " --> " + new_version)
            
            
    def systemic_kernel(self):
        """Системные ядера"""
        real_number = self.search_re(kernel_num=release())
        
        kernel_sys = run(
            'rpm -qa | grep kernel-image-', \
                shell=True, stdout=PIPE, encoding='utf-8').stdout
        
        raw_list_kernel = self.search_re(prefix=kernel_sys)
        kernel_list = []
        
        for x in raw_list_kernel.splitlines():
            pkg = run(f'apt-cache pkgnames {x}', \
                shell=True, stdout=PIPE, encoding='utf-8').stdout
            
            kernel_list.append(pkg.rstrip())
            
        for x in kernel_list:
            if real_number in x:
                kernel_list.remove(x)
                
        if not kernel_list:
            kernel_list.append('Ядра для удаления не обнаружены (no)')
            
        self.show_list_kernel_gui(kernel_list)
        
        
    def combobox_flavour(self):
        """Widget comboBox и список flavour в нем"""
        self.comboBox_ChangeKernel.addItem('Flavour - не выбран')
        self.comboBox_ChangeKernel.addItem('Ядро STD-DEF ( основное ядро )')
        self.comboBox_ChangeKernel.addItem('Ядро OLD-DEF ( старая ветка std-def )')
        self.comboBox_ChangeKernel.addItem('Ядро UN-DEF ( экспериментальное ядро )')
        
            
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
        
        
    # Функции кнопок
    def remove_kernel(self, item):
        """Удаление ядра из списка listwidget """
        if 'no' in item.text():
            pass
        else:
            run(f"xterm -e 'apt-get remove {item.text()} ; \
                sleep 3'", shell=True)
            
            self.update_list_kernel()
            
            
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
            run(f"xterm -e 'apt-get dist-upgrade ; \
                update-kernel -t {flavour} ; sleep 3'", shell=True)
        except UnboundLocalError:
            pass
        else:
            self.update_list_kernel()
        
        
    def distribution_up(self):
        """Обновить дистрибутив"""
        run("xterm -e 'apt-get dist-upgrade ; \
            sleep 3'", shell=True)

        
    def del_kernel_old(self):
        """Удаление старых ядер"""
        run("xterm -e 'remove-old-kernels ; \
            sleep 3'",shell=True)
        
        self.update_list_kernel()
        
        
    def cache_clear_apt(self):
        """Очистка кэша пакетов"""
        run("xterm -e 'apt-get autoclean ; \
            sleep 3'", shell=True)
        
        
    def upgrade_kernel(self):
        """Обновление ядра"""
        run("xterm -e 'apt-get dist-upgrade ; \
            update-kernel ; sleep 3'", shell=True)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    k_m = MainWindow()
    k_m.show()
    
    sys.exit(app.exec_())
