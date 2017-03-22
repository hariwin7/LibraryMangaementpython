# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_createuser.ui'
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

class Createuser(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = Lib_DB.Database()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Newusr_name_txt = QtGui.QLineEdit(self.centralwidget)
        self.Newusr_name_txt.setObjectName(_fromUtf8("Newusr_name_txt"))
        self.verticalLayout_2.addWidget(self.Newusr_name_txt)
        self.Newusr_depart_txt = QtGui.QLineEdit(self.centralwidget)
        self.Newusr_depart_txt.setObjectName(_fromUtf8("Newusr_depart_txt"))
        self.verticalLayout_2.addWidget(self.Newusr_depart_txt)
        self.Newusr_usr_id_txt = QtGui.QLineEdit(self.centralwidget)
        self.Newusr_usr_id_txt.setObjectName(_fromUtf8("Newusr_usr_id_txt"))
        self.verticalLayout_2.addWidget(self.Newusr_usr_id_txt)
        self.Newusr_desig_txt = QtGui.QLineEdit(self.centralwidget)
        self.Newusr_desig_txt.setObjectName(_fromUtf8("Newusr_desig_txt"))
        self.verticalLayout_2.addWidget(self.Newusr_desig_txt)
        self.Newusr_contact_txt = QtGui.QLineEdit(self.centralwidget)
        self.Newusr_contact_txt.setObjectName(_fromUtf8("Newusr_contact_txt"))
        self.verticalLayout_2.addWidget(self.Newusr_contact_txt)
        self.Password_txt = QtGui.QLineEdit(self.centralwidget)
        self.Password_txt.setObjectName(_fromUtf8("Password_txt"))
        self.Password_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.Password_txt)
        self.Repassword_txt = QtGui.QLineEdit(self.centralwidget)
        self.Repassword_txt.setObjectName(_fromUtf8("Repassword_txt"))
        self.Repassword_txt.setEchoMode(QtGui.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.Repassword_txt)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Newusr_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Newusr_add_btn.setObjectName(_fromUtf8("Newusr_add_btn"))
        self.horizontalLayout_2.addWidget(self.Newusr_add_btn)
        self.Newusr_clr_btn = QtGui.QPushButton(self.centralwidget)
        self.Newusr_clr_btn.setObjectName(_fromUtf8("Newusr_clr_btn"))
        self.horizontalLayout_2.addWidget(self.Newusr_clr_btn)
        self.Newusr_cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Newusr_cancel_btn.setObjectName(_fromUtf8("Newusr_cancel_btn"))
        self.horizontalLayout_2.addWidget(self.Newusr_cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
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
        QtCore.QObject.connect(self.Newusr_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Newusr_name_txt.clear)
        QtCore.QObject.connect(self.Newusr_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Newusr_depart_txt.clear)
        QtCore.QObject.connect(self.Newusr_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Newusr_usr_id_txt.clear)
        QtCore.QObject.connect(self.Newusr_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Newusr_contact_txt.clear)
        QtCore.QObject.connect(self.Newusr_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Password_txt.clear)
        QtCore.QObject.connect(self.Newusr_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Repassword_txt.clear)
        QtCore.QObject.connect(self.Newusr_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Newusr_desig_txt.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "User Details", None))
        self.label.setText(_translate("MainWindow", "Name:", None))
        self.label_2.setText(_translate("MainWindow", "Department:", None))
        self.label_3.setText(_translate("MainWindow", "User Id:", None))
        self.label_8.setText(_translate("MainWindow", "Designation:", None))
        self.label_4.setText(_translate("MainWindow", "Contact info:", None))
        self.label_6.setText(_translate("MainWindow", "Password:", None))
        self.label_7.setText(_translate("MainWindow", "Re enter password:", None))
        self.Newusr_add_btn.setText(_translate("MainWindow", "Add", None))
        self.Newusr_clr_btn.setText(_translate("MainWindow", "Clear", None))
        self.Newusr_cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.Newusr_add_btn.clicked.connect(self.CreateUser)
        self.Newusr_cancel_btn.clicked.connect(self.hideit)

    def CreateUser(self):
        name = self.Newusr_name_txt.text()
        userid = self.Newusr_usr_id_txt.text()
        usercontact = self.Newusr_contact_txt.text()
        department = self.Newusr_depart_txt.text()
        designation = self.Newusr_desig_txt.text()
        passwd = self.Password_txt.text()
        repasswd =self.Repassword_txt.text()
        if(not name):
            QtGui.QMessageBox.information(self,'Message','Name Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not department):
            QtGui.QMessageBox.information(self,'Message','Department Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not userid):
            QtGui.QMessageBox.information(self,'Message','User Id cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not designation):
            QtGui.QMessageBox.information(self,'Message','Designation cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not usercontact):
            QtGui.QMessageBox.information(self,'Message','Contact information Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not passwd):
            QtGui.QMessageBox.information(self,'Message','Password Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not repasswd):
            QtGui.QMessageBox.information(self,'Message','Please Re Enter Password',QtGui.QMessageBox.Ok)
        else:
            if(passwd == repasswd):
                err = self.db.AddEntryToUserTable(name,department,userid,designation,usercontact)
                if(err == 1062):
                    QtGui.QMessageBox.information(self,'Message','Duplicate User Id Please Re Enter',QtGui.QMessageBox.Ok)
                else:
                    self.db.AddEntryToUPassword(userid,passwd)
                    self.db.comm()
                    QtGui.QMessageBox.information(self,'Message','Added Details Successfully',QtGui.QMessageBox.Ok)          
                
            else:
                QtGui.QMessageBox.information(self,'Message','Password\'s Does\'nt Match Please Re Enter',QtGui.QMessageBox.Ok)
    def hideit(self):
        self.hide()

    def keyPressEvent(self, event):
        k = event.key()
        if k == QtCore.Qt.Key_Return:
            self.CreateUser()         
       
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Createuser()
    ex.show()
    sys.exit(app.exec())
