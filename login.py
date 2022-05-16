import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from sqlconnect import *

import myMain

TAGNAME = ("Lucida Handwriting", 10, "bold")
LOGINLABEL = ("Rockwell", 25, "bold")
ADDLABEL = ("Arial", 9 , "bold")
ENTRYFONT = ("Cambria", 9)
BUTTON = ("Arial", 12, "bold")
class LogIn:

    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("930x600")
        self.window.resizable(False,False)
        self.logoImage = Image.open("Image/logo.png")
        self.logo = ImageTk.PhotoImage(self.logoImage)

        self.fbLogo = Image.open("Image/fbedit.png")
        self.myfb = ImageTk.PhotoImage(self.fbLogo)

        self.dotaLogo = Image.open("Image/dotaedit.png")
        self.mydota = ImageTk.PhotoImage(self.dotaLogo)

        self.googleLogo = Image.open("Image/gedit.png")
        self.myGoogle = ImageTk.PhotoImage(self.googleLogo)

        self.codLogo = Image.open("Image/codmedit.png")
        self.myCod= ImageTk.PhotoImage(self.codLogo)
        
        
        self.instaLogo = Image.open("Image/insta.png")
        self.myInsta= ImageTk.PhotoImage(self.instaLogo)

        self.mlLogo = Image.open("Image/mb.png")
        self.myML= ImageTk.PhotoImage(self.mlLogo)

        self.lbLogo = Image.open("Image/lb.png")
        self.myLb= ImageTk.PhotoImage(self.lbLogo)

        self.idLogo = Image.open("Image/id.png")
        self.myId= ImageTk.PhotoImage(self.idLogo)

        self.myrightFrame = self.createRight_Frame()
        self.leftFrame = self.crleftFrame()
        self.createLogo()
        self.accountLogos()
        self.crIdLogo()
        self.createLabel()
        self.createButton() 


    def createRight_Frame(self):

        rightFrame = tk.Frame(self.window, bg = "#032139" ,height = 600, width = 430)
        rightFrame.place(x = 0 , y= 0)
        return rightFrame

    def createLogo(self):
        logoLabel = tk.Label(self.myrightFrame, image = self.logo, bd = 0 , highlightthickness = 0)
        logoLabel.place(x = 100 , y = 120)

        context = tk.Label(self.myrightFrame, text = "One Name, Storage for All !!!", font = TAGNAME , bg ="#032139", fg ="White")
        context.place( x= 98 , y = 260)

    def accountLogos(self):

        fb = tk.Label(self.myrightFrame, image = self.myfb, bd = 0 , highlightthickness = 0 , bg ="#032139")
        fb.place(x = 30, y = 330)

        dota = tk.Label(self.myrightFrame, image = self.mydota, bd = 0 , highlightthickness = 0 , bg ="#032139")
        dota.place(x = 110, y = 332)

        google = tk.Label(self.myrightFrame, image = self.myGoogle, bd = 0 , highlightthickness = 0 , bg ="#032139")
        google.place(x = 190, y = 330)

        cod = tk.Label(self.myrightFrame, image = self.myCod, bd = 0 , highlightthickness = 0 , bg ="#032139")
        cod.place(x = 270, y = 332)

        insta = tk.Label(self.myrightFrame, image = self.myInsta, bd = 0 , highlightthickness = 0 , bg ="#032139")
        insta.place(x = 351, y = 332)

        ml = tk.Label(self.myrightFrame, image = self.myML, bd = 0 , highlightthickness = 0 , bg ="#032139")
        ml.place(x = 60, y = 400)

        lb = tk.Label(self.myrightFrame, image = self.myLb, bd = 0 , highlightthickness = 0 , bg ="#032139")
        lb.place(x = 240, y = 402)


    def crleftFrame(self):

        leftFrame = tk. Frame(self.window, width =500 ,height =600 ,bg ="#002645")
        leftFrame.place(x = 430, y = 0)

        return leftFrame

    def crIdLogo(self):

        idLogo = tk.Label(self.leftFrame, image = self.myId, bg = "#002645")
        idLogo.place(x = 170 , y = 30)

        loginLabel = tk.Label(self.leftFrame , text = "LOG IN ", bg = "#002645", font =LOGINLABEL, fg = "White" )
        loginLabel.place (x = 185, y = 200)

    def createLabel(self):

        usernameLabel = tk.Label(self.leftFrame , text = "Username", font = ADDLABEL, fg ="#adadad" ,bg =  "#002645")
        usernameLabel.place(x = 60, y =260)

        self.usernameEntry = tk.Entry (self.leftFrame , font = ENTRYFONT , fg ="White", bg = "#01345e", width = 52, borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.usernameEntry.place(x = 60, y = 285, height = 37)

        passwordLabel = tk.Label(self.leftFrame , text = "Password", font = ADDLABEL, fg ="#adadad" ,bg =  "#002645")
        passwordLabel.place(x = 60, y =340)

        self.passEntry = tk.Entry (self.leftFrame ,show = "*", font = ENTRYFONT , fg ="White", bg = "#01345e", width = 52, borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.passEntry.place(x = 60, y = 365, height = 37)

    def createButton(self):

        loginButton = tk.Button(self.leftFrame, text = "Login",font = BUTTON, fg ="White", bg = "#00999b", width = 38, highlightthickness = 0, relief = "flat", command = self.verifyLogin)
        loginButton.place(x = 60, y = 440 , height = 37)


    def verifyLogin(self):
        
        getUsername = self.usernameEntry.get()
        getPassword = self.passEntry.get()


        if getUsername == "" or getPassword =="":
            self.invalid()
        
        else:
            connect = connection()
            cursor = connect.cursor()
            sql = "SELECT * FROM info"
            cursor.execute(sql) 
            result = cursor.fetchall()

            for x in result:
                #print(x[0],x[1])
                if x[0] == getUsername and x[1] == getPassword:

                    
                    self.window.destroy()
                    gotoMain = myMain.Interface()

                else:
                     # print(x[0],x[1])
                      self.invalid()      
                      self.usernameEntry.delete(0,'end')
                      self.passEntry.delete(0,'end')
            connect.commit()
            connect.close()
    def invalid(self):
        MessageBox.showerror("Invalid Info","Incorrect Username or Password")

    def run(self):

        self.window.mainloop()



if __name__ =="__main__":

    myLogin = LogIn()
    myLogin.run()