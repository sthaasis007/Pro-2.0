from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview 

def doc():
    global docimg
    doc=Toplevel()
    doc.title("Hospital login")
    doc.state('zoomed')
    doc.iconbitmap('Hospi.ico')
    docimg=PhotoImage(file='doc1.png')
    Label(doc,image=docimg).place(x=-20,y=0)
    conn=sqlite3.connect('hospital.db')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS doc(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name             TEXT,
                spec             TEXT,
                rol              TEXT,
                slry             INT
    )""")

    frame=Frame(doc,width=350,height=340,bg="light gray")
    frame.place(x=500,y=180)
    def on_enter(e):
        username.delete(0,'end')

    def on_leave(e):
        name=username.get()
        if name=='':
            username.insert(0,'Doctor Name')
            
    username=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    username.place(x=45,y=50,height=30)
    username.insert(0,"Doctor Name")
    username.bind('<FocusIn>',on_enter)
    username.bind('<FocusOut>',on_leave)

    def on_enter(e):
        address.delete(0,'end')

    def on_leave(e):
        name=address.get()
        if name=='':
            address.insert(0,'Special In')

    address=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    address.place(x=45,y=100,height=30)
    address.insert(0,"Special In")
    address.bind('<FocusIn>',on_enter)
    address.bind('<FocusOut>',on_leave)

    def on_enter(e):
        role.delete(0,'end')

    def on_leave(e):
        name=role.get()
        if name=='':
            role.insert(0,'Role')

    role=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    role.place(x=45,y=150,height=30)
    role.insert(0,"Role")
    role.bind('<FocusIn>',on_enter)
    role.bind('<FocusOut>',on_leave)

    def on_enter(e):
        salary.delete(0,'end')

    def on_leave(e):
        name=salary.get()
        if name=='':
            salary.insert(0,'Salary')

    salary=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    salary.place(x=45,y=200,height=30)
    salary.insert(0,"Salary")
    salary.bind('<FocusIn>',on_enter)
    salary.bind('<FocusOut>',on_leave)

    def add():
        conn=sqlite3.connect('hospital.db')
        c=conn.cursor()
        c.execute("INSERT INTO doc(name,spec,rol,slry) VALUES(?,?,?,?)"
                ,(username.get(),address.get(),role.get(),salary.get()))
        conn.commit()
        conn.close()
        username.delete(0,END)
        address.delete(0,END)
        role.delete(0,END)
        salary.delete(0,END)

    btn_add=Button(frame,width=15,text='Add',bg='blue',font=8,fg='white',border=0,command=add)
    btn_add.place(x=20,y=250)

    def show():
        conn = sqlite3.connect("hospital.db")
        c = conn.cursor()
        c.execute('SELECT * FROM doc')
        records = c.fetchall()
        conn.close()

        # Create a new window to display the records
        display_window = Tk()
        display_window.title("Doctor Records")

        # Create Treeview widget to display records
        tree = Treeview(display_window, columns=("ID", "Name", "Specialization", "Role", "Salary"), show="headings")
        tree.pack()

        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Specialization", text="Specialization")
        tree.heading("Role", text="Role")
        tree.heading("Salary", text="Salary")

        # Insert records into Treeview
        for record in records:
            tree.insert("", "end", values=record)

        # Add a button to the window
        button = Button(display_window, text="Close", command=display_window.destroy)
        button.pack()


    btn_retrive=Button(frame,width=15,text='Show records',bg='blue',font=8,fg='white',border=0,command=show)
    btn_retrive.place(x=190,y=250)

win=Tk()
win.title("Welcome")
win.state('zoomed')
win.iconbitmap('Hospi.ico')
pic=PhotoImage(file='Img2.png')
Label(win,image=pic).pack()

frame=Frame(win,width=350,height=100,bg="gray")
frame.place(x=200,y=150)
lblford=Label(frame,text="For Doctor info",bg='gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=100,y=10)
doc=Button(frame,width=30,text='Doc',bg='blue',font=8,fg='white',border=0,command=doc).place(x=40,y=50)

def reg():
    reg=Tk()



frame=Frame(win,width=350,height=100,bg="dark gray")
frame.place(x=700,y=150)
lblford=Label(frame,text='Registration',bg='dark gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=110,y=10)
doc=Button(frame,width=30,text='Reg',bg='blue',font=8,fg='white',border=0,command=reg).place(x=40,y=50)

def ptr():
    ptr=Tk()


frame=Frame(win,width=350,height=100,bg="dark gray")
frame.place(x=200,y=400)
lblforc=Label(frame,text="For Patient report info",bg='dark gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=70,y=10)
doc=Button(frame,width=30,text='Report',bg='blue',font=8,fg='white',border=0,command=ptr).place(x=40,y=50)


def stf():
    stf=Tk()

    
frame=Frame(win,width=350,height=100,bg="gray")
frame.place(x=700,y=400)
lblford=Label(frame,text="Staff Info",bg='gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=120,y=10)
doc=Button(frame,width=30,text='Staff',bg='blue',font=8,fg='white',border=0,command=stf).place(x=40,y=50)

win.mainloop()
