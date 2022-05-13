import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import tkinter as tk

import myMain

class dataBase:

    def __init__(self,getName = 0 ,getEmail = 0,getPhone = 0,getPass = 0, getType= 0):

        self.connect = mysql.connect(
            host = "localhost", 
            username = "root",
            port ="3306", 
            password="", 
            database = "accountstorage"
            )
        self.getName = getName
        self.getEmail = getEmail
        self.getPhone = getPhone
        self.getPass = getPass
        self.getType = getType

    def setEntry(self,getName, getEmail, getPhone, getPass, getType):

        self.getName = getName
        self.getEmail = getEmail
        self.getPhone = str(getPhone)
        self.getPass = getPass
        self.getType = getType


    def insert(self):
        
        if (self.getName == ""or self.getEmail == ""or self.getPhone == ""or self.getPass == ""or self.getType == ""):

            MessageBox.showinfo("Insert Status","Complete the following form")

        else:
             cursor = self.connect.cursor()
             sql = ("INSERT INTO mytable (Accountname,Email,Password,Phone,Type) VALUES(%s,%s,%s,%s,%s)")
             val = (self.getName, self.getEmail,self.getPass, self.getPhone, self.getType)
             cursor.execute(sql,val)
            #cursor.execute("INSERT INTO example (name,email,phone,password,type) VALUES('"+info1+"','"+info2+"','"+info3+"','"+info4+"','"+info5+"')")
            
             cursor.execute("commit")
             objMain = myMain.Interface()
             objMain.resetAccount()
             objMain.resetEmail()
             objMain.resetPass()
             objMain.resetPhone()
             MessageBox.showinfo("Insert Status","Data Added Successfully")
             self.connect.close()


