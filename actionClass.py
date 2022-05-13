import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import myMain

addPanelBG = "#032139"
contentPanelBG = "#002645"
ADDCOLOR = "#adadad"
TAGNAME = ("Lucida Handwriting", 10, "bold")
ADDLABEL = ("Arial", 9 , "bold")
#BUTTONLABEL = ("Arial", 9, ")
ENTRYFONT = ("Arial", 9 )
ADMINFONT = ("Sitka Text", 10, "bold")
SQUARELABEL = ("Verdana", 10, "bold")
COUNTLABEL = ("Verdana", 36, "bold")
class Action:

    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("400x580")
        self.window.resizable(False, False)
        self.window.title("Update");
        self.window.config(bg = "#032139")
        
        self.myList =tk.StringVar()
        #self.createAddLabel()
        self.id= tk.StringVar()
        self.type = tk.StringVar()
        self.hold = ""
        #self.createEntry()
        self.list= ["Social Media Account","Game Account","Online/Bank Account"]
        self.index = 0
        self.createAddLabel() 
        self.createEntry()
        #self.createCombo_type()
        self.createButtons()
     


        
        self.values =""

        

    def setValue(self, value):

        try:
            self.values = value
            #self.idEntry.insert(0, self.values[0])
            self.id = self.values[0]
            self.acc.insert(0, self.values[1])
            self.accountEntry.insert(0, self.values[2])
            self.emailEntry.insert(0, self.values[3])
            self.passwordEntry.insert(0, self.values[4])
            self.phoneEntry.insert(0, self.values[5])
            #self.typeList.set(self.values[6])
           #self.x = 
            #print(self.values[6],"x")
            if self.values[6] == "Social Media Account":
            
                self.index = 0
                self.hold = self.list[self.index]
                self.type = self.hold

            elif self.values[6] == "Game Account":
                self.index = 1
                self.hold = self.list[self.index]
                self.type = self.hold

            elif self.values[6] == "Online/Bank Account":
                self.index = 2
                self.hold = self.list[self.index]
                self.type = self.hold

            print("index",self.type)
            self.displayIdEntry()
            self.createCombo_type()

        except Exception as e:

            MessageBox.showerror("Show error","Please select an item")
            self.window.destroy()
        
    def createAddLabel(self):

        id = tk.Label(self.window, text = "ID" , font =ADDLABEL, bg = addPanelBG, fg = ADDCOLOR )
        id.place(x = 35, y =45)

        account = tk.Label(self.window, text = "Account" , font =ADDLABEL, bg = addPanelBG, fg = ADDCOLOR )
        account.place(x = 150, y =45)

        accountName = tk.Label(self.window, text = "Account Name", font =ADDLABEL, bg = addPanelBG, fg = ADDCOLOR)
        accountName.place (x = 35, y = 120)

        email = tk.Label(self.window, text = "Email", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        email.place(x = 35, y = 195)

        password = tk.Label(self.window, text = "Password / Pin Code", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        password.place(x = 35, y = 270)

        phoneNumber = tk.Label(self.window, text = "Phone Number", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        phoneNumber.place(x = 35, y = 345)

        type = tk.Label(self.window, text = "Type", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        type.place(x = 35, y = 420)

    def displayIdEntry(self):
        self.idEntry = tk.Label(self.window, bg ="#01345e" , text = self.id , font =ENTRYFONT,width = 12, borderwidth = 10, highlightthickness = 0 ,fg ="White", relief = "flat", anchor = tk.W)
        #self.idEntry.config(disabledbackground = "#01345e")

        self.idEntry.place(x = 35, y = 70, height = 35)

    def createEntry(self):

        

        self.acc = tk.Entry(self.window, bg ="#01345e", font =ENTRYFONT,width = 28, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.acc.place(x = 150, y = 70, height = 35)

        self.accountEntry = tk.Entry(self.window, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.accountEntry.place(x = 35, y = 145, height = 35)

        self.emailEntry = tk.Entry(self.window, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.emailEntry.place(x = 35, y = 220, height = 35)

        self.passwordEntry= tk.Entry(self.window,bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.passwordEntry.place(x = 35, y = 295, height = 35)

        self.phoneEntry = tk.Entry(self.window, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.phoneEntry.place(x = 35, y = 370, height = 35)

    def createCombo_type(self):

        
        self.style  = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", fieldbackground = "#01345e")
        self.typeList = ttk.Combobox(self.window, width = 51,foreground = "black", background ="#01345e", textvariable = self.myList)
        self.typeList ['values'] = ('Social Media Account','Game Account','Online/Bank Account')
        
        self.typeList ['state'] = 'readonly'
        self.typeList.set(self.hold)
        self.typeList.current()
        self.typeList.place(x = 36, y = 445, height = 35)
        print(self.type,"n")

    def createButtons(self):

        updateButton = tk.Button(self.window, text = "Update", font =ADDLABEL, bg ="#017779", fg ="White", borderwidth = 0, highlightthickness = 0, relief = "flat", command = self.updateData)
        updateButton.place(x = 180, y =520, height = 30, width = 80)

        cancelButton = tk.Button(self.window, text = "Cancel", font =ADDLABEL, bg ="#017779", fg ="White", borderwidth = 0, highlightthickness = 0, relief = "flat", command = self.quit)
        cancelButton.place(x = 280, y =520, height = 30, width = 80)


    def updateData(self):
        updateID = self.id
        updateAcc = self.acc.get()
        updateName = self.accountEntry.get()
        updateEmail = self.emailEntry.get()
        updatePass = self.passwordEntry.get()
        updatePhone = self.phoneEntry.get()
        updateType = self.typeList.get()

        if (updateAcc =="" or updateName == "" or updateEmail==  ""or updatePass == ""or updatePhone == "" ):
            MessageBox.showerror("Error","Please Complete the Following Form")
        
        else:

            connect = mysql.connect(
                    host = "localhost", 
                    username = "root",
                    port ="3306", 
                    password="", 
                    database = "accountstorage",
                
                    )
            cursor = connect.cursor()
            sql = "UPDATE table1 SET account = %s,accountname = %s,email = %s,password = %s,contact = %s,type = %s WHERE id = %s"
            val = (updateAcc,updateName,updateEmail,updatePass,updatePhone,updateType,updateID)
            cursor.execute(sql,val)
            #print (updateType,"1")
            print(self.type,"1")
            connect.commit()
            connect.close()

            self.quit()
            
            #myInstance = myMain();

           # self.myInstance.createTable();
            #self.myInstance.displayData()
           # myObj.displayData()
  
    def quit(self):
        self.window.destroy()      
        
    def run(self):
        self.window.mainloop()

