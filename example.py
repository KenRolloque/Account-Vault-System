
import mysql.connector as mysql
import tkinter as tk
import tkinter.messagebox as MessageBox


def insert():
    info1 = entry1.get()
    info2 = entry2.get()
    info3 = entry3.get()
    info4 = entry4.get()
    info5 = entry5.get()

    if (entry1 == ""or entry2 == ""or entry3 == ""or entry4 == ""or entry5 == ""):

        MessageBox.showinfo("Inser Status","Complete the following form")

    else:
            connect = connection()

            cursor = connect.cursor()
            cursor.execute("INSERT INTO example (name,email,phone,password,type) VALUES('"+info1+"','"+info2+"','"+info3+"','"+info4+"','"+info5+"')")
            cursor.execute("commit")
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            entry5.delete(0, 'end')
            #MessageBox.showinfo("Data Added Successfully")

            connect.close()

window = tk.Tk()
window.geometry("500x500")
window.resizable(False,False)


entry1 = tk.Entry(window, text ="Entry 1")
entry1.pack()

entry2 = tk.Entry(window, text ="Entry 2")
entry2.pack()

entry3 = tk.Entry(window, text ="Entry 3")
entry3.pack()

entry4 = tk.Entry(window, text ="Entry 4")
entry4.pack()

entry5 = tk.Entry(window, text ="Entry 5")
entry5.pack()

add = tk.Button(window, text = "Add", command = insert)
add.pack()

window.mainloop()