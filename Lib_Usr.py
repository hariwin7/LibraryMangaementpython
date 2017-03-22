# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Usr.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import Lib_DB,Lib_Search,Lib_Change
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

class Usr(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = Lib_DB.Database()
        # self.ob = Lib_Change.Change()
       
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Usr_nme_labl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.Usr_nme_labl.setFont(font)
        self.Usr_nme_labl.setText(_fromUtf8(""))
        self.Usr_nme_labl.setObjectName(_fromUtf8("Usr_nme_labl"))
        self.verticalLayout_2.addWidget(self.Usr_nme_labl)
        self.Usr_id_labl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.Usr_id_labl.setFont(font)
        self.Usr_id_labl.setText(_fromUtf8(""))
        self.Usr_id_labl.setObjectName(_fromUtf8("Usr_id_labl"))
        self.verticalLayout_2.addWidget(self.Usr_id_labl)
        self.Usr_dep_labl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.Usr_dep_labl.setFont(font)
        self.Usr_dep_labl.setText(_fromUtf8(""))
        self.Usr_dep_labl.setObjectName(_fromUtf8("Usr_dep_labl"))
        self.verticalLayout_2.addWidget(self.Usr_dep_labl)
        self.Usr_desig_labl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.Usr_desig_labl.setFont(font)
        self.Usr_desig_labl.setText(_fromUtf8(""))
        self.Usr_desig_labl.setObjectName(_fromUtf8("Usr_desig_labl"))
        self.verticalLayout_2.addWidget(self.Usr_desig_labl)
        self.Usr_conta_labl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.Usr_conta_labl.setFont(font)
        self.Usr_conta_labl.setText(_fromUtf8(""))
        self.Usr_conta_labl.setObjectName(_fromUtf8("Usr_conta_labl"))
        self.verticalLayout_2.addWidget(self.Usr_conta_labl)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(253, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.Usr_book_treewidget = QtGui.QTreeWidget(self.centralwidget)
        self.Usr_book_treewidget.setObjectName(_fromUtf8("Usr_book_treewidget"))
        self.Usr_book_treewidget.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_3.addWidget(self.Usr_book_treewidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSearch = QtGui.QMenu(self.menubar)
        self.menuSearch.setObjectName(_fromUtf8("menuSearch"))
        self.menuReserve_Book = QtGui.QMenu(self.menubar)
        self.menuReserve_Book.setObjectName(_fromUtf8("menuReserve_Book"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuChange_Password = QtGui.QMenu(self.menubar)
        self.menuChange_Password.setObjectName(_fromUtf8("menuChange_Password"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionAdvanced_search = QtGui.QAction(MainWindow)
        self.actionAdvanced_search.setObjectName(_fromUtf8("actionAdvanced_search"))
        self.actionReserve = QtGui.QAction(MainWindow)
        self.actionReserve.setObjectName(_fromUtf8("actionReserve"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionContact = QtGui.QAction(MainWindow)
        self.actionContact.setObjectName(_fromUtf8("actionContact"))
        self.actionChange_Password = QtGui.QAction(MainWindow)
        self.actionChange_Password.setObjectName(_fromUtf8("actionChange_Password"))
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuSearch.addAction(self.actionAdvanced_search)
        self.menuSearch.addSeparator()
        self.menuReserve_Book.addAction(self.actionReserve)
        self.menuReserve_Book.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionContact)
        self.menuChange_Password.addAction(self.actionChange_Password)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuReserve_Book.menuAction())
        self.menubar.addAction(self.menuChange_Password.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Name:", None))
        self.label_4.setText(_translate("MainWindow", "User id:", None))
        self.label_3.setText(_translate("MainWindow", "Department:", None))
        self.label_5.setText(_translate("MainWindow", "Designation:", None))
        self.label_6.setText(_translate("MainWindow", "Contact info:", None))
        self.label_11.setText(_translate("MainWindow", "Books Issued", None))
        self.menuFile.setTitle(_translate("MainWindow", "File ", None))
        self.menuSearch.setTitle(_translate("MainWindow", "Search", None))
        self.menuReserve_Book.setTitle(_translate("MainWindow", "Reserve Book", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuChange_Password.setTitle(_translate("MainWindow", "Change Password", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionAdvanced_search.setText(_translate("MainWindow", "Advanced search", None))
        self.actionReserve.setText(_translate("MainWindow", "Reserve", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionContact.setText(_translate("MainWindow", "Contact", None))
        self.actionChange_Password.setText(_translate("MainWindow", "Change Password", None))
        self.actionAdvanced_search.triggered.connect(self.ShowSearch)
        self.actionChange_Password.triggered.connect(self.ShowChange)

    def GetUser(self,userid):
        self.usrid = userid
        table = self.db.GetUser("UserTable",userid)
        self.Usr_nme_labl.setText(_fromUtf8(table[0][0]))
        self.Usr_dep_labl.setText(_fromUtf8(table[0][1]))
        self.Usr_id_labl.setText(_fromUtf8(table[0][2]))
        self.Usr_desig_labl.setText(_fromUtf8(table[0][3]))
        self.Usr_conta_labl.setText(_fromUtf8(table[0][4]))
       

    def Settree(self,userid):
        col = self.db.GetColumns("Bookentrytable")
               
        self.Usr_book_treewidget.clear()

        for c in range(len(col)+1):
            if(c<len(col)):
                self.Usr_book_treewidget.headerItem().setText(c, col[c][0])
            else:
                 self.Usr_book_treewidget.headerItem().setText(c,"Issue Date")

        self.Usr_book_treewidget.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.Usr_book_treewidget.header().setStretchLastSection(False)
        self.Usr_book_treewidget.setAlternatingRowColors(True) 
        self.Usr_book_treewidget.setStyleSheet("alternate-background-color :lavender")

            
        booktab = []
        issuetab = self.db.GetUserBooks(userid)
        print(issuetab)
        for i in range(len(issuetab)):
            bookid = issuetab[i][0]
            booktab = booktab + self.db.Search("BookId",bookid)
            print(booktab)

        for k in range(len(booktab)):
                QtGui.QTreeWidgetItem(self.Usr_book_treewidget)
                for l in range(len(booktab[k])+1):
                    if(l<len(booktab[k])):
                        self.Usr_book_treewidget.topLevelItem(k).setText(l, str(booktab[k][l]))
        for k in range(len(issuetab)):
            QtGui.QTreeWidgetItem(self.Usr_book_treewidget)
            self.Usr_book_treewidget.topLevelItem(k).setText(9, str(issuetab[k][2]))
    def ShowSearch(self):
        self.subsearch = Lib_Search.Search()
        self.subsearch.show()
    def ShowChange(self):
        self.subchange = Lib_Change.Change()
        self.subchange.show()
              


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Usr()
    ex.show()
    sys.exit(app.exec())


