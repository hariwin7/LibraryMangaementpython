# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Lib_Adm import*
from Lib_Usr import*
import Lib_DB
import sys

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

class Login(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(297, 213)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.Adm_usr_txt = QtGui.QLineEdit(self.tab)
        self.Adm_usr_txt.setObjectName(_fromUtf8("Adm_usr_txt"))
        self.gridLayout.addWidget(self.Adm_usr_txt, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.Adm_pass_txt = QtGui.QLineEdit(self.tab)
        self.Adm_pass_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.Adm_pass_txt.setObjectName(_fromUtf8("Adm_pass_txt"))
        self.gridLayout.addWidget(self.Adm_pass_txt, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Adm_ok_btn = QtGui.QPushButton(self.tab)
        self.Adm_ok_btn.setObjectName(_fromUtf8("Adm_ok_btn"))
        self.horizontalLayout_3.addWidget(self.Adm_ok_btn)
        self.Adm_cancel_btn = QtGui.QPushButton(self.tab)
        self.Adm_cancel_btn.setObjectName(_fromUtf8("Adm_cancel_btn"))
        self.horizontalLayout_3.addWidget(self.Adm_cancel_btn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.Usr_usr_txt = QtGui.QLineEdit(self.tab_2)
        self.Usr_usr_txt.setObjectName(_fromUtf8("Usr_usr_txt"))
        self.gridLayout_2.addWidget(self.Usr_usr_txt, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.Usr_pass_txt = QtGui.QLineEdit(self.tab_2)
        self.Usr_pass_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.Usr_pass_txt.setObjectName(_fromUtf8("Usr_pass_txt"))
        self.gridLayout_2.addWidget(self.Usr_pass_txt, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Usr_ok_btn = QtGui.QPushButton(self.tab_2)
        self.Usr_ok_btn.setObjectName(_fromUtf8("Usr_ok_btn"))
        self.horizontalLayout_2.addWidget(self.Usr_ok_btn)
        self.Usr_cancel_btn = QtGui.QPushButton(self.tab_2)
        self.Usr_cancel_btn.setObjectName(_fromUtf8("Usr_cancel_btn"))
        self.horizontalLayout_2.addWidget(self.Usr_cancel_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 297, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Username:", None))
        self.label_4.setText(_translate("MainWindow", "Password :", None))
        self.Adm_ok_btn.setText(_translate("MainWindow", "ok", None))
        self.Adm_cancel_btn.setText(_translate("MainWindow", "cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Administrator login", None))
        self.label.setText(_translate("MainWindow", "Username:", None))
        self.label_2.setText(_translate("MainWindow", "Password :", None))
        self.Usr_ok_btn.setText(_translate("MainWindow", "ok", None))
        self.Usr_cancel_btn.setText(_translate("MainWindow", "cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "User login", None))
        self.Adm_ok_btn.clicked.connect(self.Admlogin)
        self.Usr_ok_btn.clicked.connect(self.Usrlogin)
        

    # My code
    def Admlogin(self):
        self.adm_passwd = self.Adm_pass_txt.text()
        self.adm_username = self.Adm_usr_txt.text()
        if(not self.adm_passwd or not self.adm_username):
            eply = QtGui.QMessageBox.information(self, 'Message',
            "Username Or Password Cannot Be Blank", QtGui.QMessageBox.Ok)
        else:
            if(self.adm_username == "admin@jk" and self.adm_passwd == "password"):
                QtGui.QMessageBox.information(self,'Message','successfully logged in',QtGui.QMessageBox.Ok)
                self.showadm()
                self.hide()

            else:
                QtGui.QMessageBox.information(self,'Message','Username Or Password Wrong',QtGui.QMessageBox.Ok)

    def Usrlogin(self):
        self.usr_passwd = self.Usr_pass_txt.text()
        self.usr_username = self.Usr_usr_txt.text()
        if(not self.usr_passwd or not self.usr_username):
            QtGui.QMessageBox.information(self, 'Message',"Username Or Password Cannot Be Blank", QtGui.QMessageBox.Ok)
        else:
            self.usr_username = "\'%" + self.usr_username + "%\'"
            self.db = Lib_DB.Database()
            passwd = self.db.GetUserPassword(self.usr_username)
            if(not passwd):
                QtGui.QMessageBox.information(self,'Message','Username Or Password Wrong',QtGui.QMessageBox.Ok)
            else:
                print(passwd)
                if(self.usr_passwd == passwd[0][2]):
                    QtGui.QMessageBox.information(self,'Message','successfully logged in',QtGui.QMessageBox.Ok)
                    self.showuser()             
                else:
                    QtGui.QMessageBox.information(self,'Message','Username Or Password Wrong',QtGui.QMessageBox.Ok)


    def showadm(self):
        self.sub = Adm()
        self.sub.show()


    def showuser(self):
        self.username = self.Usr_usr_txt.text()
        self.username = "\'" + self.username + "\'"
        self.sub = Usr()
        self.sub.GetUser(self.username)
        self.sub.Settree(self.username)
        self.sub.show()
    def keyPressEvent(self, event):
        k = event.key()
        if k == QtCore.Qt.Key_Return:
            if self.tabWidget.currentIndex()==1:
                self.Usrlogin()
            else:
                self.Admlogin()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())
