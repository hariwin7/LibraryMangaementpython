#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime


# ================================

class Database:
    def __init__(self):
        self.dbname = "Librarydb"
        self.B_entry_tble = "Bookentrytable"
        self.usr_tble = "UserTable"
        self.issue_tble = "Issue"
        self.usrpass_tble = "Userpassword"
        self.admpass_tble = "Adminpassword"
        passwd = "password"

        self.conn = mysql.connector.connect(user='root', password=passwd, host='127.0.0.1')
        self.cursor = self.conn.cursor()

        self.ConnectToDatabase()
        self.CreateTable()

    def ConnectToDatabase(self):
        try:
            self.conn.database = self.dbname
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.CreateDatabase()
                self.conn.database = self.dbname

    def CreateDatabase(self):
        try:
            self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" % self.dbname)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

    def CreateTable(self):
        cmd = (" CREATE TABLE IF NOT EXISTS " + self.B_entry_tble + " ("
                                                                    " `ID` int(5) NOT NULL AUTO_INCREMENT,"
                                                                    " `Book_Name` varchar(50) NOT NULL,"
                                                                    " `BookId` int(10) NOT NULL,"
                                                                    " `Author` text NOT NULL,"
                                                                    " `ISBN` varchar(20) NOT NULL,"
                                                                    " `Publisher` varchar(50) NOT NULL,"
                                                                    " `Genre` varchar(25) NOT NULL,"
                                                                    " `Semester` varchar(5) ,"
                                                                    " `Status` varchar(20) NOT NULL,"

                                                                    " CONSTRAINT `k` PRIMARY KEY (`ID`,`BookId`)"
                                                                    ")ENGINE = InnoDB;")

        usr = (" CREATE TABLE IF NOT EXISTS " + self.usr_tble + "("
                                                                " `Name` varchar(25) NOT NULL,"
                                                                " `Department` varchar(10) NOT NULL,"
                                                                " `UserId` varchar(8) NOT NULL,"
                                                                " `Designation` varchar(25) NOT NULL,"
                                                                " `Contact` varchar(25),"
                                                                "  PRIMARY KEY (`UserId`)"
                                                                ")ENGINE = InnoDB;")
        issue = (" CREATE TABLE IF NOT EXISTS " + self.issue_tble + "("
                                                                    " `BookId` int(10) NOT NULL,"
                                                                    " `UserId` varchar(15) NOT NULL,"
                                                                    " `Date` date NOT NULL,"
                                                                    " `Time` time NOT NULL,"
                                                                    " PRIMARY KEY (`BookId`)"
                                                                    ")ENGINE = InnoDB;")
        usrpasswd = (" CREATE TABLE IF NOT EXISTS " + self.usrpass_tble + "("
                                                                    " `Slno` int(5) NOT NULL AUTO_INCREMENT,"
                                                                    " `Username` varchar(10) NOT NULL,"
                                                                    " `Password` varchar(30) NOT NULL,"
                                                                    "PRIMARY KEY (`Slno`,`Username`)"
                                                                    ")ENGINE = InnoDB;")
        admpasswd = (" CREATE TABLE IF NOT EXISTS " + self.admpass_tble + "("
                                                                    " `Slno` int(5) NOT NULL AUTO_INCREMENT,"
                                                                    " `Password` varchar(15) NOT NULL,"
                                                                    "PRIMARY KEY (`Slno`)"
                                                                    ")ENGINE = InnoDB;")

        self.RunCommand(cmd)
        self.RunCommand(usr)
        self.RunCommand(issue)
        self.RunCommand(usrpasswd)
        self.RunCommand(admpasswd)

    def RunCommand(self, cmd):
        print("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)            
        except mysql.connector.Error as err:
            print('ERROR MESSAGE: ' + str(err.msg))
            print('WITH ' + cmd)
            return err.errno
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg

    def AddEntryToBookTable(self, Book_id, Book_name, Author_name, isbn, publisher, genre, semester):

        status = "Available"
        cmd = " INSERT INTO " + self.B_entry_tble + " (Book_Name, BookId, Author, ISBN, Publisher, Genre, Semester,Status)"
        cmd += " VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' );" % (
            Book_name, Book_id, Author_name, isbn, publisher, genre, semester, status)
        self.RunCommand(cmd)

    def AddEntryToUserTable(self, name, department, userid, designation, contact):
    	
    	cmd = " INSERT INTO " + self.usr_tble + " (Name, Department, UserId, Designation, Contact)"
    	cmd += " VALUES ('%s', '%s', '%s', '%s', '%s');" % (name, department, userid, designation, contact)
    	err = self.RunCommand(cmd)
    	if(err!=1062):
    		return 1
    	else:
    		return err    	

    def AddEntryToIssueTable(self, Book_id, userid):

        date1 = datetime.now().strftime("%y-%m-%d")
        time = datetime.now().strftime("%H:%M")
        cmd = " INSERT INTO " + self.issue_tble + " (BookId,UserId,Date,Time)"
        cmd += " VALUES ('%s', '%s', '%s', '%s');" % (Book_id, userid, date1, time)
        err = self.RunCommand(cmd)
        return err

    def AddEntryToUPassword(self,usrnme,passwd):
        cmd = " INSERT INTO " + self.usrpass_tble + " (Username,Password)"
        cmd += " VALUES ('%s', '%s');" % (usrnme,passwd)
        self.RunCommand(cmd)
    def AddEntryToAPassword(self,passwd):
        cmd = " INSERT INTO " + self.admpass_tble + " (Password)"
        cmd += " VALUES ('%s');" % (passwd)
        self.RunCommand(cmd)

    def GetColumns(self,tablename):
        return self.RunCommand("SHOW COLUMNS FROM %s;" % tablename)

    def GetTable(self, tablename):
        self.CreateTable()
        return self.RunCommand("SELECT * FROM %s;" % tablename)

    def GetUserPassword(self,usrnme):
        self.CreateTable()
        return self.RunCommand("SELECT * FROM %s WHERE Username LIKE %s;" % (self.usrpass_tble,usrnme))

    def GetAdminPassword(self):
        self.CreateTable()
        return self.RunCommand("SELECT * FROM %s;" % (self.admpass_tble))

    def GetUser(self,tablename,userid):
        self.CreateTable()
        return self.RunCommand("SELECT * FROM %s WHERE UserId = %s;" % (tablename,userid))

    def Search(self, ser_type, ser_id):
        return self.RunCommand("SELECT * FROM Bookentrytable WHERE %s LIKE %s ;" % (ser_type, ser_id))

    def Delete(self,bookid):
    	self.RunCommand("DELETE  FROM  Issue WHERE BookId = %s;" % bookid)

    def Update(self,bookid,status):
    	self.RunCommand("UPDATE %s SET Status = %s WHERE BookId = %s; " % (self.B_entry_tble,status,bookid))

    def GetUserBooks(self,usrnme):
        self.CreateTable()
        return self.RunCommand("SELECT * FROM %s WHERE UserId LIKE %s;" % (self.issue_tble,usrnme))

    def DeleteUser(self,userid):
    	self.RunCommand("DELETE  FROM  UserTable WHERE UserId = %s;" % userid)
    	self.RunCommand("DELETE FROM Issue WHERE UserId = %s;" % userid)

    def DeleteUserinall(self,tablename,colom,userid):
    	self.RunCommand("DELETE  FROM %s WHERE %s = %s;" %(tablename,colom ,userid))

    def GetIssue(self,tablename,userid):
        self.CreateTable()
        return self.RunCommand("SELECT * FROM %s WHERE BookId = %s;" % (tablename,userid))

    def UpdatePassword(self,username,passwd):
    	self.RunCommand("UPDATE Userpassword SET Password = %s WHERE Username = %s; " % (passwd,username))

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def comm(self):
        self.conn.commit()


if __name__ == '__main__':
    db = Database()

    #db.AddEntryToBookTable('22', 'signal processing', 'ramesh   babu', "978-81-8371-288-0", "scietech publications",
     #                      "electronics", "S5")
    #db.AddEntryToUserTable("hari prasad", "cse", "cs02713", "associate proffessor", "04802467123")
    #db.AddEntryToIssueTable("22", "cs02713")
    #print(db.GetTable("Bookentrytable"))
    #print(db.GetTable("UserTable"))
    #print(db.GetTable("Issue"))
    #db.AddEntryToAPassword("password")
    #db.AddEntryToUPassword("cs02713", "lol")
    #print(db.GetAdminPassword())
    #print(db.GetUserPassword("'%cs02713%'"))
    #print(db.GetUser("UserTable","'cs02713'"))
    #db.AddEntryToIssueTable(1,"cs02713")
    
    #print(db.GetUser("Issue","'cs02713'"))

