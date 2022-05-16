import tkinter as tk
from PIL import ImageTk, Image

import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from sqlconnect import *

ADDLABEL = ("Arial", 9 , "bold")
ENTRYFONT = ("Cambria", 9)
BUTTON = ("Arial", 10, "bold")

class Admin:

    def __init__(self):

        self.window = tk.Toplevel()
        self.window.geometry("400x500")
        self.window.resizable(False,False)   
        self.window.title("Hi")
        #self.window.eval('tk::PlaceWindow . center')
        self.window.config(bg = "#032139")

        self.count = 1

        self.crLogo()
        self.crEntry()
        self.crButton()

    def crLogo(self):
        self.logoImage = Image.open("Image/logo.png")
        self.logo = ImageTk.PhotoImage(self.logoImage)
        myLogo = tk.Label(self.window, image = self.logo, borderwidth = 0, highlightthickness = 0, bg ="#032139")
        myLogo.place(x = 80 , y = 30)

    def crEntry(self):
        connect = connection()
        cursor = connect.cursor()
        sql = "SELECT * FROM info"
        cursor.execute(sql) 
        result = cursor.fetchall()

        self.getUsername = ""
        self.getPass = ""

        for x in result:

            self.getUsername = x[0]
            self.getPass = x[1]

            print(self.getUsername)
            print(self.getPass)

        usernameLabel = tk.Label(self.window, text = "Username", font = ADDLABEL, bg = "#032139", fg ="#adadad")
        usernameLabel.place(x = 32, y = 195)

        self.userNameEntry = tk.Entry(self.window, font = ENTRYFONT , fg ="White", bg = "#01345e", width = 45, borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.userNameEntry.insert(0,self.getUsername)
        self.userNameEntry.config(state =tk.DISABLED,disabledbackground = "#01345e", disabledforeground = "#9A9A9A")
        self.userNameEntry.place(x = 32, y = 220, height = 37)

        passLabel = tk.Label(self.window, text = "Password", font = ADDLABEL, bg = "#032139", fg ="#adadad")
        passLabel.place(x = 32, y = 275)

        self.passEntry = tk.Entry(self.window, show = "*" , fg ="White", bg = "#01345e", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.passEntry.insert(0,self.getPass)
        self.passEntry.config(state =tk.DISABLED,disabledbackground = "#01345e", disabledforeground = "#9A9A9A")
        self.passEntry.place(x = 32, y = 300, height = 37, width = 335)    

    def crButton(self):

        self.saveButton = tk.Button(self.window, text = "Save",font = BUTTON, fg ="White", bg = "#00999b", width = 41, highlightthickness = 0, relief = "flat", command = self.update)
        self.saveButton.config(state = tk.DISABLED, disabledforeground = "#CACACA")
        self.saveButton.place(x = 32, y = 370, height = 37)   

        self.editButton = tk.Button(self.window, text = "Edit",font = BUTTON, fg ="White", bg = "#00999b", width = 41, highlightthickness = 0, relief = "flat", command =self.editAction)
        self.editButton.place(x = 32, y = 420, height = 37) 

    def editAction(self):
        
        
        if self.count < 2:

            self.confirm = tk.Toplevel()
            self.confirm.geometry("400x130")
            self.confirm.resizable(False,False)
            self.confirm.title("Account Information")
            self.confirm.config(bg = "#032139")
            #self.confirm.eval('tk::PlaceWindow . center')
     

            passwordLabel = tk.Label(self.confirm, text = "Enter Password" , fg = "White", bg = "#032139")
            passwordLabel.place(x = 10 , y = 35)

            self.passwordEntry =tk.Entry(self.confirm, fg = "White" ,show = "*", bg ="#01345e",borderwidth = 10, highlightthickness = 0, relief = "flat")
            self.passwordEntry.place (x = 100 , y = 30, width = 280, height = 30)         

            button = tk.Button(self.confirm, text = "Submit" ,bg = "#00999b", fg ="White", highlightthickness = 0, relief = "flat", command = self.confirmPass)
            button.place(x = 170 , y = 80, width = "100", height = "30" )
            
            self.count += 1
            self.confirm.mainloop()

        
        self.count = 0
            

    def confirmPass(self):

        if self.passwordEntry == "":
            MessageBox.showerror("Erorr","Invalid Password")

        else:
            
            connect = connection()
            cursor = connect.cursor()
            sql = "SELECT * FROM info"
            cursor.execute(sql) 
            result = cursor.fetchall()

        

            for x in result:

                if x[1] == self.passwordEntry.get():
                    self.saveButton.config(state = tk.NORMAL)
                    self.passEntry.config(state = tk.NORMAL)
                    self.userNameEntry.config(state = tk.NORMAL)
                    self.confirm.destroy()

                else:

                    MessageBox.showerror("Erorr","Invalid Password")

    def update(self):
        a = self.userNameEntry.get()
        b = self.passEntry.get()
        

        if a =="" or b=="":
            MessageBox.showerror("Erorr","Please Complete the Entries")
            

        else:
            
            connect = connection()
            cursor = connect.cursor()
            sql = "UPDATE info SET username = %s, password = %s "
       
            val = (a,b)
            cursor.execute(sql, val) 
            result = cursor.fetchall()

            connect.commit()
            connect.close()

            self.window.destroy()
            
    def run(self):

        self.window.mainloop()

    def y ():

        return 0

if __name__ == "__main__":

    myAdmin = Admin()
    myAdmin.run()

