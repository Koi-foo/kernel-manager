# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoProcessWin(object):
    def setupUi(self, InfoProcessWin):
        InfoProcessWin.setObjectName("InfoProcessWin")
        InfoProcessWin.resize(550, 580)
        InfoProcessWin.setMinimumSize(QtCore.QSize(550, 580))
        font = QtGui.QFont()
        font.setPointSize(10)
        InfoProcessWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/icons/kernel-manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InfoProcessWin.setWindowIcon(icon)
        InfoProcessWin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(InfoProcessWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 3)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Cancel.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout_2.addWidget(self.pushButton_Cancel, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_Ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Ok.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_Ok.setObjectName("pushButton_Ok")
        self.gridLayout_2.addWidget(self.pushButton_Ok, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        InfoProcessWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InfoProcessWin)
        self.statusbar.setObjectName("statusbar")
        InfoProcessWin.setStatusBar(self.statusbar)

        self.retranslateUi(InfoProcessWin)
        QtCore.QMetaObject.connectSlotsByName(InfoProcessWin)

    def retranslateUi(self, InfoProcessWin):
        _translate = QtCore.QCoreApplication.translate
        InfoProcessWin.setWindowTitle(_translate("InfoProcessWin", _("Information")))
        self.groupBox.setTitle(_translate("InfoProcessWin", _("Task progress")))
        self.pushButton_Cancel.setToolTip(_translate("InfoProcessWin", _("Stop the process")))
        self.pushButton_Cancel.setText(_translate("InfoProcessWin", _("Cancel")))
        self.pushButton_Ok.setToolTip(_translate("InfoProcessWin", _("Agree to continue the process")))
        self.pushButton_Ok.setText(_translate("InfoProcessWin", _("Confirm")))
import resources
