import tkinter as tk
import tkinter .ttk as ttk
from PIL import ImageTk, Image
import tkinter.font as font


import updateClass
import updateProfile
import Login

LOGO = ("Consolas", 18, "bold")
ADMIN = ("Verdana", 11, "bold")

LABEL = ("Coco Gothic", 10,)
COUNT = ("Verdana", 50,"bold")

ENTRYLABEL = ("Bahnschrift", 10,"bold")




class Interface:

    def __init__(self):
        
        self.window = tk.Tk()
        self.window.geometry("1500x1000")
        self.window.resizable(False, False)
        self.window.withdraw()

        
        self.interface = self.createWindow()
        self.display = self.mainFrame()
        self.n = tk.StringVar()
        
        #Circles

        self.circle = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/circle.png")
        self.resizeCircle = self.circle.resize((90,90))
        self.myCircle = ImageTk.PhotoImage(self.resizeCircle)

        self.resizeCircle2 = self.circle.resize((30,30))
        self.myCircle2 = ImageTk.PhotoImage(self.resizeCircle2)

        self.resizeCircle3 = self.circle.resize((45,45))
        self.myCircle3 = ImageTk.PhotoImage(self.resizeCircle3)

        self.resizeCircle4 = self.circle.resize((130,130))
        self.myCircle4 = ImageTk.PhotoImage(self.resizeCircle4)

        self.resizeCircle5 = self.circle.resize((80,80))
        self.myCircle5 = ImageTk.PhotoImage(self.resizeCircle5)

        #Images
        self.logout = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/icons8-log-out-64.png")
        self.resize_Logout = self.logout.resize((30,30), Image.ANTIALIAS)
        self.myLogout = ImageTk.PhotoImage(self.resize_Logout)

        self.logo = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/logo.png")
        self.resizeLogo = self.logo.resize((100,80), Image.ANTIALIAS)
        self.myLogo = ImageTk.PhotoImage(self.resizeLogo)

        self.adminLogo = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/icons8-test-account-40.png")
        self.myAdmin = ImageTk.PhotoImage(self.adminLogo)

        self.icon1 = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/logo1.png")
        self.myIcon = ImageTk.PhotoImage(self.icon1)

        self.icon2 = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/logo2.png")
        self.myIcon2 = ImageTk.PhotoImage(self.icon2)

        self.icon3 = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/logo3.png")
        self.myIcon3 = ImageTk.PhotoImage(self.icon3)

        self.icon4 = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/logo4.png")
        self.myIcon4 = ImageTk.PhotoImage(self.icon4)

        self.deleteLogo = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/icons8-delete-96.png")
        self.resizeDel = self.deleteLogo.resize((20,20), Image.ANTIALIAS)
        self.myDel = ImageTk.PhotoImage(self.resizeDel)

        self.updateLogo = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/icons8-edit-50.png")
        self.resizeUp = self.updateLogo.resize((20,20), Image.ANTIALIAS)
        self.myUp = ImageTk.PhotoImage(self.resizeUp)


        self.frame1 = self.createFrame1()
        self.frame2 = self.createFrame2()
        self.frame3 = self.createFrame3()
        
        self.frame1Content()
        self.design() 
        self.sqr1 , self.sqr2 ,self.sqr3, self.sqr4 = self.frame2Content()
        self.panel1 , self.panel2 =  self.frame3Content()
        
        self.sqrContent()

        self.panel1Content()

        self.allBut, self. butGame, self.butBank, self.butSoc = self.panel2Content()

        self.showAll()
        self.modifyButton()
        self.runWindow()

    def createWindow (self):

        self.crWindow = tk.Toplevel(height = 1000, width = 1510)
        self.crWindow.resizable(False,False)
        self.crWindow.pack_propagate(False)

        self.crWindow.title("Accout Vault System")
        return  self.crWindow

    def mainFrame(self):

        frame = tk.Frame (self.interface, height = 1000, width = 1510, bg ="red")
        frame.place(x = 1, y =1)
        return frame

   
    def createFrame1 (self):
        
        frame1 = tk.Frame(self.display, height = 80 , width = 1510, bg = "#01c79b")
        frame1.pack(fill = 'both',expand =True, side = tk.TOP)        
        return frame1
        
        

    def createFrame2 (self):

        frame2 = tk.Frame(self.display, height = 200,width = 1510, bg = "white")
        frame2.pack(fill = 'both',expand =True, side = tk.TOP)
        frame2.pack_propagate(False)
        return frame2

    def createFrame3 (self):

        frame3 = tk.Frame(self.display, height = 530,width = 1510, bg = "red")
        frame3.pack(fill = 'x')
        frame3.pack_propagate(False)
        return frame3

    def frame1Content (self):

        logo = tk.Label(self.frame1, image = self.myLogo, bg = "#01c79b")
        logo.pack(side = tk.LEFT, padx = (50,0))

        label = tk.Label(self.frame1, bg ="#01c79b",  text = " Account Vault System", fg = "White",font = LOGO)
        label.pack(side = tk.LEFT )


        logout_button = tk.Button(self.frame1, image =self.myLogout, bg = "#01c79b",borderwidth = 0, command = self.backto_Login)
        logout_button.pack(side = tk.RIGHT, padx = (0, 30))

        admin_button = tk.Button(self.frame1, image =self.myAdmin, bg = "#01c79b",borderwidth = 0, command = self.showProfile)
        admin_button.pack(side = tk.RIGHT, padx = (10, 10))

        username = tk.Label(self.frame1, bg ="#01c79b", text = "Administrator", fg = "white", font = ADMIN )
        username.pack(side = tk.RIGHT)
   
    def frame2Content (self):



        square1 = tk.Frame(self.frame2, bg = "#d62828", height = 131, width = 171)
        square1.pack(side = tk.LEFT, padx = (270,90))
        square1.pack_propagate(False)

        square2 = tk.Frame(self.frame2, bg = "#f77f00", height = 131, width = 171)
        square2.pack(side = tk.LEFT, padx = (0,90))
  
        square3 = tk.Frame(self.frame2, bg = "#fcbf49", height = 131, width = 171)
        square3.pack(side = tk.LEFT, padx = (0,90))

        square4 = tk.Frame(self.frame2, bg = "#eae2b7", height = 131, width = 171)
        square4.pack(side = tk.LEFT, padx = (0,90))

        return square1,square2,square3,square4

    def sqrContent (self):

    #1
        icon = tk.Label(self.sqr1, image = self.myIcon , bg = "#d62828")
        icon.place(relx = 1.0, rely = 1.0, anchor = tk.SE)
        
        label1 = tk.Label(self.sqr1, text =  "TOTAL ACCOUNT", fg = "White", bg ="#d62828" , font = LABEL)
        label1.place(relx = .25 , rely = 0.08)

        count1 = tk.Label(self.sqr1, text = "10", fg = "white", font = COUNT,  bg ="#d62828")
        count1.place(relx = .15, rely = .24)

    #2
        icon2 = tk.Label(self.sqr2, image = self.myIcon2 , bg = "#f77f00")
        icon2.place(relx = 1.0, rely = 1.0, anchor = tk.SE)

        label2 = tk.Label(self.sqr2, text =  "GAME ACCOUNT", fg = "White", bg ="#f77f00" , font = LABEL)
        label2.place(relx = .25 , rely = 0.08)

        count2 = tk.Label(self.sqr2, text = "14", fg = "white", font = COUNT,  bg ="#f77f00")
        count2.place(relx = .15, rely = .24)

    #3

        count3 = tk.Label(self.sqr3, text = "14", fg = "#434444", font = COUNT,  bg ="#fcbf49")
        count3.place(relx = .15, rely = .24)

        icon3 = tk.Label(self.sqr3, image = self.myIcon3 , bg = "#fcbf49")
        icon3.place(relx = 1.0, rely = 1.0, anchor = tk.SE)

        label3 = tk.Label(self.sqr3, text =  "BANK ACCOUNT", fg = "#434444", bg ="#fcbf49" , font = LABEL)
        label3.place(relx = .25 , rely = 0.08)



        count4 = tk.Label(self.sqr4, text = "14", fg = "#434444", font = COUNT,  bg ="#eae2b7")
        count4.place(relx = .15, rely = .24)

        icon4 = tk.Label(self.sqr4, image = self.myIcon4 , bg = "#eae2b7")
        icon4.place(relx = 1.1, rely = 1.0, anchor = tk.SE)

        label4 = tk.Label(self.sqr4, text =  "SOCMED ACCOUNT", fg = "#434444", bg ="#eae2b7" , font = LABEL)
        label4.place(relx = .15 , rely = 0.08)

    def frame3Content(self):

        frame1 = tk.Frame(self.frame3, width = 450, height = 530, bg = "white")
        frame1.pack( side = tk.LEFT)
        frame1.pack_propagate(False)

        frame2 = tk.Frame(self.frame3, width = 1150 , height = 530, bg = "white")
        frame2.pack( side = tk.LEFT)
        frame2.pack_propagate(False)
        return frame1, frame2

    def panel1Content(self):
        
        account = tk.Label (self.panel1, text = "ACCOUNT", font = ENTRYLABEL,  fg = "#7e7e7e", bg = "white")
        account.pack(side = tk.TOP, anchor = tk.NW, padx = 50)

        accEntry = tk.Entry (self.panel1, width = 50,relief = "flat",  highlightthickness = 1 ,borderwidth = 6)
        accEntry.configure(highlightbackground = "green", highlightcolor = "green")
        accEntry.pack(side = tk.TOP, anchor = tk.NW, padx = 50, pady = (0, 20))

        username = tk.Label (self.panel1, text = "USERNAME", font = ENTRYLABEL,  fg = "#7e7e7e", bg = "white")
        username.pack(side = tk.TOP, anchor = tk.NW, padx = 50)

        usernameEntry = tk.Entry (self.panel1, width = 50,relief = "flat",  highlightthickness = 1 ,borderwidth = 6)
        usernameEntry.configure(highlightbackground = "green", highlightcolor = "green")
        usernameEntry.pack(side = tk.TOP, anchor = tk.NW, padx = 50, pady = (0, 20))

        email = tk.Label (self.panel1, text = "EMAIL", font = ENTRYLABEL,  fg = "#7e7e7e", bg = "white")
        email.pack(side = tk.TOP, anchor = tk.NW, padx = 50)

        emailEntry = tk.Entry (self.panel1, width = 50,relief = "flat",  highlightthickness = 1 ,borderwidth = 6)
        emailEntry.configure(highlightbackground = "green", highlightcolor = "green")
        emailEntry.pack(side = tk.TOP, anchor = tk.NW, padx = 50, pady = (0, 20))

        password = tk.Label (self.panel1, text = "PASSWORD / PIN CODE", font = ENTRYLABEL,  fg = "#7e7e7e", bg = "white")
        password.pack(side = tk.TOP, anchor = tk.NW, padx = 50)

        passwordEntry = tk.Entry (self.panel1, width = 50,relief = "flat",  highlightthickness = 1 ,borderwidth = 6)
        passwordEntry.configure(highlightbackground = "green", highlightcolor = "green")
        passwordEntry.pack(side = tk.TOP, anchor = tk.NW, padx = 50, pady = (0, 20))

        phone = tk.Label (self.panel1, text = "PHONE NUMBER", font = ENTRYLABEL,  fg = "#7e7e7e", bg = "white")
        phone.pack(side = tk.TOP, anchor = tk.NW, padx = 50)

        phoneEntry = tk.Entry (self.panel1, width = 50,relief = "flat",  highlightthickness = 1 ,borderwidth = 6)
        phoneEntry.configure(highlightbackground = "green", highlightcolor = "green")
        phoneEntry.pack(side = tk.TOP, anchor = tk.NW, padx = 50, pady = (0, 20))

        type = tk.Label (self.panel1, text = "TYPE", font = ENTRYLABEL,  fg = "#7e7e7e", bg = "white")
        type.pack(side = tk.TOP, anchor = tk.NW, padx = 50)


        style  = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground = "white", background="white", foreground = "black",selectforeground = "black", selectbackground = "white")
        typeList = ttk.Combobox(self.panel1, width = 49,height = 100, foreground = "black", background ="white", textvariable = self.n, state = "readonly")
        typeList ['values'] = ('Social Media Account','Game Account','Online/Bank Account')
        typeList.place(relx = .11, rely = .73, height = 35)
        typeList.current(0)       

        myFont = font.Font(family = "Coco Gothic", weight = "bold", size = 9)

        clearBttn = tk.Button (self.panel1, width = 10,height = 1,fg = "white", bg = "#128a4a", highlightthickness = 5,borderwidth = 0, text ="CLEAR")
        clearBttn.pack(side = tk.RIGHT, padx = (0,85), pady = (0,5))
        clearBttn['font'] = myFont

        addBttn = tk.Button (self.panel1, width = 10, height = 1,fg = "white", bg = "#128a4a",highlightthickness = 5,borderwidth = 0, text ="ADD")
        addBttn.pack(side = tk.RIGHT, padx = (0,20), pady = (0,5))
        addBttn['font'] = myFont

    def panel2Content(self):
            myFont = font.Font(family = "Coco Gothic", weight = "bold", size = 10)

            all = tk.Button(self.panel2, width = 10 ,bg = "white", fg ="#808080", text = "ALL", highlightthickness = 0,borderwidth = 0, command = self.showAll)
            all.pack(side = tk.LEFT, anchor = tk.NW, padx = (0,20))
            all['font'] = myFont

            game = tk.Button(self.panel2, width = 10 ,bg = "white", fg ="#808080", text = "GAME", highlightthickness = 0,borderwidth = 0, command = self.showGame_Frame)
            game.pack(side = tk.LEFT, anchor = tk.NW, padx = (0,20))
            game['font'] = myFont

            bank = tk.Button(self.panel2, width = 10 ,bg = "white", fg ="#808080",  text = "BANK", highlightthickness = 0,borderwidth = 0, command = self.showBank_Frame)
            bank.pack(side = tk.LEFT, anchor = tk.NW)
            bank['font'] = myFont

            socmed = tk.Button(self.panel2, width = 15 ,bg = "white", fg ="#808080",  text = "SOCIAL MEDIA", highlightthickness = 0,borderwidth = 0, command = self.showSoc_Frame)
            socmed.pack(side = tk.LEFT, anchor = tk.NW, padx = 20)
            socmed['font'] = myFont

            return all, game, bank, socmed
    
    def showAll(self):
            self.allBut.config(bg = "#F2DFA2")
            self.butGame.config(bg = "white")
            self.butBank.config(bg = "white")
            self.butSoc.config(bg = "white")
            tableFrame = tk.Frame(self.panel2, width = 970, height = 500,borderwidth = 0)

            tableFrame.place (relx = 0 , rely = .06)

            style = ttk.Style(tableFrame)
            style.theme_use("clam")
            style.configure("Treeview", background = "White", fieldbackground = "White", rowheight = 30, )
        
            style2 = ttk.Style(tableFrame)
            style2.theme_use("clam")
            style2.configure("Treeview.Heading", background = "#c8faf6", fieldbackground = "White", font = ("Arial",10,"bold"), borderwidth = 0, highlightthickness = 0)
            style2.map('Treeview.Heading', background = [('selected','#0a5b9c')])

            self.table = ttk.Treeview(tableFrame, height = 14)
            self.table['columns'] = ('ID', 'Account','Account Name','Email','Password','Phone','Type')
        
            self.table.column('#0',width = 0, stretch=False)
            self.table.column('ID', anchor = tk.CENTER, width = 70)
            self.table.column('Account', anchor = tk.W, width = 130)
            self.table.column('Account Name', anchor = tk.W, width = 170)
            self.table.column('Email', anchor = tk.W, width = 170)
            self.table.column('Password', anchor = tk.W, width = 170)
            self.table.column('Phone', anchor = tk.W, width = 150)
            self.table.column('Type', anchor = tk.W, width = 140)

            self.table.heading('ID', text ='ID', anchor =tk.CENTER )
            self.table.heading('Account', text ='Account', anchor =tk.CENTER)
            self.table.heading('Account Name', text ='Account Name', anchor =tk.CENTER)
            self.table.heading('Email', text ='Email', anchor =tk.CENTER)
            self.table.heading('Password', text ='Password', anchor =tk.CENTER)
            self.table.heading('Phone', text ='Phone', anchor =tk.CENTER)
            self.table.heading('Type', text ='Type', anchor =tk.CENTER)

            self.table.pack()

            return tableFrame
    def showGame_Frame(self):

            self.allBut.config(bg = "white")
            self.butGame.config(bg = "#F2DFA2")
            self.butBank.config(bg = "white")
            self.butSoc.config(bg = "white")
            tableFrame = tk.Frame(self.panel2, width = 970, height = 500 )

            tableFrame.place (relx = 0 , rely = .06)

            style = ttk.Style(tableFrame)
            style.theme_use("clam")
            style.configure("Treeview", background = "White", fieldbackground = "White", rowheight = 30)
        
            style2 = ttk.Style(tableFrame)
            style2.theme_use("clam")
            style2.configure("Treeview.Heading", background = "#c8faf6", fieldbackground = "White", font = ("Arial",10,"bold"), borderwidth = 0, highlightthickness = 0)       
            style2.map('Treeview.Heading', background = [('selected','#0a5b9c')])

            self.table = ttk.Treeview(tableFrame, height = 14)
            self.table['columns'] = ('ID', 'Account','Account Name','Email','Password','Phone','Type')
        
            self.table.column('#0',width = 0, stretch=False)
            self.table.column('ID', anchor = tk.CENTER, width = 70)
            self.table.column('Account', anchor = tk.W, width = 130)
            self.table.column('Account Name', anchor = tk.W, width = 170)
            self.table.column('Email', anchor = tk.W, width = 170)
            self.table.column('Password', anchor = tk.W, width = 170)
            self.table.column('Phone', anchor = tk.W, width = 150)
            self.table.column('Type', anchor = tk.W, width = 140)

            self.table.heading('ID', text ='ID', anchor =tk.CENTER )
            self.table.heading('Account', text ='Account', anchor =tk.CENTER)
            self.table.heading('Account Name', text ='Account Name', anchor =tk.CENTER)
            self.table.heading('Email', text ='Email', anchor =tk.CENTER)
            self.table.heading('Password', text ='Password', anchor =tk.CENTER)
            self.table.heading('Phone', text ='Phone', anchor =tk.CENTER)
            self.table.heading('Type', text ='Type', anchor =tk.CENTER)

            self.table.pack()

            return tableFrame


    def showBank_Frame(self):
            self.allBut.config(bg = "white")
            self.butGame.config(bg = "white")
            self.butBank.config(bg = "#F2DFA2")
            self.butSoc.config(bg = "white")
            tableFrame = tk.Frame(self.panel2, width = 970, height = 500 )

            tableFrame.place (relx = 0 , rely = .06)


            style = ttk.Style(tableFrame)
            style.theme_use("clam")
            style.configure("Treeview", background = "White", fieldbackground = "White", rowheight = 30)
        
            style2 = ttk.Style(tableFrame)
            style2.theme_use("clam")
            style2.configure("Treeview.Heading", background = "#c8faf6", fieldbackground = "White", font = ("Arial",10,"bold"), borderwidth = 0, highlightthickness = 0)      
      
            style2.map('Treeview.Heading', background = [('selected','#0a5b9c')])

            self.table = ttk.Treeview(tableFrame, height = 14)
            self.table['columns'] = ('ID', 'Account','Account Name','Email','Password','Phone','Type')
        
            self.table.column('#0',width = 0, stretch=False)
            self.table.column('ID', anchor = tk.CENTER, width = 70)
            self.table.column('Account', anchor = tk.W, width = 130)
            self.table.column('Account Name', anchor = tk.W, width = 170)
            self.table.column('Email', anchor = tk.W, width = 170)
            self.table.column('Password', anchor = tk.W, width = 170)
            self.table.column('Phone', anchor = tk.W, width = 150)
            self.table.column('Type', anchor = tk.W, width = 140)

            self.table.heading('ID', text ='ID', anchor =tk.CENTER )
            self.table.heading('Account', text ='Account', anchor =tk.CENTER)
            self.table.heading('Account Name', text ='Account Name', anchor =tk.CENTER)
            self.table.heading('Email', text ='Email', anchor =tk.CENTER)
            self.table.heading('Password', text ='Password', anchor =tk.CENTER)
            self.table.heading('Phone', text ='Phone', anchor =tk.CENTER)
            self.table.heading('Type', text ='Type', anchor =tk.CENTER)

            self.table.pack()

            return tableFrame

    def showSoc_Frame(self):

            self.allBut.config(bg = "white")
            self.butGame.config(bg = "white")
            self.butBank.config(bg = "white")
            self.butSoc.config(bg = "#F2DFA2")

            tableFrame = tk.Frame(self.panel2, width = 970, height = 500 )
            tableFrame.place (relx = 0 , rely = .06)


            style = ttk.Style(tableFrame)
            style.theme_use("clam")
            style.configure("Treeview", background = "White", fieldbackground = "White", rowheight = 30)
        
            style2 = ttk.Style(tableFrame)
            style2.theme_use("clam")
            style2.configure("Treeview.Heading", background = "#c8faf6", fieldbackground = "White", font = ("Arial",10,"bold"), borderwidth = 0, highlightthickness = 0)

            style2.map('Treeview.Heading', background = [('selected','#0a5b9c')])

            self.table = ttk.Treeview(tableFrame, height = 14)
            self.table['columns'] = ('ID', 'Account','Account Name','Email','Password','Phone','Type')
        
            self.table.column('#0',width = 0, stretch=False)
            self.table.column('ID', anchor = tk.CENTER, width = 70)
            self.table.column('Account', anchor = tk.W, width = 130)
            self.table.column('Account Name', anchor = tk.W, width = 170)
            self.table.column('Email', anchor = tk.W, width = 170)
            self.table.column('Password', anchor = tk.W, width = 170)
            self.table.column('Phone', anchor = tk.W, width = 150)
            self.table.column('Type', anchor = tk.W, width = 140)

            self.table.heading('ID', text ='ID', anchor =tk.CENTER )
            self.table.heading('Account', text ='Account', anchor =tk.CENTER)
            self.table.heading('Account Name', text ='Account Name', anchor =tk.CENTER)
            self.table.heading('Email', text ='Email', anchor =tk.CENTER)
            self.table.heading('Password', text ='Password', anchor =tk.CENTER)
            self.table.heading('Phone', text ='Phone', anchor =tk.CENTER)
            self.table.heading('Type', text ='Type', anchor =tk.CENTER)

            self.table.pack()

            return tableFrame
   

    
    def hideGame(self):
       game = self.showGame_Frame()
       game.place_forget()

    def hideBank(self):
        bank = self.showBank_Frame()
        bank.place_forget()

    def hideSoc(self):

        socmed = self.showSoc_Frame()
        socmed.place_forget()

    def hideAll(self):

        all = self.showAll()
        all.place_forget()

    def modifyButton (self):

        delete = tk.Button(self.panel2,width = 30, height =30, text ="button 1", image = self.myDel, bg = "white", highlightthickness = 0, borderwidth = 0)
        delete.place(relx = .92, rely = 0)

        edit = tk.Button(self.panel2,width = 30, height =30, text ="button 1", image = self.myUp, bg = "white", highlightthickness = 0, borderwidth = 0, command = self.showUpdate_Frame)
        edit.place(relx = .88, rely = 0)

    def showUpdate_Frame(self):


        show = updateClass.Update()

    def design(self):

        label = tk.Label(self.frame2, image = self.myCircle, bg= "White")
        label.place(relx = -.03 , rely = .14)

        label2 = tk.Label(self.frame2, image = self.myCircle2, bg= "White")
        label2.place(relx = .08 , rely = .25)

        label3 = tk.Label(self.frame2, image = self.myCircle3, bg= "White")
        label3.place(relx = .11 , rely = .5)

        label4 = tk.Label(self.frame2, image = self.myCircle4, bg= "White")
        label4.place(relx = .28 , rely = .03)

        label4 = tk.Label(self.frame2, image = self.myCircle4, bg= "White")
        label4.place(relx = .62 , rely = .35)

        label5 = tk.Label(self.frame2, image = self.myCircle5, bg= "White")
        label5.place(relx = .85 , rely = .1)

        label5 = tk.Label(self.frame2, image = self.myCircle3, bg= "White")
        label5.place(relx = .89 , rely = .57)

        label6 = tk.Label(self.frame2, image = self.myCircle2, bg= "White")
        label6.place(relx = .93 , rely = .2)


    def showProfile(self):

        show = updateProfile.updateUser()

    def backto_Login(self):

        self.interface.withdraw()
        show = Login.LogIn()
        



    def runWindow (self):
        self.window.mainloop()
        self.interface.mainloop()



if __name__ == "__main__":

    myMain = Interface()
    myMain.runWindow()


