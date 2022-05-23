
import tkinter as tk
import tkinter .ttk as ttk
from PIL import ImageTk, Image
import tkinter.font as font



LABEL = ("Bahnschrift",10)


class updateUser:

    def __init__(self):

        self.main = tk.Tk()
        self.main.withdraw()
        self.window = tk.Toplevel(width = 500, height = 700, bg ="white")
        self.window.resizable(False,False)
        self.window.propagate(False)
        self.window.title("Profile")

        width = 500
        height = 700

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))


        self.loginImg = Image.open("D:/Administrator/Files/BSU/2ND YEAR/2nd Sem/ADBMS/PROJECYT/Acc/Image/icons8-male-user-100.png")
        self.resizeLogin = self.loginImg.resize((110,110))
        self.myLoginImg = ImageTk.PhotoImage(self.resizeLogin)

        self.logo()
        self.entries()
        self.button()
    
    def logo(self):

        logo = tk.Label(self.window, bg = "white")
        logo.config(image = self.myLoginImg)
        logo.image = self.myLoginImg
        logo.pack(pady = (30,0))

        fullname = tk.Label(self.window, text = "KEN MARK ROLLOQUE", fg = "#272727", bg = "white", font = ("Bahnschrift",18))
        fullname.pack(pady = 15)


    def entries(self):

        username = tk.Label(self.window, text ="USERNAME", font = LABEL, fg ="#6d6d6d", bg = "white")
        username.place (relx = .13, rely = .33)

        usernameEntry = tk.Entry(self.window, width =59, bg = "#e6e6e6", relief = "flat" , borderwidth =6 , highlightthickness = 1)
        usernameEntry.configure(highlightbackground = "#e6e6e6", highlightcolor = "#759CC9", state = tk.DISABLED)
        usernameEntry.place (relx = .13, rely = .36, height = 35)

        firstname = tk.Label(self.window, text ="FIRSTNAME", font = LABEL, fg ="#6d6d6d", bg = "white")
        firstname.place (relx = .13, rely = .44)

        firstnameEntry = tk.Entry(self.window, width =59, bg = "#e6e6e6", relief = "flat" , borderwidth =6 , highlightthickness = 1)
        firstnameEntry.configure(highlightbackground = "#e6e6e6", highlightcolor = "#759CC9", state = tk.DISABLED)
        firstnameEntry.place (relx = .13, rely = .47, height = 35)

        lastname = tk.Label(self.window, text ="LASTNAME", font = LABEL, fg ="#6d6d6d", bg = "white")
        lastname.place (relx = .13, rely = .55)

        lastnameEntry = tk.Entry(self.window, width =59, bg = "#e6e6e6", relief = "flat" , borderwidth =6 , highlightthickness = 1)
        lastnameEntry.configure(highlightbackground = "#e6e6e6", highlightcolor = "#759CC9", state = tk.DISABLED)
        lastnameEntry.place (relx = .13, rely = .58, height = 35)

        password = tk.Label(self.window, text ="PASSWORD", font = LABEL, fg ="#6d6d6d", bg = "white")
        password.place (relx = .13, rely = .66)

        passwordEntry = tk.Entry(self.window,show = "*",width =59, bg = "#e6e6e6", relief = "flat" , borderwidth =6 , highlightthickness = 1)
        passwordEntry.configure(highlightbackground = "#e6e6e6", highlightcolor = "#759CC9", state = tk.DISABLED)
        passwordEntry.place (relx = .13, rely = .69, height = 35)

        return usernameEntry, firstnameEntry,lastnameEntry,passwordEntry
        
    def button(self):
        myFont = font.Font(family = "Coco Gothic", weight = "bold", size = 9)

        edit = tk.Button (self.window, width = 10,height = 1,fg = "white", bg = "#128a4a", highlightthickness = 5,borderwidth = 0, text ="EDIT", command = self.process)
        edit.place(relx = .7 , rely = .78)
        edit['font'] = myFont 

        save = tk.Button (self.window, state = tk.DISABLED, width = 10,height = 1,fg = "white", bg = "#128a4a", highlightthickness = 5,borderwidth = 0, text ="SAVE")
        save.place(relx = .5 , rely = .78)
        save['font'] = myFont 

        return edit


    def edit (self):   
        
        deactEdit = self.button()
        deactEdit.config(state = tk.DISABLED)

        screen = tk.Toplevel(self.window,height = 200, width = 400, bg ="white")

        screen.resizable(False,False)
        screen.propagate(False)
        screen.protocol("WM_DELETE_WINDOW", self.exit)
        screen.title("Confirm Password")
        width = 400
        height = 200

        screen_width = screen.winfo_screenwidth()
        screen_height = screen.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        screen.geometry('%dx%d+%d+%d' % (width, height, x, y))

        return screen

    def process(self):

        showWindow = self.edit()

        password = tk.Label(showWindow, text = "Confirm Password", bg = "white")
        password.place(relx = .1 ,rely = .37)

        confirmPassword = tk.Entry (showWindow, width =30,relief= "flat", borderwidth = 6, highlightthickness = 1,bg = "white")
        confirmPassword.configure(highlightbackground = "#759CC9", highlightcolor = "#759CC9")
        confirmPassword.place (relx = .38, rely = .32,height = 38)

        myFont = font.Font(family = "Coco Gothic", weight = "bold", size = 9)
        submit = tk.Button (showWindow, width = 10,height = 1,fg = "white", bg = "#128a4a", highlightthickness = 5,borderwidth = 0, text ="SAVE")
        submit.place(relx = .7 , rely = .7)
        submit['font'] = myFont
   
    def newWindow(self):

        show = confirmPass.Password()

    def run(self):

        self.window.mainloop()


    def exit(self):
        self.window.destroy()

