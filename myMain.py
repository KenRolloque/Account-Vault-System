import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk
from PIL import ImageTk, Image

import adminInformation
import actionClass 


#import myDB
#outside class

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
class Interface:    

    def __init__ (self):

        self.window = tk.Tk()
        self.window.geometry("1500x820")
        self.window.resizable("False","False")

        self.y = 0
        

        #Image Variable
        self.n = tk.StringVar()
        
        self.stringVar_totalAcc = tk.StringVar()
        self.stringVar_gameAcc = tk.StringVar()
        self.stringVar_bank = tk.StringVar()
        self.stringVar_soc = tk.StringVar()
        self.logoImage = Image.open("D:/Administrator/Python Code/Class/Account Storage/Image/logo.png")
        self.adminImage = Image.open("D:/Administrator/Python Code/Class/Account Storage/Image/admin.png")
        self.logo = ImageTk.PhotoImage(self.logoImage)
        self.admin = ImageTk.PhotoImage(self.adminImage)

        self.displayAddPanel = self.createAdd_Panel()
        self.displayContent = self.contentPanel()
        # Entry variable
       # self.passAccount
        #self.passEmail
        #self.passPass
        #self.passPhone
        #self.passType
        #Call Method
        self.createLogo()
        self.createAddLabel()
        self.createEntry()
        self.createButtons()
        self.createCombo_type()

        self.createAdmin()
        self.displaySqr_container = self.createSqr_container()

        #self.totalAccount = self.findTotal_acc()
        self.findTotal_acc()
        self.findGame_acc()
        self.findBank_acc()
        self.findSoc_acc()

        self.displaySqr1 = self.createSquare1()
        self.displaySqr2 = self.createSquare2()
        self.displaySqr3 = self.createSquare3()
        self.displaySqr4 = self.createSquare4()

        
        self.createContent_sqr()
        self.createCount_sqr()

        self.displayTable_container = self.createTable_container()
        self.createRec()
        self.displayTable = self.createTable()
        self.createScrollbar()
        self.createTable_button()

        self.window.after(0, self.displayData)
        
             # self.equal = ImageTk.PhotoImage(file  ="D:/Administrator/Python Code/Class/Practicing Tkinter/2col.png")     
    
    def callOutsideClass(self):
        self.myObj = actionClass.Action()

    def createAdd_Panel(self):
        addPanel = tk.Frame(self.window, height = 820, width = 400, bg =addPanelBG)
        addPanel.place (x = 0 , y = 0)
        return addPanel

    # Content of Add Panel

    def createLogo (self):
        logo = tk.Label(self.displayAddPanel,image = self.logo, borderwidth = 0, highlightthickness = 0, bg = addPanelBG) 
        logo.image = self.logo
        logo.place(x = 75, y = 40)

        logoLabel = tk.Label(self.displayAddPanel, text = "One Name, Storage for All !!!", font = TAGNAME , bg =addPanelBG, fg ="White")
        logoLabel.place (x = 75 ,y = 180)

    # ENTRY LABEL
    def createAddLabel(self):

        #id = tk.Label(self.displayAddPanel, text = "ID" , font =ADDLABEL, bg = addPanelBG, fg = ADDCOLOR )
        #id.place(x = 35, y =245)

        account = tk.Label(self.displayAddPanel, text = "Account" , font =ADDLABEL, bg = addPanelBG, fg = ADDCOLOR )
        account.place(x = 35, y =245)

        accountName = tk.Label(self.displayAddPanel, text = "Account Name", font =ADDLABEL, bg = addPanelBG, fg = ADDCOLOR)
        accountName.place (x = 35, y = 320)

        email = tk.Label(self.displayAddPanel, text = "Email", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        email.place(x = 35, y = 395)

        password = tk.Label(self.displayAddPanel, text = "Password / Pin Code", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        password.place(x = 35, y = 470)

        phoneNumber = tk.Label(self.displayAddPanel, text = "Phone Number", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        phoneNumber.place(x = 35, y = 545)

        type = tk.Label(self.displayAddPanel, text = "Type", font = ADDLABEL , bg = addPanelBG , fg = ADDCOLOR)
        type.place(x = 35, y = 620)

    # Add ENTRY
    def createEntry(self):

       # self.idEntry = tk.Entry(self.displayAddPanel, bg ="#01345e", font =ENTRYFONT,width = 12, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        #self.idEntry.place(x = 35, y = 270, height = 35)

        self.acc = tk.Entry(self.displayAddPanel, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.acc.place(x = 35, y = 270, height = 35)

        self.accountEntry = tk.Entry(self.displayAddPanel, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.accountEntry.place(x = 35, y = 345, height = 35)

        self.emailEntry = tk.Entry(self.displayAddPanel, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.emailEntry.place(x = 35, y = 420, height = 35)

        self.passwordEntry= tk.Entry(self.displayAddPanel ,bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.passwordEntry.place(x = 35, y = 495, height = 35)

        self.phoneEntry = tk.Entry(self.displayAddPanel, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        self.phoneEntry.place(x = 35, y = 570, height = 35)

        #typeEntry = tk.Entry(self.displayAddPanel, bg ="#01345e", font =ENTRYFONT,width = 44, fg ="White", borderwidth = 10, highlightthickness = 0, relief = "flat")
        #typeEntry.place(x = 35, y = 570, height = 35)

    def createCombo_type(self):

        style  = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground = "#01345e")
        typeList = ttk.Combobox(self.displayAddPanel, width = 51,foreground = "white", background ="#01345e", textvariable = self.n)
        typeList ['values'] = ('Social Media Account','Game Account','Online/Bank Account')
        typeList.place(x = 36, y = 645, height = 35)
        typeList.current(0)


    def createButtons(self):

        addButton = tk.Button(self.displayAddPanel, text = "Add", font =ADDLABEL, bg ="#017779", fg ="White", borderwidth = 0, highlightthickness = 0, relief = "flat", command = self.insert)
        addButton.place(x = 180, y =720, height = 30, width = 80)

        clearButton = tk.Button(self.displayAddPanel, text = "Clear", font =ADDLABEL, bg ="#017779", fg ="White", borderwidth = 0, highlightthickness = 0, relief = "flat", comman = self.clear)
        clearButton.place(x = 280, y =720, height = 30, width = 80)



    # Content Panel

    def contentPanel(self):
        contentPanel = tk.Frame(self.window, height = 820,width = 1100, bg =contentPanelBG,)
        contentPanel.place(x = 400, y = 0)
        return contentPanel

    def createAdmin(self):

        self.adminText = ""

        adminIcon = tk.Button(self.displayContent,image = self.admin, borderwidth = 0, highlightthickness = 0, bg = contentPanelBG, command = self.accessAdmin) 
        adminIcon.image = self.admin
        adminIcon.place(x = 1000, y = 20)

        connect = mysql.connect(
                    host = "localhost", 
                    username = "root",
                    port ="3306", 
                    password="", 
                    database = "accountstorage",
                
                    )
        cursor = connect.cursor()
        sql = "SELECT * FROM info"
        cursor.execute(sql) 
        result = cursor.fetchall()
        
        for x in result:
            
            self.adminText = x[0]

        
        adminLabel = tk.Button(self.displayContent, text = self.adminText, fg ="White", bg  = contentPanelBG, font = ADMINFONT, bd = 0 , highlightthickness = 0, command = self.accessAdmin)
        adminLabel.place(x = 880, y = 35)

    def createSqr_container(self): # Square container
        container = tk.Frame(self.displayContent, height = 160, width =1000, bg = "#001221")
        container.place(x = 50, y = 100)
        return container

    def createSquare1(self):

        square1 = tk.Frame(self.displaySqr_container, height = 123, width = 132, bg ="#3d107b")
        square1.place( x = 88, y = 18)
        return square1  

    def createSquare2(self):
        square2 = tk.Frame(self.displaySqr_container, height = 123, width = 132, bg ="#019ecb" )
        square2.place( x = 303, y = 18)
        return square2

    def createSquare3(self):

        square3 = tk.Frame(self.displaySqr_container, height = 123, width = 132, bg ="#00b236" )
        square3.place( x = 543, y = 18)
        return square3

    def createSquare4(self):

        square4 = tk.Frame(self.displaySqr_container, height = 123, width = 132, bg ="#c0009a" )
        square4.place( x = 783, y = 18)
        return square4

        #adminIcon.pack(side = "right")

    def createContent_sqr(self):

        titleLabel = tk.Label(self.displaySqr1, text = "Total Account",  width = 14, fg = "White", font = SQUARELABEL, bg ="#3d107b")
        titleLabel.place(x = 0 , y = 10)

        titleLabel2 = tk.Label(self.displaySqr2, text = "Game Account",  width = 14, fg = "White", font = SQUARELABEL, bg ="#019ecb")
        titleLabel2.place(x = 0 , y = 10)

        titleLabel3 = tk.Label(self.displaySqr3, text = "Bank Account",  width = 14, fg = "White", font = SQUARELABEL, bg ="#00b236")
        titleLabel3.place(x = 0 , y = 10)

        titleLabel4 = tk.Label(self.displaySqr4, text = "Social Media \n Account",  width = 14, fg = "White", font = SQUARELABEL, bg ="#c0009a")
        titleLabel4.place(x = 0 , y = 2)

        return titleLabel
        return titleLabel2
        return titleLabel3
        return titleLabel4


    def createRec(self):
        rec = tk.Frame(self.displayContent, height = 30, width = 1000, bg = "#00999b")
        rec.place(x = 50, y = 280)
        return rec
    def insert(self):

            #getID = self.idEntry.get()

            #self.createEntry()

            getAcc = self.acc.get()
            getAccount = self.accountEntry.get()
            getEmail = self.emailEntry.get()
            getPass = self.passwordEntry.get()
            getPhone = self.phoneEntry.get()
            getType = self.n.get()

            if ( getAcc == "" or getAccount == "" or getEmail == "" or getPass== "" or getPhone == ""):
                
                MessageBox.showerror("Insert Status","Complete the following form")
                


            else:

                connect = mysql.connect(
                host = "localhost", 
                username = "root",
                port ="3306", 
                password="", 
                database = "accountstorage",
                )
                
                cursor = connect.cursor()
                #cursor.execute("INSERT INTO example (name,email,phone,password,type) VALUES('"+info1+"','"+info2+"','"+info3+"','"+info4+"','"+info5+"')")
                #
                sql = ("INSERT INTO table1 (account,accountname,email,password,contact,type) VALUES(%s,%s,%s,%s,%s,%s)")
                val = (getAcc,getAccount, getEmail,getPass, getPhone, getType)
                cursor.execute(sql,val)
                #cursor.execute("commit")
                connect.commit()
                #self.idEntry.delete(0, 'end')
                self.acc.delete(0, 'end')
                self.accountEntry.delete(0, 'end')
                self.emailEntry.delete(0, 'end')
                self.passwordEntry.delete(0, 'end')
                self.phoneEntry.delete(0, 'end')
               
                #connect.autocommit = True
                connect.close()
                MessageBox.showinfo("Data Added","Data Added Successfully")
                self.displayData()
                self.findTotal_acc()
                self.findGame_acc()
                self.findBank_acc()
                self.findSoc_acc()
                self.createCount_sqr()

    def displayData(self):
        connect = mysql.connect(
                host = "localhost", 
                username = "root",
                port ="3306", 
                password="", 
                database = "accountstorage",
                
                )
        cursor = connect.cursor()
        sql = "SELECT * FROM table1 ORDER BY type"
        cursor.execute(sql) 
        result = cursor.fetchall()
        
        self.table.tag_configure('oddrow',background = "#001221")
        self.table.tag_configure('evenrow',background = "#002645")

        self.count = 0
        #for i in result:
            #self.table.insert('',tk.END,values = i)
        if len(result) !=0 :
            self.table.delete(*self.table.get_children())
            for row in result:
                if self.count % 2 != 0:

                    self.table.insert('',tk.END, values = row, tags = ('oddrow',))
                
                else:
                    self.table.insert('',tk.END, values = row, tags = ('evenrow',))
                    
                self.count +=1

        connect.commit()
        #connect.autocommit = True
        connect.close()

    def findTotal_acc(self):
        connect = mysql.connect(
                host = "localhost", 
                username = "root",
                port ="3306", 
                password="", 
                database = "accountstorage",
                
                )
        cursor = connect.cursor()
        sql = "SELECT * FROM table1"
        cursor.execute(sql) 
        cursor.fetchall()
        self.stringVar_totalAcc = cursor.rowcount
        connect.commit()
        #return self.stringVar_totalAcc

    def findGame_acc(self):
        connect = mysql.connect(
                host = "localhost", 
                username = "root",
                port ="3306", 
                password="", 
                database = "accountstorage",
                
                )
        cursor = connect.cursor()
        sql = "SELECT * FROM table1 WHERE type ='Game Account'"
        cursor.execute(sql)
        cursor.fetchall()
        self.stringVar_gameAcc = cursor.rowcount
        connect.commit()

        #return count

    def findBank_acc(self):
        connect = mysql.connect(
                host = "localhost", 
                username = "root",
                port ="3306", 
                password="", 
                database = "accountstorage",
                
                )
        cursor = connect.cursor()
        sql = "SELECT * FROM table1 WHERE type ='Online/Bank Account'"
        cursor.execute(sql)
        cursor.fetchall()
        self.stringVar_bank = cursor.rowcount
        connect.commit()

    def findSoc_acc(self):
        connect = mysql.connect(
                host = "localhost", 
                username = "root",
                port ="3306", 
                password="", 
                database = "accountstorage",
                
                )
        cursor = connect.cursor()
        sql = "SELECT * FROM table1 WHERE type ='Social Media Account'"
        cursor.execute(sql)
        cursor.fetchall()
        self.stringVar_soc = cursor.rowcount
        connect.commit()

    def createTable_container(self): # Table Container

        tableContaier = tk.Frame(self.displayContent, height = 350, width = 1000, bg ="#001221")
        tableContaier.place(x = 50, y = 320 )
        return tableContaier

    def createTable(self):
        style = ttk.Style(self.displayTable_container)
        style.theme_use("clam")
        style.configure("Treeview", background = "#001221", fieldbackground = "#001221", foreground ="White", rowheight = 30)
        
        style2 = ttk.Style(self.displayTable_container)
        style2.theme_use("clam")
        style2.configure("Treeview.Heading", background = "#032139", fieldbackground = "#032139", foreground ="White")
        style2.map('Treeview.Heading', background = [('selected','#0a5b9c')])

        self.table = ttk.Treeview(self.displayTable_container, height = 12)
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

        #contacts = []
        #for n in range(1, 100):
            #contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
        #for contact in contacts:
            #self.table.insert('', tk.END, values=contact)
        
        self.table.pack()  
        self.displayData()
        print("exit")
        #self.totalGame()
        return self.table

    def createScrollbar(self):

        scrollbar = ttk.Scrollbar(self.displayTable_container, orient = tk.VERTICAL, command =self.displayTable.yview)
        self.displayTable.configure(yscroll=scrollbar.set)
        scrollbar.place(x= 990 , y = 0, height = 387)
        return scrollbar

    def createTable_button(self):

        refreshBUtton = tk.Button(self.displayContent, text = "Refresh",font =ADDLABEL, bg ="#017779", fg ="White", borderwidth = 0, highlightthickness = 0, relief = "flat", command = self.refresh)
        refreshBUtton.place(x = 775 , y =740, height = 30, width = 80)

        updateButton = tk.Button(self.displayContent, text = "Update",font =ADDLABEL, bg ="#017779", fg ="White", borderwidth = 0, highlightthickness = 0, relief = "flat", command = self.selectData)
        updateButton.place(x = 875 , y =740, height = 30, width = 80)

        delButton = tk.Button(self.displayContent, text = "Delete",font =ADDLABEL, bg ="#017779", fg ="White", borderwidth = 0, highlightthickness = 0, relief = "flat", command = self.delete)
        delButton.place(x = 975 , y =740, height = 30, width = 80)

    def createCount_sqr(self):

        totalAccount = tk.Label(self.displaySqr1, text = self.stringVar_totalAcc, width = 3, fg = "white", font = COUNTLABEL, bg ="#3d107b" )
        totalAccount.place(x = 13, y = 35)

        gameAccount = tk.Label(self.displaySqr2, text = self.stringVar_gameAcc, width = 3, fg = "white", font = COUNTLABEL, bg ="#019ecb" )
        gameAccount.place(x = 13, y = 35)

        bankAccount = tk.Label(self.displaySqr3, text = self.stringVar_bank, width = 3, fg = "white", font = COUNTLABEL, bg ="#00b236" )
        bankAccount.place(x = 13, y = 35)
    
        mediaAccount = tk.Label(self.displaySqr4, text = self.stringVar_soc, width = 3, fg = "white", font = COUNTLABEL, bg ="#c0009a" )
        mediaAccount.place(x = 13, y = 35)
    
        return totalAccount
        return gameAccount
        return bankAccount
        return mediaAccount


    def selectData(self):

            curItem = self.displayTable.focus()
            values = self.displayTable.item(curItem, "values")
            #print(values[6])

           #value1 = values[0]
            #value2 = values[1]
            #value3 = values[2]
            #value4 = values[3]
            #value5 = values[4]
            #value6 = values[5]
            
            obj = actionClass.Action()
            
            
            obj.setValue(values)    
            print("HI TEXT")
            #obj.displayIdEntry()
            #obj.createCombo_type()
            #self.callOutsideClass()           
            self.refresh()
            
    def delete(self):

        try:
            connect = mysql.connect(
                    host = "localhost", 
                    username = "root",
                    port ="3306", 
                    password="", 
                    database = "accountstorage",
                
                    )
            cursor = connect.cursor()
            self.selectedItem = self.table.selection()[0]
            self.uid = self.table.item(self.selectedItem)['values'][0]
            sql = "DELETE FROM table1 WHERE id = %s"
            data = (self.uid,)
            cursor.execute(sql, data)

            connect.commit()
            self.table.delete(self.selectedItem)
            MessageBox.showinfo("Delete","Data Deleted Successfully")
            self.refresh()

        except Exception as e:

            MessageBox.showerror("Delete Error","Select an Item First")

    def clear(self):
        self.acc.delete(0, 'end')
        self.accountEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')
        self.phoneEntry.delete(0, 'end')

    def refresh(self):

        self.displayData()
        self.findBank_acc()
        self.findGame_acc()
        self.findTotal_acc()
        self.findSoc_acc()
        self.createCount_sqr()
        self.createAdmin()
        self.y = 0
    def accessAdmin(self):

        if self.y < 1:
            self.x = adminInformation.Admin()
            self.y +=1

        

    def run(self):
       
        self.window.mainloop()

   


if __name__ == "__main__":

    myInferface = Interface()
    #myInferface.displayData()
    myInferface.run()

