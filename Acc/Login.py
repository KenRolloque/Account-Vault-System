import tkinter as tk
import tkinter .ttk as ttk
from PIL import ImageTk, Image
import tkinter.font as font
import Main

LOGIN = ("Antipasto Pro",20)
LOGINLABEL = ("Bahnschrift",8)
LOGINBUT = ("Bahnschrift",12,"bold")
LABEL1 = ("Segoe UI",10,"normal")
LABEL2 = ("Segoe UI",11,"normal")

TITLE = ("Consolas ",25,"bold")
TAG = ("Segoe UI",15)
class LogIn:
    
    def __init__(self):

        self.main = tk.Tk()
        self.main.withdraw()
        self.window = tk.Toplevel(width = 980, height = 700)
        self.window.title("Login")
        self.window.resizable(False,False)


        width = 980
        height = 700

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

        # Declaration of Image

        self.loginImg = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/icons8-male-user-100.png")
        self.resizeLogin = self.loginImg.resize((60,60))
        self.myLoginImg = ImageTk.PhotoImage(self.resizeLogin)

        self.logo = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/logo.png")
        self.resizeLogo = self.logo.resize((250,220))
        self.myLogo = ImageTk.PhotoImage(self.resizeLogo)


        self.accLogo = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/1.png")
        self.myAccLogo = ImageTk.PhotoImage(self.accLogo)

        self.accLogo2 = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/fbedit.png")
        self.resizeAccLogo2 = self.accLogo2.resize((32,27))
        self.myAccLogo2 = ImageTk.PhotoImage(self.resizeAccLogo2)

        self.accLogo3 = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/codmedit.png")
        self.resizeAccLogo3 = self.accLogo3.resize((32,27))
        self.myAccLogo3 = ImageTk.PhotoImage(self.resizeAccLogo3)

        self.accLogo4 = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/dotaedit.png")
        self.resizeAccLogo4 = self.accLogo4.resize((32,27))
        self.myAccLogo4 = ImageTk.PhotoImage(self.resizeAccLogo4)

        self.bottom = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/bottom.png")
        self.resizeBot = self.bottom.resize((370,220))
        self.myBot = ImageTk.PhotoImage(self.resizeBot)

        self.circle = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/circle.png")

        self.resizeCircle = self.circle.resize((137,132))
        self.myCircle = ImageTk.PhotoImage(self.resizeCircle)

        self.resizeCircle2 = self.circle.resize((57,52))
        self.myCircle2 = ImageTk.PhotoImage(self.resizeCircle2)

        self.resizeCircle4 = self.circle.resize((77,72))
        self.myCircle4 = ImageTk.PhotoImage(self.resizeCircle4)

        self.resizeCircle5 = self.circle.resize((37,32))
        self.myCircle5 = ImageTk.PhotoImage(self.resizeCircle5)

        self.rightFrame = self.rightSide()
        self.rightContent()

        self.showSign_Up()
        self.loginFrame = self.cr_LoginFrame()
        self.login_Cont()

        self.loginLabel()
        self.loginEntry()
        self.loginBut()

    def call(self):

        self.loginFrame = self.cr_LoginFrame()
        self.login_Cont()
        self.loginLabel()
        self.loginEntry()
        self.loginBut()

    def rightSide(self):

        rightFrame = tk.Frame(self.window, height = 700, width = 480, bg = "#01c79b")
        rightFrame.place(x = 500, y = 0)

        return rightFrame
    def cr_LoginFrame(self):
        login = tk.Frame (self.window, height = 700, width = 500, bg = "White")
        login.place (x = 0, y = 0)
        return login

    def cr_SignUp_Frame(self):
        signUp = tk.Frame (self.window, height = 700, width = 500, bg = "White")
        signUp.place(x = 0 , y = 0)
        signUp.pack_propagate(False)


        return signUp

    def login_Cont(self):
       

        loginLogo = tk.Label(self.loginFrame, image = self.myLoginImg, bg = "White", height = 100)
        loginLogo.place( x = 215, y = 30)

        label = tk.Label(self.loginFrame,  text = "LOGIN", fg = "Black", font = LOGIN, bg = "White")
        label.place(x = 200 , y = 140 )

    def loginLabel(self):
        username = tk.Label(self.loginFrame, text = "USERNAME", font = LOGINLABEL, bg= "white" , fg = "#6d6d6d")
        username.place(x = 60, y = 250)

        password = tk.Label(self.loginFrame, text = "PASSWORD", font = LOGINLABEL, bg= "white" , fg = "#6d6d6d")
        password.place(x = 60, y = 330)

        label1 = tk.Label (self.loginFrame, text = "Don't have an account?", font = LABEL1, bg ="White" , fg = "#818181")
        label1.place(x = 175, y = 560)  

        myFont = font.Font(family = "Segoe UI", weight = "normal", size = 11)

        label2 = tk.Button (self.loginFrame, text = "Create an account", font = LABEL2, bg ="White" , fg = "#01c79b", borderwidth = 0 ,highlightthickness = 0, command = self.showSign_Up)
        label2.place(x = 181, y = 585) 
        label2['font'] = myFont

    def loginEntry(self):

        username = tk.Entry (self.loginFrame , width = 59, relief = "flat",  highlightthickness = 1 ,borderwidth = 10)
        username.configure(highlightbackground = "#1b6392", highlightcolor = "#1b6392")
        username.place(x = 60, y = 270, height = 40)

        password = tk.Entry (self.loginFrame , show = "*", width = 59, relief = "flat",  highlightthickness = 1 ,borderwidth = 10)
        password.configure(highlightbackground = "#1b6392", highlightcolor = "#1b6392")
        password.place(x = 60, y = 350, height = 40)

    def loginBut(self):

        login = tk.Button(self.loginFrame, width = 41, height = 2, text = "LOG IN ", font = LOGINBUT, bg = "#01c79b", fg ="white",highlightthickness = 0, relief = "flat", command = self.showMain)
        login.place(x = 60, y= 430)

       
   
  
    def showSign_Up (self):
        self.cr_LoginFrame().pack_forget()
        signUp = self.cr_SignUp_Frame()
        
        loginLogo = tk.Label(signUp, image = self.myLoginImg, bg = "White", height = 100)
        loginLogo.place( x = 215, y = 30)

        label = tk.Label(signUp,  text = "SIGN UP", fg = "Black", font = LOGIN, bg = "White")
        label.place(x = 190 , y = 140 )

        lastname = tk.Label(signUp, text = "LASTNAME", font = LOGINLABEL, bg= "white" , fg = "#6d6d6d")
        lastname.place(x = 60, y = 210)

        firsname = tk.Label(signUp, text = "FIRSTNAME", font = LOGINLABEL, bg= "white" , fg = "#6d6d6d")
        firsname.place(x = 60, y = 290)

        username = tk.Label(signUp, text = "USERNAME", font = LOGINLABEL, bg= "white" , fg = "#6d6d6d")
        username.place(x = 60, y = 370)

        password = tk.Label(signUp ,text = "PASSWORD", font = LOGINLABEL, bg= "white" , fg = "#6d6d6d")
        password.place(x = 60, y = 450)

        password = tk.Label(signUp ,text = "RE-PASSWORD", font = LOGINLABEL, bg= "white" , fg = "#6d6d6d")
        password.place(x = 60, y = 530)

        lastname_Entry = tk.Entry (signUp , width = 59, relief = "flat",  highlightthickness = 1 ,borderwidth = 10)
        lastname_Entry.configure(highlightbackground = "#1b6392", highlightcolor = "#1b6392")
        lastname_Entry.place(x = 60, y = 230, height = 36)


        firstname_Entry = tk.Entry (signUp , show = "*", width = 59, relief = "flat",  highlightthickness = 1 ,borderwidth = 10)
        firstname_Entry.configure(highlightbackground = "#1b6392", highlightcolor = "#1b6392")
        firstname_Entry.place(x = 60, y = 310, height = 36)

        username_Entry = tk.Entry (signUp , width = 59, relief = "flat",  highlightthickness = 1 ,borderwidth = 10)
        username_Entry.configure(highlightbackground = "#1b6392", highlightcolor = "#1b6392")
        username_Entry.place(x = 60, y = 390, height = 36)


        pass_Entry = tk.Entry (signUp , show = "*", width = 59, relief = "flat",  highlightthickness = 1 ,borderwidth = 10)
        pass_Entry.configure(highlightbackground = "#1b6392", highlightcolor = "#1b6392")
        pass_Entry.place(x = 60, y = 470, height = 36)

        rePass_Entry = tk.Entry (signUp , width = 59, relief = "flat",  highlightthickness = 1 ,borderwidth = 10)
        rePass_Entry.configure(highlightbackground = "#1b6392", highlightcolor = "#1b6392")
        rePass_Entry.place(x = 60, y = 550, height = 36)

        loginBttn = tk.Button (signUp, width = 42, text = "Submit", font = LOGINBUT, bg = "#01c79b", fg = "White", relief = "flat", highlightthickness = 0 ,borderwidth = 0)
        loginBttn.place(x = 59, y = 620, height = 36)

        back = tk.Button (signUp, text = "BACK", font = LOGINBUT, bg = "White", fg = "#b9b9b9", relief = "flat", highlightthickness = 0 ,borderwidth = 0, command = self.call)
        back.pack(side = tk.LEFT, anchor = tk.NW, padx = 30, pady = 10)



    def rightContent(self):


        logo = tk.Label (self.rightFrame, image = self.myLogo, bg = "#01c79b")
        logo.place(x = 115 , y = 150)

        circle = tk.Label(self.rightFrame, image = self.myCircle, bg = "#01c79b")
        circle.place(x = 30, y = 40)

        circle2 = tk.Label(self.rightFrame, image = self.myCircle2, bg = "#01c79b")
        circle2.place(x = 260, y = 120)

        circle3 = tk.Label(self.rightFrame, image = self.myCircle, bg = "#01c79b")
        circle3.place(x = 400, y = -60)

       

        label = tk.Label(self. rightFrame, text = "Account Vault System", fg = "white", font = TITLE, bg = "#01c79b" )
        label.place(x = 70 , y = 380)

       

        bot = tk.Label(self.rightFrame, bg = "#01c79b", image = self.myBot)
        bot.place (x = 110, y = 490 )

        circle4 = tk.Label(self.rightFrame, image = self.myCircle4, bg = "#01c79b")
        circle4.place(x = 50, y = 500)

        circle5 = tk.Label(self.rightFrame, image = self.myCircle5, bg = "#01c79b")
        circle5.place(x = 280, y = 550)

        label2 = tk.Label (self.rightFrame, text = "Remember Everything Important", font = TAG, fg = "white" ,bg ="#01c79b" )
        label2.place(x = 95 , y = 420)

        accLogo = tk.Label(self.rightFrame, bg = "#57dec0", image =self.myAccLogo)
        accLogo.place (x = 240 , y = 650)

        accLogo2 = tk.Label(self.rightFrame, bg = "#57dec0", image =self.myAccLogo2)
        accLogo2.place (x = 300 , y = 650)

        accLogo3 = tk.Label(self.rightFrame, bg = "#57dec0", image =self.myAccLogo3)
        accLogo3.place (x = 360 , y = 650)

        accLogo4= tk.Label(self.rightFrame, bg = "#57dec0", image =self.myAccLogo4)
        accLogo4.place (x = 420 , y = 650)

    def showMain(self):
        self.window.withdraw()
        display = Main.Interface()
        

        

    def run(self):

        self.window.mainloop()




if __name__ =="__main__":

    myLogin = LogIn()
    myLogin.run()



