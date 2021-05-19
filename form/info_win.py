# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogInfo(object):
    def setupUi(self, DialogInfo):
        DialogInfo.setObjectName("DialogInfo")
        DialogInfo.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogInfo.resize(650, 380)
        DialogInfo.setMinimumSize(QtCore.QSize(650, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/icons/kernel-manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogInfo.setWindowIcon(icon)
        DialogInfo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        DialogInfo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gridLayout = QtWidgets.QGridLayout(DialogInfo)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_Info = QtWidgets.QTextEdit(DialogInfo)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.textEdit_Info.setFont(font)
        self.textEdit_Info.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit_Info.setReadOnly(True)
        self.textEdit_Info.setObjectName("textEdit_Info")
        self.gridLayout.addWidget(self.textEdit_Info, 0, 0, 1, 1)

        self.retranslateUi(DialogInfo)
        QtCore.QMetaObject.connectSlotsByName(DialogInfo)

    def retranslateUi(self, DialogInfo):
        _translate = QtCore.QCoreApplication.translate
        DialogInfo.setWindowTitle(_translate("DialogInfo", _("Information")))
        self.textEdit_Info.setHtml(_translate("DialogInfo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
import resources
