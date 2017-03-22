# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Deleteuser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import Lib_DB
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

class Deleteuser(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.Delete_id_txt = QtGui.QLineEdit(self.centralwidget)
        self.Delete_id_txt.setObjectName(_fromUtf8("Delete_id_txt"))
        self.horizontalLayout.addWidget(self.Delete_id_txt)
        self.Delete_btn = QtGui.QPushButton(self.centralwidget)
        self.Delete_btn.setObjectName(_fromUtf8("Delete_btn"))
        self.horizontalLayout.addWidget(self.Delete_btn)
        self.Delete_clr_btn = QtGui.QPushButton(self.centralwidget)
        self.Delete_clr_btn.setObjectName(_fromUtf8("Delete_clr_btn"))
        self.horizontalLayout.addWidget(self.Delete_clr_btn)
        self.Delete_cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Delete_cancel_btn.setObjectName(_fromUtf8("Delete_cancel_btn"))
        self.horizontalLayout.addWidget(self.Delete_cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
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
        QtCore.QObject.connect(self.Delete_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Delete_id_txt.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "User Id:", None))
        self.Delete_btn.setText(_translate("MainWindow", "Delete", None))
        self.Delete_clr_btn.setText(_translate("MainWindow", "Clear", None))
        self.Delete_cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.Delete_btn.clicked.connect(self.Delete)
        self.Delete_cancel_btn.clicked.connect(self.hideit)

    def Delete(self):
        self.db = Lib_DB.Database()
        self.delid = self.Delete_id_txt.text()
        self.delid = "\'" + self.delid + "\'"
        answer = self.db.GetUser("UserTable",self.delid)
        if(not answer):
            QtGui.QMessageBox.information(self,'Message','Invalid User Id',QtGui.QMessageBox.Ok)
        else:
            self.db.DeleteUser(self.delid)
            self.db.DeleteUserinall("Issue","UserId",self.delid)
            self.db.DeleteUserinall("Userpassword","Username",self.delid)
            QtGui.QMessageBox.information(self,'Message','User Deleted Successfully',QtGui.QMessageBox.Ok)
            self.db.comm()

    def hideit(self):
        self.hide()
    def keyPressEvent(self, event):
        k = event.key()
        if k == QtCore.Qt.Key_Return:
            self.Delete()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Deleteuser()
    ex.show()
    sys.exit(app.exec())