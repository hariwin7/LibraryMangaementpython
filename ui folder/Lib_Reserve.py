# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Reserve.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.Reserve_txt = QtGui.QLineEdit(self.centralwidget)
        self.Reserve_txt.setObjectName(_fromUtf8("Reserve_txt"))
        self.horizontalLayout.addWidget(self.Reserve_txt)
        self.Reserve_btn = QtGui.QPushButton(self.centralwidget)
        self.Reserve_btn.setObjectName(_fromUtf8("Reserve_btn"))
        self.horizontalLayout.addWidget(self.Reserve_btn)
        self.Reserve_clr_btn = QtGui.QPushButton(self.centralwidget)
        self.Reserve_clr_btn.setObjectName(_fromUtf8("Reserve_clr_btn"))
        self.horizontalLayout.addWidget(self.Reserve_clr_btn)
        self.Reserve_cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Reserve_cancel_btn.setObjectName(_fromUtf8("Reserve_cancel_btn"))
        self.horizontalLayout.addWidget(self.Reserve_cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.Reserve_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Reserve_txt.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Book Id:", None))
        self.Reserve_btn.setText(_translate("MainWindow", "Reserve", None))
        self.Reserve_clr_btn.setText(_translate("MainWindow", "Clear", None))
        self.Reserve_cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))

