# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_Search.ui'
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

class Search(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = Lib_DB.Database()
        self.UpdateTree()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 463)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Search_txt = QtGui.QLineEdit(self.centralwidget)
        self.Search_txt.setObjectName(_fromUtf8("Search_txt"))
        self.horizontalLayout.addWidget(self.Search_txt)
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.horizontalLayout.addWidget(self.Search_btn)
        self.Search_clr_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_clr_btn.setObjectName(_fromUtf8("Search_clr_btn"))
        self.horizontalLayout.addWidget(self.Search_clr_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.B_name_radio = QtGui.QRadioButton(self.centralwidget)
        self.B_name_radio.setObjectName(_fromUtf8("B_name_radio"))
        self.B_name_radio.setChecked(True)
        self.horizontalLayout_2.addWidget(self.B_name_radio)
        self.B_id_radio = QtGui.QRadioButton(self.centralwidget)
        self.B_id_radio.setObjectName(_fromUtf8("B_id_radio"))
        self.horizontalLayout_2.addWidget(self.B_id_radio)
        self.B_isbn_radio = QtGui.QRadioButton(self.centralwidget)
        self.B_isbn_radio.setObjectName(_fromUtf8("B_isbn_radio"))
        self.horizontalLayout_2.addWidget(self.B_isbn_radio)
        self.B_author_radio = QtGui.QRadioButton(self.centralwidget)
        self.B_author_radio.setObjectName(_fromUtf8("B_author_radio"))
        self.horizontalLayout_2.addWidget(self.B_author_radio)
        self.B_genre_radio = QtGui.QRadioButton(self.centralwidget)
        self.B_genre_radio.setObjectName(_fromUtf8("B_genre_radio"))
        self.horizontalLayout_2.addWidget(self.B_genre_radio)
        self.B_semester_radio = QtGui.QRadioButton(self.centralwidget)
        self.B_semester_radio.setObjectName(_fromUtf8("B_semester_radio"))
        self.horizontalLayout_2.addWidget(self.B_semester_radio)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 88, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Search_tree_widget = QtGui.QTreeWidget(self.centralwidget)
        self.Search_tree_widget.setObjectName(_fromUtf8("Search_tree_widget"))
        self.Search_tree_widget.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout.addWidget(self.Search_tree_widget)
        self.verticalLayout_3.addLayout(self.verticalLayout)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Search_btn.setText(_translate("MainWindow", "Search", None))
        self.Search_clr_btn.setText(_translate("MainWindow", "Clear", None))
        self.label.setText(_translate("MainWindow", "Search By", None))
        self.B_name_radio.setText(_translate("MainWindow", "Book Name", None))
        self.B_id_radio.setText(_translate("MainWindow", "Book Id", None))
        self.B_isbn_radio.setText(_translate("MainWindow", "ISBN", None))
        self.B_author_radio.setText(_translate("MainWindow", "Author", None))
        self.B_genre_radio.setText(_translate("MainWindow", "Genre", None))
        self.B_semester_radio.setText(_translate("MainWindow", "Semester", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.Search_btn.clicked.connect(self.searchit)
        self.Search_clr_btn.clicked.connect(self.Search_txt.clear)


    def UpdateTree(self):
        table = self.db.GetTable("Bookentrytable")
        col = self.db.GetColumns("Bookentrytable")
                
        self.Search_tree_widget.clear()

        for c in range(len(col)):
            self.Search_tree_widget.headerItem().setText(c, col[c][0])
        
        for item in range(len(table)):
            QtGui.QTreeWidgetItem(self.Search_tree_widget)
            for value in range(len(table[item])):
                self.Search_tree_widget.topLevelItem(item).setText(value, str(table[item][value]))

        self.Search_tree_widget.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.Search_tree_widget.header().setStretchLastSection(False)
        self.Search_tree_widget.setAlternatingRowColors(True) 
        self.Search_tree_widget.setStyleSheet("alternate-background-color :lavender")   

    def searchit(self):
        serid = self.Search_txt.text()
        serid  = '\''+'%'+ serid +'%' +'\''
       
        
        if(self.B_name_radio.isChecked()):
            k = self.db.Search("Book_Name",serid)            
        elif(self.B_id_radio.isChecked()):
            k = self.db.Search("BookId",serid)
        elif(self.B_isbn_radio.isChecked()):
            k = self.db.Search("ISBN",serid)
        elif(self.B_author_radio.isChecked()):
            k = self.db.Search("Author",serid)
        elif(self.B_genre_radio.isChecked()):
            k = self.db.Search("Genre",serid)
        elif(self.B_semester_radio.isChecked()):
            k = self.db.Search("Semester",serid)

        if(not k):
            QtGui.QMessageBox.information(self,'Message','Entry Not found',QtGui.QMessageBox.Ok)


        col = self.db.GetColumns("Bookentrytable")
                
        self.Search_tree_widget.clear()

        for c in range(len(col)):
           self.Search_tree_widget.headerItem().setText(c, col[c][0])
        

        for item in range(len(k)):
            QtGui.QTreeWidgetItem(self.Search_tree_widget)
            for value in range(len(k[item])):
                self.Search_tree_widget.topLevelItem(item).setText(value, str(k[item][value]))

        self.Search_tree_widget.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.Search_tree_widget.header().setStretchLastSection(False)

    def keyPressEvent(self, event):
        k = event.key()
        if k == QtCore.Qt.Key_Return:
            self.searchit()
            

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec())
