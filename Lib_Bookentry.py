# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Bookentry.ui'
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

class Bookentry(QtGui.QMainWindow):
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
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
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
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Bentry_Bnme_txt = QtGui.QLineEdit(self.centralwidget)
        self.Bentry_Bnme_txt.setObjectName(_fromUtf8("Bentry_Bnme_txt"))
        self.verticalLayout_2.addWidget(self.Bentry_Bnme_txt)
        self.Bentry_bid_txt = QtGui.QLineEdit(self.centralwidget)
        self.Bentry_bid_txt.setObjectName(_fromUtf8("Bentry_bid_txt"))
        self.verticalLayout_2.addWidget(self.Bentry_bid_txt)
        self.Bentry_author_txt = QtGui.QLineEdit(self.centralwidget)
        self.Bentry_author_txt.setObjectName(_fromUtf8("Bentry_author_txt"))
        self.verticalLayout_2.addWidget(self.Bentry_author_txt)
        self.bentry_isbn_txt = QtGui.QLineEdit(self.centralwidget)
        self.bentry_isbn_txt.setObjectName(_fromUtf8("bentry_isbn_txt"))
        self.verticalLayout_2.addWidget(self.bentry_isbn_txt)
        self.Bentryt_publisher_txt = QtGui.QLineEdit(self.centralwidget)
        self.Bentryt_publisher_txt.setObjectName(_fromUtf8("Bentryt_publisher_txt"))
        self.verticalLayout_2.addWidget(self.Bentryt_publisher_txt)
        self.Bentry_genre_txt = QtGui.QLineEdit(self.centralwidget)
        self.Bentry_genre_txt.setObjectName(_fromUtf8("Bentry_genre_txt"))
        self.verticalLayout_2.addWidget(self.Bentry_genre_txt)
        self.Bentry_sem_txt = QtGui.QLineEdit(self.centralwidget)
        self.Bentry_sem_txt.setObjectName(_fromUtf8("Bentry_sem_txt"))
        self.verticalLayout_2.addWidget(self.Bentry_sem_txt)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Bentry_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Bentry_add_btn.setObjectName(_fromUtf8("Bentry_add_btn"))
        self.horizontalLayout_2.addWidget(self.Bentry_add_btn)
        self.Bentry_clr_btn = QtGui.QPushButton(self.centralwidget)
        self.Bentry_clr_btn.setObjectName(_fromUtf8("Bentry_clr_btn"))
        self.horizontalLayout_2.addWidget(self.Bentry_clr_btn)
        self.Bentry_cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.Bentry_cancel_btn.setObjectName(_fromUtf8("Bentry_cancel_btn"))
        self.horizontalLayout_2.addWidget(self.Bentry_cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
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
        QtCore.QObject.connect(self.Bentry_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Bentry_Bnme_txt.clear)
        QtCore.QObject.connect(self.Bentry_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Bentry_bid_txt.clear)
        QtCore.QObject.connect(self.Bentry_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Bentry_author_txt.clear)
        QtCore.QObject.connect(self.Bentry_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.bentry_isbn_txt.clear)
        QtCore.QObject.connect(self.Bentry_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Bentryt_publisher_txt.clear)
        QtCore.QObject.connect(self.Bentry_clr_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Bentry_genre_txt.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_7.setText(_translate("MainWindow", "Enter Book Details", None))
        self.label.setText(_translate("MainWindow", "Book Name:", None))
        self.label_2.setText(_translate("MainWindow", "Book Id:", None))
        self.label_3.setText(_translate("MainWindow", "Author:", None))
        self.label_4.setText(_translate("MainWindow", "ISBN:", None))
        self.label_5.setText(_translate("MainWindow", "Publisher:", None))
        self.label_6.setText(_translate("MainWindow", "Genre:", None))
        self.label_8.setText(_translate("MainWindow", "Semester", None))
        self.Bentry_add_btn.setText(_translate("MainWindow", "Add", None))
        self.Bentry_clr_btn.setText(_translate("MainWindow", "Clear", None))
        self.Bentry_cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.Bentry_add_btn.clicked.connect(self.Add)
        self.Bentry_cancel_btn.clicked.connect(self.hideit)

    def Add(self):
        B_name =self.Bentry_Bnme_txt.text()
        B_id = self.Bentry_bid_txt.text()
        B_author = self.Bentry_author_txt.text()
        B_isbn = self.bentry_isbn_txt.text()
        B_publisher = self.Bentryt_publisher_txt.text()
        B_genre = self.Bentry_genre_txt.text()
        B_semester = self.Bentry_sem_txt.text()
        if(not B_name):
            QtGui.QMessageBox.information(self,'Message','Book Name Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not B_id):
            QtGui.QMessageBox.information(self,'Message','Book Id Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not B_author):
            QtGui.QMessageBox.information(self,'Message','Book Author Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not B_isbn):
            QtGui.QMessageBox.information(self,'Message','Book ISBN Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not B_publisher):
            QtGui.QMessageBox.information(self,'Message','Book Publisher Cannot Be Blank',QtGui.QMessageBox.Ok)
        elif(not B_genre):
            QtGui.QMessageBox.information(self,'Message','Book Genre Cannot Be Blank',QtGui.QMessageBox.Ok)
        else:
            answer = self.db.Search("BookId",B_id)
            if(not answer):
                self.db.AddEntryToBookTable(int(B_id),B_name,B_author,B_isbn,B_publisher,B_genre,B_semester)
                self.db.comm()
                QtGui.QMessageBox.information(self,'Message','Details Added Successfully ',QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.information(self,'Message','Duplicate Book Id Found',QtGui.QMessageBox.Ok)

    def hideit(self):
        self.hide()

    def keyPressEvent(self, event):
        k = event.key()
        if k == QtCore.Qt.Key_Return:
            self.Add()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Bookentry()
    ex.show()
    sys.exit(app.exec())
