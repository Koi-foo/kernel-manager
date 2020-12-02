# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/icons/kernel-manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Tab1 = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.Tab1.setFont(font)
        self.Tab1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Tab1.setIconSize(QtCore.QSize(16, 16))
        self.Tab1.setObjectName("Tab1")
        self.Tab1_Question = QtWidgets.QWidget()
        self.Tab1_Question.setObjectName("Tab1_Question")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Tab1_Question)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_Question = QtWidgets.QTextBrowser(self.Tab1_Question)
        self.text_Question.setObjectName("text_Question")
        self.gridLayout_2.addWidget(self.text_Question, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/icons/what.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Tab1.addTab(self.Tab1_Question, icon1, "")
        self.Tab2_ChangeKernel = QtWidgets.QWidget()
        self.Tab2_ChangeKernel.setObjectName("Tab2_ChangeKernel")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Tab2_ChangeKernel)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_ChangeFlavour = QtWidgets.QPushButton(self.Tab2_ChangeKernel)
        self.pushButton_ChangeFlavour.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_ChangeFlavour.setWhatsThis("")
        self.pushButton_ChangeFlavour.setObjectName("pushButton_ChangeFlavour")
        self.gridLayout_3.addWidget(self.pushButton_ChangeFlavour, 1, 0, 1, 1)
        self.comboBox_ChangeKernel = QtWidgets.QComboBox(self.Tab2_ChangeKernel)
        self.comboBox_ChangeKernel.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_ChangeKernel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_ChangeKernel.setObjectName("comboBox_ChangeKernel")
        self.gridLayout_3.addWidget(self.comboBox_ChangeKernel, 1, 2, 1, 1)
        self.text_Change_Kernel = QtWidgets.QTextBrowser(self.Tab2_ChangeKernel)
        self.text_Change_Kernel.setObjectName("text_Change_Kernel")
        self.gridLayout_3.addWidget(self.text_Change_Kernel, 0, 0, 1, 3)
        self.Tab1.addTab(self.Tab2_ChangeKernel, "")
        self.Tab3_DelKernel = QtWidgets.QWidget()
        self.Tab3_DelKernel.setObjectName("Tab3_DelKernel")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Tab3_DelKernel)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidget_Kernel = QtWidgets.QListWidget(self.Tab3_DelKernel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Kernel.sizePolicy().hasHeightForWidth())
        self.listWidget_Kernel.setSizePolicy(sizePolicy)
        self.listWidget_Kernel.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.listWidget_Kernel.setFont(font)
        self.listWidget_Kernel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_Kernel.setAutoFillBackground(False)
        self.listWidget_Kernel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_Kernel.setLineWidth(1)
        self.listWidget_Kernel.setMidLineWidth(0)
        self.listWidget_Kernel.setAutoScrollMargin(16)
        self.listWidget_Kernel.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget_Kernel.setIconSize(QtCore.QSize(0, 0))
        self.listWidget_Kernel.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidget_Kernel.setMovement(QtWidgets.QListView.Static)
        self.listWidget_Kernel.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget_Kernel.setProperty("isWrapping", False)
        self.listWidget_Kernel.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_Kernel.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_Kernel.setGridSize(QtCore.QSize(0, 22))
        self.listWidget_Kernel.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_Kernel.setModelColumn(0)
        self.listWidget_Kernel.setUniformItemSizes(False)
        self.listWidget_Kernel.setBatchSize(100)
        self.listWidget_Kernel.setObjectName("listWidget_Kernel")
        self.gridLayout_4.addWidget(self.listWidget_Kernel, 0, 0, 1, 3)
        self.pushButton_Clean = QtWidgets.QPushButton(self.Tab3_DelKernel)
        self.pushButton_Clean.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_Clean.setWhatsThis("")
        self.pushButton_Clean.setObjectName("pushButton_Clean")
        self.gridLayout_4.addWidget(self.pushButton_Clean, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 1, 1, 1)
        self.pushButton_DELK = QtWidgets.QPushButton(self.Tab3_DelKernel)
        self.pushButton_DELK.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_DELK.setWhatsThis("")
        self.pushButton_DELK.setObjectName("pushButton_DELK")
        self.gridLayout_4.addWidget(self.pushButton_DELK, 1, 2, 1, 1)
        self.listWidget_Kernel.raise_()
        self.pushButton_DELK.raise_()
        self.pushButton_Clean.raise_()
        self.Tab1.addTab(self.Tab3_DelKernel, "")
        self.Tab4_UpdateKernel = QtWidgets.QWidget()
        self.Tab4_UpdateKernel.setObjectName("Tab4_UpdateKernel")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Tab4_UpdateKernel)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.text_Update_kernel = QtWidgets.QTextBrowser(self.Tab4_UpdateKernel)
        self.text_Update_kernel.setObjectName("text_Update_kernel")
        self.gridLayout_5.addWidget(self.text_Update_kernel, 0, 0, 1, 3)
        self.pushButton_KERN = QtWidgets.QPushButton(self.Tab4_UpdateKernel)
        self.pushButton_KERN.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_KERN.setWhatsThis("")
        self.pushButton_KERN.setObjectName("pushButton_KERN")
        self.gridLayout_5.addWidget(self.pushButton_KERN, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 1, 1, 1, 1)
        self.pushButton_DISTR = QtWidgets.QPushButton(self.Tab4_UpdateKernel)
        self.pushButton_DISTR.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_DISTR.setMouseTracking(False)
        self.pushButton_DISTR.setTabletTracking(False)
        self.pushButton_DISTR.setWhatsThis("")
        self.pushButton_DISTR.setAccessibleName("")
        self.pushButton_DISTR.setAccessibleDescription("")
        self.pushButton_DISTR.setObjectName("pushButton_DISTR")
        self.gridLayout_5.addWidget(self.pushButton_DISTR, 1, 2, 1, 1)
        self.Tab1.addTab(self.Tab4_UpdateKernel, "")
        self.gridLayout.addWidget(self.Tab1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tab1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Управление ядрами"))
        self.text_Question.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Справка по программе.</span><br />Данная программа предоставляет средство простого графического управления скриптами: <span style=\" font-style:italic;\">update-kernel</span>, <span style=\" font-style:italic;\">remove-old-kernel</span>.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; background-color:transparent;\">Смена ядра.</span><span style=\" background-color:transparent;\"><br />Позволяет изменить тип ядра на выбор ( STD-DEF, UN-DEF, OLD-DEF ).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; background-color:transparent;\">Удаление ядер.</span><span style=\" background-color:transparent;\"><br />Показывает список установленных в системе ядер. Двойной клик на строку удаляет выбранное ядро и его модули.<br />Кнопка «Удалить ядра» очищает систему от всех старых версий ядер. Активное в данный момент ядро удалить нельзя.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; background-color:transparent;\">Обновить ядро.</span><span style=\" background-color:transparent;\"><br />Автоматически обновляет ядро и модули до самой новой версии. Кнопка «Дистрибутив» обновляет ПО до актуальной версии.</span></p></body></html>"))
        self.pushButton_ChangeFlavour.setToolTip(_translate("MainWindow", "Изменить тип flavour"))
        self.pushButton_ChangeFlavour.setText(_translate("MainWindow", "Изменить"))
        self.comboBox_ChangeKernel.setToolTip(_translate("MainWindow", "Выберите ядро из списка и нажмите кнопку<br>«Изменить» для перехода на новый flavour"))
        self.text_Change_Kernel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Заметка</span><br />Окно смены<span style=\" font-style:italic;\"> flavour\'s</span> ( типы сборки ) ядер операционной системы.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ядро: STD-DEF</span><br />Стандартное ядро. При сборке используются патчи из стабильной ветки ядер исправляющие работу д<span style=\" background-color:transparent;\">райверов и ПО.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ядро: OLD-DEF</span><br />Предыдущая ветка ядра std-def. Ядро old-def поддерживает более старое оборудование и длительную поддержку.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ядро: UN-DEF</span><br />Экспериментальное ядро для десктопов. Ядро un-def имеет более новую версию и может поддерживать оборудование которое не работает в <span style=\" font-style:italic;\">std-def</span>.</p></body></html>"))
        self.Tab1.setTabText(self.Tab1.indexOf(self.Tab2_ChangeKernel), _translate("MainWindow", "Смена ядра"))
        self.pushButton_Clean.setToolTip(_translate("MainWindow", "Очистка локального кэша"))
        self.pushButton_Clean.setText(_translate("MainWindow", "autoclean"))
        self.pushButton_DELK.setToolTip(_translate("MainWindow", "Удаляет старые версии ядер"))
        self.pushButton_DELK.setText(_translate("MainWindow", "Удалить ядра"))
        self.Tab1.setTabText(self.Tab1.indexOf(self.Tab3_DelKernel), _translate("MainWindow", "Удаление ядер"))
        self.text_Update_kernel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Заметка</span><br />Перед обновлением ядра рекомендуется обновить дистрибутив до последней версии. Такое обновление поможет избежать лишних проблем при обновлении ядра.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Кнопка «Обновить ядро»</span><br />Обновляет текущее активное ядро системы и все установленные для него модули.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Все действия программы будут выведены в терминал и требуют подтверждения пользователя. <span style=\" text-decoration: underline;\">Если Вы не уверены в своих действиях, отмените обновление.</span></p></body></html>"))
        self.pushButton_KERN.setToolTip(_translate("MainWindow", "Обновление ядра"))
        self.pushButton_KERN.setText(_translate("MainWindow", "Обновить ядро"))
        self.pushButton_DISTR.setToolTip(_translate("MainWindow", "Обновление дистрибутива"))
        self.pushButton_DISTR.setText(_translate("MainWindow", "Дистрибутив"))
        self.Tab1.setTabText(self.Tab1.indexOf(self.Tab4_UpdateKernel), _translate("MainWindow", "Обновить ядро"))

import resources
