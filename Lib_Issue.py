# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Issue.ui'
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

class Issue(QtGui.QMainWindow):
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
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Issue_usrid_txt = QtGui.QLineEdit(self.centralwidget)
        self.Issue_usrid_txt.setObjectName(_fromUtf8("Issue_usrid_txt"))
        self.verticalLayout_2.addWidget(self.Issue_usrid_txt)
        self.Issue_bid_txt = QtGui.QLineEdit(self.centralwidget)
        self.Issue_bid_txt.setObjectName(_fromUtf8("Issue_bid_txt"))
        self.verticalLayout_2.addWidget(self.Issue_bid_txt)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Issue_issue_btn = QtGui.QPushButton(self.centralwidget)
        self.Issue_issue_btn.setObjectName(_fromUtf8("Issue_issue_btn"))
        self.horizontalLayout_2.addWidget(self.Issue_issue_btn)
        self.Issue_clr_btn = QtGui.QPushButton(self.centralwidget)
        self.Issue_clr_btn.setObjectName(_fromUtf8("Issue_clr_btn"))
        self.horizontalLayout_2.addWidget(self.Issue_clr_btn)
        self.Issue_cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Issue_cancel_btn.setObjectName(_fromUtf8("Issue_cancel_btn"))
        self.horizontalLayout_2.addWidget(self.Issue_cancel_btn)
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
        QtCore.QObject.connect(self.Issue_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Issue_usrid_txt.clear)
        QtCore.QObject.connect(self.Issue_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Issue_bid_txt.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Book Details:", None))
        self.label_2.setText(_translate("MainWindow", "User Id:", None))
        self.label.setText(_translate("MainWindow", "Book Id:", None))
        self.Issue_issue_btn.setText(_translate("MainWindow", "Issue", None))
        self.Issue_clr_btn.setText(_translate("MainWindow", "Clear", None))
        self.Issue_cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.Issue_issue_btn.clicked.connect(self.IssueBook)
        self.Issue_cancel_btn.clicked.connect(self.hideit)

    def IssueBook(self):
        bookid = self.Issue_bid_txt.text()
        userid = self.Issue_usrid_txt.text()
        table = self.db.GetUser("UserTable",("\'"+userid+"\'"))
        book = self.db.Search("BookId",bookid)
        if not table:
            QtGui.QMessageBox.information(self,'Message','Invalid User Id Please Re Enter',QtGui.QMessageBox.Ok)
        elif not book:
            QtGui.QMessageBox.information(self,'Message','Invalid Book Id Please Re Enter',QtGui.QMessageBox.Ok)
        else:
            err = self.db.AddEntryToIssueTable(bookid,userid)
            if(err == 1062):
                QtGui.QMessageBox.information(self,'Message','Duplicate Book Id Please Re Enter',QtGui.QMessageBox.Ok)
            else:
                self.db.Update(bookid,"'Issued'")
                self.db.comm()
                QtGui.QMessageBox.information(self,'Message','Book Entry Successfull',QtGui.QMessageBox.Ok)
    def hideit(self):
        self.hide()
    def keyPressEvent(self, event):
        k = event.key()
        if k == QtCore.Qt.Key_Return:
            self.IssueBook()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Issue()
    ex.show()
    sys.exit(app.exec())