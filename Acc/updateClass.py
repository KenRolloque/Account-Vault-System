import tkinter as tk
import tkinter .ttk as ttk
from PIL import ImageTk, Image
import tkinter.font as font

ENTRYLABEL = ("Bahnschrift", 10)

class Update:


    def __init__(self):
      
        self.window = tk.Toplevel( width = 500, height = 750)
        self.window.resizable(False,False)
        self.window.configure(bg = "white")
        self.window.propagate(False)

        self.window.title("Update")

        width = 500
        height = 750

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))


        self.n = tk.StringVar()

        self.circle = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/Main/circle2.png")
        self.resizeCircle = self.circle.resize((100,100))
        self.myCircle = ImageTk.PhotoImage(self.resizeCircle)

        self.resizeCircle2 = self.circle.resize((50,50))
        self.myCircle2 = ImageTk.PhotoImage(self.resizeCircle2)

        self.resizeCircle3 = self.circle.resize((30,30))
        self.myCircle3 = ImageTk.PhotoImage(self.resizeCircle3)

        self.resizeCircle4 = self.circle.resize((65,65))
        self.myCircle4 = ImageTk.PhotoImage(self.resizeCircle4)

        self.resizeCircle5 = self.circle.resize((40,40))
        self.myCircle5 = ImageTk.PhotoImage(self.resizeCircle5)

        self.resizeCircle6 = self.circle.resize((20,20))
        self.myCircle6 = ImageTk.PhotoImage(self.resizeCircle6)

        self.resizeCircle7 = self.circle.resize((30,30))
        self.myCircle7 = ImageTk.PhotoImage(self.resizeCircle7)

        self.design()
        self.logo()
        self.displayLabel()
        self.displayEntry()
        self.displayButton()
        



    def logo(self):
        logo = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/logo.png")
        resizeLogo = logo.resize((140,120))
        myLogo = ImageTk.PhotoImage(resizeLogo)
        b = myLogo;

        a = tk.Label(self.window, bg = "white")
        a.config(image = b)
        a.image = b
        a.pack(side = tk.TOP, pady = (10,0))

        label = tk.Label(self.window, text = "UPDATE", fg ="#666666", bg = "white", font =("Consolas",25,"bold"))
        label.pack(side = tk.TOP)


    def displayLabel(self):
       #IDLabel = tk.Label (self.frame, text = "ID", font = ENTRYLABEL, fg = "#7e7e7e", bg = "white")
       # IDLabel.pack(side = tk.TOP, anchor = tk. W, padx = 50,pady = (20,0))
        IDLabel = tk.Label (self.window, text = "ID ", font = ENTRYLABEL, fg = "#4a4a4a", bg = "white")
        IDLabel.place(relx = .14 , rely = .3)

        accLabel = tk.Label (self.window, text = "ACCOUNT", font = ENTRYLABEL, fg = "#4a4a4a", bg = "white")
        accLabel.place(relx = .31 , rely = .3)

        username = tk.Label (self.window, text = "USERNAME", font = ENTRYLABEL, fg = "#4a4a4a", bg = "white")
        username.place(relx = .14 , rely = .4)

        email = tk.Label (self.window, text = "EMAIL", font = ENTRYLABEL, fg = "#4a4a4a", bg = "white")
        email.place(relx = .14 , rely = .5)

        password = tk.Label (self.window, text = "PASSWORD", font = ENTRYLABEL, fg = "#4a4a4a", bg = "white")
        password.place(relx = .14 , rely = .6)


        phone = tk.Label (self.window, text = "PHONE", font = ENTRYLABEL, fg = "#4a4a4a", bg = "white")
        phone.place(relx = .14 , rely = .7)

        type = tk.Label (self.window, text = "TYPE", font = ENTRYLABEL, fg = "black", bg = "white")
        type.place(relx = .14 , rely = .8)

    def displayEntry(self):

        id = tk.Entry (self.window, width = 10,relief = "flat",  highlightthickness = 1 ,borderwidth = 6, bg ="#FBFBFB")
        id.configure(highlightbackground = "#d3d3d3", highlightcolor = "#759CC9", state = tk.DISABLED)
        id.place(relx = .14 , rely = .33, height = 35)

        accEntry = tk.Entry (self.window, width = 42,relief = "flat",  highlightthickness = 1 ,borderwidth = 6, bg ="#FBFBFB")
        accEntry.configure(highlightbackground = "#d3d3d3", highlightcolor = "#759CC9")
        accEntry.place(relx = .31 , rely = .33, height = 35)

        usernameEntry = tk.Entry (self.window, width = 56,relief = "flat",  highlightthickness = 1 ,borderwidth = 6, bg ="#FBFBFB")
        usernameEntry.configure(highlightbackground = "#d3d3d3", highlightcolor = "#759CC9")
        usernameEntry.place(relx = .14 , rely = .43, height = 35)

        emailEntry = tk.Entry (self.window, width = 56,relief = "flat",  highlightthickness = 1 ,borderwidth = 6, bg ="#FBFBFB")
        emailEntry.configure(highlightbackground = "#d3d3d3", highlightcolor = "#759CC9")
        emailEntry.place(relx = .14 , rely = .53, height = 35)

        passwordEntry = tk.Entry (self.window, width = 56,relief = "flat",  highlightthickness = 1 ,borderwidth = 6, bg ="#FBFBFB")
        passwordEntry.configure(highlightbackground = "#d3d3d3", highlightcolor = "#759CC9")
        passwordEntry.place(relx = .14 , rely = .63, height = 35)

        phoneEntry = tk.Entry (self.window, width = 56,relief = "flat",  highlightthickness = 1 ,borderwidth = 6, bg ="#FBFBFB")
        phoneEntry.configure(highlightbackground = "#d3d3d3", highlightcolor = "#759CC9")
        phoneEntry.place(relx = .14 , rely = .73, height = 35)

        #typeEntry = tk.Entry (self.frame, width = 64,relief = "flat",  highlightthickness = 1 ,borderwidth = 6)
        #typeEntry.configure(highlightbackground = "green", highlightcolor = "green")


        style  = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground = "white", background="white", foreground = "black",selectforeground = "black", selectbackground = "white")
        typeList = ttk.Combobox(self.window, width = 56,height = 100, foreground = "black", background ="white", textvariable = self.n, state = "readonly")
        typeList ['values'] = ('Social Media Account','Game Account','Online/Bank Account')
        typeList.place(relx = .14 , rely = .83, height =35)
        typeList.current(0)  

    def displayButton(self):

        myFont = font.Font(family = "Coco Gothic", weight = "bold", size = 9)

        cancel = tk.Button (self.window, width = 10,height = 1,fg = "white", bg = "#128a4a", highlightthickness = 5,borderwidth = 0, text ="CANCEL", command = self.quit)
        cancel.place(relx = .68 , rely = .92)
        cancel['font'] = myFont 

        update = tk.Button (self.window, width = 10,height = 1,fg = "white", bg = "#128a4a", highlightthickness = 5,borderwidth = 0, text ="UPDATE")
        update.place(relx = .49 , rely = .92)
        update['font'] = myFont 

    def design(self):


        circle1 = tk.Label(self.window, bg = "white")
        circle1.config(image = self.myCircle)
        circle1.image = self.myCircle
        circle1.place( relx = -.07, rely = -.01)

        circle2 = tk.Label(self.window, bg = "white")
        circle2.config(image = self.myCircle2)
        circle2.image = self.myCircle2
        circle2.place( relx = 0.11, rely = 0.13)
        
        circle3 = tk.Label(self.window, bg = "white")
        circle3.config(image = self.myCircle3)
        circle3.image = self.myCircle3
        circle3.place( relx = 0.2, rely = 0.07)

        circle4 = tk.Label(self.window, bg = "white")
        circle4.config(image = self.myCircle)
        circle4.image = self.myCircle
        circle4.place( relx = .85, rely = .13)

        circle5 = tk.Label(self.window, bg = "white")
        circle5.config(image = self.myCircle4)
        circle5.image = self.myCircle4
        circle5.place( relx = .7, rely = .09)

        circle6 = tk.Label(self.window, bg = "white")
        circle6.config(image = self.myCircle5)
        circle6.image = self.myCircle5
        circle6.place(  relx = .84, rely = .04)

        circle6 = tk.Label(self.window, bg = "white")
        circle6.config(image = self.myCircle4)
        circle6.image = self.myCircle4
        circle6.place(  relx = -.03, rely = .87)

        circle7 = tk.Label(self.window, bg = "white")
        circle7.config(image = self.myCircle6)
        circle7.image = self.myCircle6
        circle7.place(  relx = .18, rely = .93)

        circle8 = tk.Label(self.window, bg = "white")
        circle8.config(image = self.myCircle7)
        circle8.image = self.myCircle7
        circle8.place(  relx = .27, rely = .89)

        circle9 = tk.Label(self.window, bg = "white")
        circle9.config(image = self.myCircle6)
        circle9.image = self.myCircle6
        circle9.place( relx = .37, rely = .93)

    def quit(self):
        self.window.withdraw()
    def run(self):

        self.window.mainloop()





