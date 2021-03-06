# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 465)
        MainWindow.setMinimumSize(QtCore.QSize(700, 465))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/icons/kernel-manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Tab1 = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.Tab1.setFont(font)
        self.Tab1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Tab1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Tab1.setStyleSheet("")
        self.Tab1.setIconSize(QtCore.QSize(16, 16))
        self.Tab1.setObjectName("Tab1")
        self.Tab1_Question = QtWidgets.QWidget()
        self.Tab1_Question.setObjectName("Tab1_Question")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Tab1_Question)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_Question = QtWidgets.QTextBrowser(self.Tab1_Question)
        self.text_Question.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
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
        self.text_Change_Kernel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
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
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.listWidget_Kernel.setFont(font)
        self.listWidget_Kernel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listWidget_Kernel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_Kernel.setAutoFillBackground(False)
        self.listWidget_Kernel.setStyleSheet("QListWidget:item{height: 30px;border-bottom: 1px solid rgb(225, 225, 225);} QListWidget::item:selected {background-color: rgb(231, 242, 249); color: black} QListView::item:selected:!active {background-color: rgb(231, 242, 249); color: black} QListView::item:selected:active {background-color: rgb(231, 242, 249); color: black} QListView::item:hover {background-color: rgb(231, 242, 249); color: black}")
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
        self.listWidget_Kernel.setGridSize(QtCore.QSize(0, 31))
        self.listWidget_Kernel.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_Kernel.setModelColumn(0)
        self.listWidget_Kernel.setUniformItemSizes(False)
        self.listWidget_Kernel.setBatchSize(100)
        self.listWidget_Kernel.setObjectName("listWidget_Kernel")
        self.gridLayout_4.addWidget(self.listWidget_Kernel, 0, 0, 1, 3)
        self.textBrowser = QtWidgets.QTextBrowser(self.Tab3_DelKernel)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 1, 0, 1, 3)
        self.pushButton_Clean = QtWidgets.QPushButton(self.Tab3_DelKernel)
        self.pushButton_Clean.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_Clean.setWhatsThis("")
        self.pushButton_Clean.setObjectName("pushButton_Clean")
        self.gridLayout_4.addWidget(self.pushButton_Clean, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 1, 1, 1)
        self.pushButton_DELK = QtWidgets.QPushButton(self.Tab3_DelKernel)
        self.pushButton_DELK.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_DELK.setWhatsThis("")
        self.pushButton_DELK.setObjectName("pushButton_DELK")
        self.gridLayout_4.addWidget(self.pushButton_DELK, 2, 2, 1, 1)
        self.listWidget_Kernel.raise_()
        self.pushButton_DELK.raise_()
        self.pushButton_Clean.raise_()
        self.textBrowser.raise_()
        self.Tab1.addTab(self.Tab3_DelKernel, "")
        self.Tab4_UpdateKernel = QtWidgets.QWidget()
        self.Tab4_UpdateKernel.setObjectName("Tab4_UpdateKernel")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Tab4_UpdateKernel)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_KERN = QtWidgets.QPushButton(self.Tab4_UpdateKernel)
        self.pushButton_KERN.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_KERN.setWhatsThis("")
        self.pushButton_KERN.setObjectName("pushButton_KERN")
        self.gridLayout_5.addWidget(self.pushButton_KERN, 1, 0, 1, 1)
        self.text_Update_kernel = QtWidgets.QTextBrowser(self.Tab4_UpdateKernel)
        self.text_Update_kernel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.text_Update_kernel.setOpenExternalLinks(True)
        self.text_Update_kernel.setObjectName("text_Update_kernel")
        self.gridLayout_5.addWidget(self.text_Update_kernel, 0, 0, 1, 4)
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
        self.gridLayout_5.addWidget(self.pushButton_DISTR, 1, 3, 1, 1)
        self.comboBox_ChangeRepo = QtWidgets.QComboBox(self.Tab4_UpdateKernel)
        self.comboBox_ChangeRepo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_ChangeRepo.setObjectName("comboBox_ChangeRepo")
        self.gridLayout_5.addWidget(self.comboBox_ChangeRepo, 1, 2, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", _("Kernels management")))
        self.text_Question.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Program help.</span><br />This program provides a simple graphical script management tool: <span style=\" font-style:italic;\">update-kernel</span>, <span style=\" font-style:italic;\">remove-old-kernel</span>.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; background-color:transparent;\">Change of kernel.</span><span style=\" background-color:transparent;\"><br />Allows you to change the kernel type to choose from ( STD-DEF, UN-DEF, OLD-DEF ).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; background-color:transparent;\">Removing kernels.</span><span style=\" background-color:transparent;\"><br />Shows a list of kernels installed on the system. Double clicking on a line removes the selected kernel and its modules. The currently active core is not displayed in the list. The Clear button clears the cache of obsolete packages and removes duplicates.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:transparent;\">The Remove Kernels button clears the system of all kernels except the current one. The currently active core cannot be removed.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; background-color:transparent;\">Update kernel.</span><span style=\" background-color:transparent;\"><br />Automatically updates the kernel and modules to the newest version. The &quot;Distribution&quot; button updates the software to the current version. The repository list allows you to modify the branches of the repository.</span></p></body></html>")))
        self.pushButton_ChangeFlavour.setToolTip(_translate("MainWindow", _("Change flavor type")))
        self.pushButton_ChangeFlavour.setText(_translate("MainWindow", _("Change")))
        self.comboBox_ChangeKernel.setToolTip(_translate("MainWindow", _("Select a kernel from the list and click the <br>\"Change\" button to switch to a new flavor")))
        self.text_Change_Kernel.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">The note</span><br />The tab for changing the flavour\'s (assembly types) of the operating system kernels.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Kernel: STD-DEF</span><br />Standard kernel. During the assembly, patches from the stable kernel branch are used to correct the work of drivers and software.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Kernel: OLD-DEF</span><br />Previous kernel branch std-def. The old-def kernel supports older hardware and long-term support.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Kernel: UN-DEF</span><br />An experimental core for desktops. The un-def kernel is newer and may support hardware that does not work in std-def.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Sisyphus: UN-DEF </span><br />It is an unstable repository of the latest software. Recommended for Intel integrated graphics not supported by other kernels. When using the kernel from this repository, you will not be able to work with programs that depend on the version of the module in the stable repositories.</p></body></html>")))
        self.Tab1.setTabText(self.Tab1.indexOf(self.Tab2_ChangeKernel), _translate("MainWindow", _("Change of kernels")))
        self.listWidget_Kernel.setSortingEnabled(False)
        self.textBrowser.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">The note</span><br />The right mouse button menu provides additional options such as loading the default kernel. For the convenience of orientation, color coding has been introduced.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Color coding.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/icons/std.png\" height=\"12\" /> - kernel type ( std-def ) <img src=\":/picture/icons/un.png\" height=\"12\" /> - kernel type ( un-def ) <img src=\":/picture/icons/old.png\" height=\"12\" /> - kernel type ( old-def )</p></body></html>")))
        self.pushButton_Clean.setToolTip(_translate("MainWindow", _("Clearing the local cache of obsolete packages<br>and removing duplicate packages")))
        self.pushButton_Clean.setText(_translate("MainWindow", _("Clear")))
        self.pushButton_DELK.setToolTip(_translate("MainWindow", _("Removes all cores except the currently active one")))
        self.pushButton_DELK.setText(_translate("MainWindow", _("Remove kernels")))
        self.Tab1.setTabText(self.Tab1.indexOf(self.Tab3_DelKernel), _translate("MainWindow", _("Removing kernels")))
        self.pushButton_KERN.setToolTip(_translate("MainWindow", _("Kernel update")))
        self.pushButton_KERN.setText(_translate("MainWindow", _("Update kernel")))
        self.text_Update_kernel.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">The note</span><br />It is recommended to update the distribution to the latest version before updating the kernel. Such an update will help to avoid unnecessary problems when updating the kernel.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Update Kernel button</span><br />Updates the current active system kernel and all modules installed for it.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All actions of the program will be displayed in the terminal and require user confirmation. If you are unsure of your actions, cancel the update.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Repositories</span><br />Allows changing repositories. Shows the currently connected repositories. Allows you to update the OS platform. To switch to a different platform, select a repository and click &quot;Distribution&quot;. The update will start automatically. Before choosing &quot;<a href=\"https://www.altlinux.org/%D0%A7%D1%82%D0%BE_%D1%82%D0%B0%D0%BA%D0%BE%D0%B5_Sisyphus%3F\"><span style=\" text-decoration: underline; color:#2980b9;\">Sisyphus</span></a>&quot;, carefully read its description.</p></body></html>")))
        self.pushButton_DISTR.setToolTip(_translate("MainWindow", _("Distribution update")))
        self.pushButton_DISTR.setText(_translate("MainWindow", _("Distribution")))
        self.comboBox_ChangeRepo.setToolTip(_translate("MainWindow", _("Change repository")))
        self.Tab1.setTabText(self.Tab1.indexOf(self.Tab4_UpdateKernel), _translate("MainWindow", _("Update kernel")))
import resources
