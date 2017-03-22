# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Return.ui'
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

class Return(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = Lib_DB.Database()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.Return_bid_txt = QtGui.QLineEdit(self.centralwidget)
        self.Return_bid_txt.setObjectName(_fromUtf8("Return_bid_txt"))
        self.horizontalLayout.addWidget(self.Return_bid_txt)
        self.Return_return_btn = QtGui.QPushButton(self.centralwidget)
        self.Return_return_btn.setObjectName(_fromUtf8("Return_return_btn"))
        self.horizontalLayout.addWidget(self.Return_return_btn)
        self.Return_clr_btn = QtGui.QPushButton(self.centralwidget)
        self.Return_clr_btn.setObjectName(_fromUtf8("Return_clr_btn"))
        self.horizontalLayout.addWidget(self.Return_clr_btn)
        self.Return_cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Return_cancel_btn.setObjectName(_fromUtf8("Return_cancel_btn"))
        self.horizontalLayout.addWidget(self.Return_cancel_btn)
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
        QtCore.QObject.connect(self.Return_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Return_bid_txt.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Return Book Details", None))
        self.label.setText(_translate("MainWindow", "Book Id:", None))
        self.Return_return_btn.setText(_translate("MainWindow", "Return", None))
        self.Return_clr_btn.setText(_translate("MainWindow", "Clear", None))
        self.Return_cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.Return_return_btn.clicked.connect(self.Return)
        self.Return_cancel_btn.clicked.connect(self.hideit)

    def Return(self):
        bookid =  self.Return_bid_txt.text()
        if not bookid:
            QtGui.QMessageBox.information(self,"Message","Book Id Cannot Be Blank",QtGui.QMessageBox.Ok)
        else:
            bookid = "\'" + bookid + "\'"
            book = self.db.GetIssue("Issue",bookid)
            if book:
                self.db.Delete(bookid)
                self.db.Update(bookid,"'Available'")
                self.db.comm()
            else:
                QtGui.QMessageBox.information(self,'Message','Book Not Issued\n Or \n Invalid Book Id',QtGui.QMessageBox.Ok)

    def hideit(self):
        self.hide()

    def keyPressEvent(self, event):
        k = event.key()
        if k == QtCore.Qt.Key_Return:
            self.Return()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Return()
    ex.show()
    sys.exit(app.exec())