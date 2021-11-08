# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tray_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrayWindow(object):
    def setupUi(self, TrayWindow):
        TrayWindow.setObjectName("TrayWindow")
        TrayWindow.resize(618, 364)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/icons/kernel-manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TrayWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TrayWindow)
        self.centralwidget.setObjectName("centralwidget")
        TrayWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TrayWindow)
        self.statusbar.setObjectName("statusbar")
        TrayWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TrayWindow)
        QtCore.QMetaObject.connectSlotsByName(TrayWindow)

    def retranslateUi(self, TrayWindow):
        _translate = QtCore.QCoreApplication.translate
        TrayWindow.setWindowTitle(_translate("TrayWindow", "Kernel Management: Configuring Notifications"))
import resources
