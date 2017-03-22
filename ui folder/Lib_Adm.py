# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Adm.ui'
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
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 370, 311, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuUpdate_Book = QtGui.QMenu(self.menubar)
        self.menuUpdate_Book.setObjectName(_fromUtf8("menuUpdate_Book"))
        self.menuIssue_Return = QtGui.QMenu(self.menubar)
        self.menuIssue_Return.setObjectName(_fromUtf8("menuIssue_Return"))
        self.menuNew_User = QtGui.QMenu(self.menubar)
        self.menuNew_User.setObjectName(_fromUtf8("menuNew_User"))
        self.menuSearch = QtGui.QMenu(self.menubar)
        self.menuSearch.setObjectName(_fromUtf8("menuSearch"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionNew_Book_Entry = QtGui.QAction(MainWindow)
        self.actionNew_Book_Entry.setObjectName(_fromUtf8("actionNew_Book_Entry"))
        self.actionIssue_Book = QtGui.QAction(MainWindow)
        self.actionIssue_Book.setObjectName(_fromUtf8("actionIssue_Book"))
        self.actionReturn_Book = QtGui.QAction(MainWindow)
        self.actionReturn_Book.setObjectName(_fromUtf8("actionReturn_Book"))
        self.actionCreate_New_User = QtGui.QAction(MainWindow)
        self.actionCreate_New_User.setObjectName(_fromUtf8("actionCreate_New_User"))
        self.actionDelete_User = QtGui.QAction(MainWindow)
        self.actionDelete_User.setObjectName(_fromUtf8("actionDelete_User"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionContact = QtGui.QAction(MainWindow)
        self.actionContact.setObjectName(_fromUtf8("actionContact"))
        self.actionAdvanced_Search = QtGui.QAction(MainWindow)
        self.actionAdvanced_Search.setObjectName(_fromUtf8("actionAdvanced_Search"))
        self.menuFile.addAction(self.actionClose)
        self.menuUpdate_Book.addAction(self.actionNew_Book_Entry)
        self.menuIssue_Return.addAction(self.actionIssue_Book)
        self.menuIssue_Return.addSeparator()
        self.menuIssue_Return.addAction(self.actionReturn_Book)
        self.menuNew_User.addAction(self.actionCreate_New_User)
        self.menuNew_User.addAction(self.actionDelete_User)
        self.menuSearch.addAction(self.actionAdvanced_Search)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionContact)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuUpdate_Book.menuAction())
        self.menubar.addAction(self.menuIssue_Return.menuAction())
        self.menubar.addAction(self.menuNew_User.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Administrator Window", None))
        self.label.setText(_translate("MainWindow", "Library Management Software Version 1.0", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuUpdate_Book.setTitle(_translate("MainWindow", "Add New Book", None))
        self.menuIssue_Return.setTitle(_translate("MainWindow", "Issue & Return", None))
        self.menuNew_User.setTitle(_translate("MainWindow", "New User", None))
        self.menuSearch.setTitle(_translate("MainWindow", "Search", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionNew_Book_Entry.setText(_translate("MainWindow", "New Book Entry", None))
        self.actionIssue_Book.setText(_translate("MainWindow", "Issue Book", None))
        self.actionReturn_Book.setText(_translate("MainWindow", "Return Book", None))
        self.actionCreate_New_User.setText(_translate("MainWindow", "Create New User", None))
        self.actionDelete_User.setText(_translate("MainWindow", "Delete User", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionContact.setText(_translate("MainWindow", "Contact", None))
        self.actionAdvanced_Search.setText(_translate("MainWindow", "Advanced Search", None))

