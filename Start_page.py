from tkinter import*
from tkinter import messagebox
import sqlite3
from tkinter.ttk import Treeview

win=Tk()
win.title("Welcome")
win.state('zoomed')
win.iconbitmap('Hospi.ico')
pic=PhotoImage(file='Img2.png')
Label(win,image=pic).pack()

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

    frame=Frame(doc,width=350,height=400,bg="light gray")
    frame.place(x=500,y=230)

    lbl=Label(frame,text="Doctor Details form",bg="light gray",font=('Microsoft YaHei UI Light',15,'bold'))
    lbl.place(x=50,y=9)

    def on_enter(e):
        username.delete(0,'end')

    def on_leave(e):
        name=username.get()
        if name=='':
            username.insert(0,'Doctor Name')
            
    username=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    username.place(x=30,y=50,height=30)
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
    address.place(x=30,y=100,height=30)
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
    role.place(x=30,y=150,height=30)
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
    salary.place(x=30,y=200,height=30)
    salary.insert(0,"Salary")
    salary.bind('<FocusIn>',on_enter)
    salary.bind('<FocusOut>',on_leave)

    def on_enter(e):
        delete_box.delete(0,'end')

    def on_leave(e):
        name=delete_box.get()
        if name=='':
            delete_box.insert(0,'Delete')

    delete_box=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    delete_box.place(x=30,y=250,height=30)
    delete_box.insert(0,"Delete")
    delete_box.bind("<FocusIn>",on_enter)
    delete_box.bind('<FocusOut>',on_leave)

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
        username.insert(0,"Doctor Name")
        address.insert(0,"Special In")
        role.insert(0,"Role")
        salary.insert(0,"Salary")

    btn_add=Button(frame,width=10,text='Add',bg='blue',font=8,fg='white',border=0,command=add)
    btn_add.place(x=10,y=300)

    def retrive():
        conn=sqlite3.connect("hospital.db")
        c = conn.cursor()
        c.execute('SELECT * FROM doc')
        records=c.fetchall()
        conn.close()
        
        tree = Treeview(doc, columns=("ID", "Name", "Specialization", "Role", "Salary"), show="headings")
        tree.place(x=200,y=0)

        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Specialization", text="Specialization")
        tree.heading("Role", text="Role")
        tree.heading("Salary", text="Salary")
        for record in records:
            tree.insert("", "end", values=record)

    btn_retrive=Button(frame,width=12,text='Show records',bg='blue',font=8,fg='white',border=0,command=retrive)
    btn_retrive.place(x=115,y=300)

    def delete():
        conn=sqlite3.connect("hospital.db")
        c=conn.cursor()
        c.execute("DELETE FROM doc WHERE ID="+delete_box.get())
        conn.commit()
        conn.close()
        delete_box.delete(0,END)
        retrive()

    btn_delete=Button(frame,width=10,text='Delete',bg='blue',font=8,fg='white',border=0,command=delete)
    btn_delete.place(x=240,y=300)

    def edit():
        global editor
        editor=Tk()
        editor.iconbitmap('Hospi.ico')
        editor.title('Update Data')
        editor.geometry('300x400')
        con=sqlite3.connect('hospital.db')
        c=con.cursor()
        record_id=updatebox.get()
        c.execute('SELECT * FROM doc WHERE ID=?',(record_id,))
        records=c.fetchall()
        global username_editor
        global address_editor
        global role_editor
        global salary_editor

        username_editor=Entry(editor,width=30)
        username_editor.grid(row=0,column=1,padx=20,pady=(10,0))

        address_editor=Entry(editor,width=30)
        address_editor.grid(row=1,column=1)

        role_editor=Entry(editor,width=30)
        role_editor.grid(row=2,column=1)

        salary_editor=Entry(editor,width=30)
        salary_editor.grid(row=3,column=1)
        
        username_label=Label(editor,text="Doctor Name")
        username_label.grid(row=0,column=0,pady=(10,0))

        address_label=Label(editor,text="Special In")
        address_label.grid(row=1,column=0)

        role_label=Label(editor,text="Role")
        role_label.grid(row=2,column=0)

        salary_label=Label(editor,text="Salary")
        salary_label.grid(row=3,column=0)

        for record in records:
            username_editor.insert(0,record[1])
            address_editor.insert(0,record[2])
            role_editor.insert(0,record[3])
            salary_editor.insert(0,record[4])

        updatebox.delete(0,END)
        btn_save=Button(editor,text='SAVE',command=lambda:update(record_id))
        btn_save.grid(row=5,column=0,columnspan=2, pady=10,padx=10,ipadx=125)
        

    def update(record_id):
        con=sqlite3.connect('hospital.db')
        c=con.cursor()
        c.execute('''
            UPDATE doc SET 
                name=:u,
                spec=:a,
                rol=:r,
                slry=:s
                WHERE ID = :id''',
                {
                    'u': username_editor.get(),
                    'a': address_editor.get(),
                    'r': role_editor.get(),
                    's': salary_editor.get(),
                    'id': record_id
                }
        )
        con.commit()
        con.close()
        editor.destroy()
        # retrieve()

    def on_enter(e):
        updatebox.delete(0,'end')

    def on_leave(e):
        name=updatebox.get()
        if name=='':
            updatebox.insert(0,'Update Entry (Id) ')

    updatebox=Entry(frame,width=15,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    updatebox.place(x=30,y=340,height=30)
    updatebox.insert(0,"Update Entry (Id)")
    updatebox.bind('<FocusIn>',on_enter)
    updatebox.bind('<FocusOut>',on_leave)


    btn_edit=Button(frame,width=15,text='Update Records',bg='blue',font=8,fg='white',border=0,command=edit)
    btn_edit.place(x=170,y=340)
    def bck():
        doc.destroy()
    back=Button(doc,text="<== Back",font=('Arial Bold',10),command=bck).place(x=0,y=10)


frame=Frame(win,width=350,height=100,bg="gray")
frame.place(x=200,y=150)
lblford=Label(frame,text="For Doctor info",bg='gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=100,y=10)
doc=Button(frame,width=30,text='Doc',bg='blue',font=8,fg='white',border=0,command=doc).place(x=40,y=50)

def reg():
    global regimg
    reg=Toplevel()
    reg.state('zoomed')
    reg.config(bg='light gray')
    reg.iconbitmap('Hospi.ico')
    reg.title('Regrestration')
    regimg=PhotoImage(file="hobgr.png")
    Label(reg,image=regimg).place(x=0,y=0)
    lbl=Label(reg,text='Register',bg='light gray',font=('Arial Bold',50)).pack()

    conn=sqlite3.connect('hospital.db')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS ptrc(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name             TEXT,
                dies             TEXT,
                rom              INT,
                bed             INT,
                ag             INT,
                gndr            TEXT,
                adres           TEXT,
                wght            INT,
                hgt         INT
    )""")

    frame=Frame(reg,width=350,height=350,bg="light gray")
    frame.place(x=500,y=180)

    lbl=Label(frame,text="Enter patient details",bg="light gray",font=('Microsoft YaHei UI Light',15,'bold'))
    lbl.place(x=50,y=10)

    def on_enter(e):
        username.delete(0,'end')

    def on_leave(e):
        name=username.get()
        if name=='':
            username.insert(0,'Patient Name')
            
    username=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    username.place(x=30,y=50,height=30)
    username.insert(0,"Patient Name")
    username.bind('<FocusIn>',on_enter)
    username.bind('<FocusOut>',on_leave)

    def on_enter(e):
        address.delete(0,'end')

    def on_leave(e):
        name=address.get()
        if name=='':
            address.insert(0,'Age')

    address=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    address.place(x=30,y=100,height=30)
    address.insert(0,"Age")
    address.bind('<FocusIn>',on_enter)
    address.bind('<FocusOut>',on_leave)

    def on_enter(e):
        role.delete(0,'end')

    def on_leave(e):
        name=role.get()
        if name=='':
            role.insert(0,'Height')

    role=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    role.place(x=30,y=150,height=30)
    role.insert(0,"Height")
    role.bind('<FocusIn>',on_enter)
    role.bind('<FocusOut>',on_leave)

    def on_enter(e):
        salary.delete(0,'end')

    def on_leave(e):
        name=salary.get()
        if name=='':
            salary.insert(0,'Weight')

    salary=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    salary.place(x=30,y=200,height=30)
    salary.insert(0,"Weight")
    salary.bind('<FocusIn>',on_enter)
    salary.bind('<FocusOut>',on_leave)

    def add():
        conn=sqlite3.connect('hospital.db')
        c=conn.cursor()
        c.execute("INSERT INTO ptrc(name,ag,hgt,wght) VALUES(?,?,?,?)"
                ,(username.get(),address.get(),role.get(),salary.get()))
        conn.commit()
        conn.close()
        username.delete(0,END)
        address.delete(0,END)
        role.delete(0,END)
        salary.delete(0,END)
        username.insert(0,"Patient Name")
        address.insert(0,"Age")
        role.insert(0,"Height")
        salary.insert(0,"Weight")

    btn_add=Button(frame,width=10,text='Add',bg='blue',font=8,fg='white',border=0,command=add)
    btn_add.place(x=120,y=250)
    def bck():
        reg.destroy()
    back=Button(reg,text="<== Back",font=('Arial Bold',10),command=bck).place(x=0,y=10)





frame=Frame(win,width=350,height=100,bg="dark gray")
frame.place(x=700,y=150)
lblford=Label(frame,text='Registration',bg='dark gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=110,y=10)
doc=Button(frame,width=30,text='Reg',bg='blue',font=8,fg='white',border=0,command=reg).place(x=40,y=50)

def ptr():
    global ptrimg
    ptr=Toplevel()
    ptr.title('Patient Form')
    ptr.state('zoomed')
    ptr.config(bg='light gray')
    ptr.iconbitmap('Hospi.ico')
    ptrimg=PhotoImage(file="ptbg.png")
    Label(ptr,image=ptrimg).place(x=-150,y=0)
    lbl=Label(ptr,text='Patient',bg='light blue',font=('Arial Bold',50)).pack()


    frame=Frame(ptr,width=350,height=400,bg="light gray")
    frame.place(x=500,y=230)

    lbl=Label(frame,text="Enter patient details",bg="light gray",font=('Microsoft YaHei UI Light',15,'bold'))
    lbl.place(x=50,y=10)

    def on_enter(e):
        username.delete(0,'end')

    def on_leave(e):
        name=username.get()
        if name=='':
            username.insert(0,'Patient Name')
            
    username=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    username.place(x=30,y=50,height=30)
    username.insert(0,"Patient Name")
    username.bind('<FocusIn>',on_enter)
    username.bind('<FocusOut>',on_leave)

    def on_enter(e):
        address.delete(0,'end')

    def on_leave(e):
        name=address.get()
        if name=='':
            address.insert(0,'Diagnosed With')

    address=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    address.place(x=30,y=100,height=30)
    address.insert(0,"Diagnosed With")
    address.bind('<FocusIn>',on_enter)
    address.bind('<FocusOut>',on_leave)

    def on_enter(e):
        role.delete(0,'end')

    def on_leave(e):
        name=role.get()
        if name=='':
            role.insert(0,'Room No.')

    role=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    role.place(x=30,y=150,height=30)
    role.insert(1,"Room No.")
    role.bind('<FocusIn>',on_enter)
    role.bind('<FocusOut>',on_leave)

    def on_enter(e):
        salary.delete(0,'end')

    def on_leave(e):
        name=salary.get()
        if name=='':
            salary.insert(0,'Bed No.')

    salary=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    salary.place(x=30,y=200,height=30)
    salary.insert(0,"Bed No.")
    salary.bind('<FocusIn>',on_enter)
    salary.bind('<FocusOut>',on_leave)

    def on_enter(e):
        delete_box.delete(0,'end')

    def on_leave(e):
        name=delete_box.get()
        if name=='':
            delete_box.insert(0,'Delete ')

    delete_box=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    delete_box.place(x=30,y=250)
    delete_box.insert(0,"Delete Entry")
    delete_box.bind('<FocusIn>',on_enter)
    delete_box.bind('<FocusOut>',on_leave)

    def add():
        conn=sqlite3.connect('hospital.db')
        c=conn.cursor()
        c.execute("INSERT INTO ptrc(name,dies,rom,bed) VALUES(?,?,?,?)"
                ,(username.get(),address.get(),role.get(),salary.get()))
        conn.commit()
        conn.close()
        username.delete(0,END)
        address.delete(0,END)
        role.delete(0,END)
        salary.delete(0,END)
        username.insert(0,"Patient Name")
        address.insert(0,"Diagnosed With")
        role.insert(0,"Room No.")
        salary.insert(0,"Bed No.")

    btn_add=Button(frame,width=10,text='Add',bg='blue',font=8,fg='white',border=0,command=add)
    btn_add.place(x=10,y=300)

    def retrive():
        conn=sqlite3.connect("hospital.db")
        c = conn.cursor()
        c.execute('SELECT * FROM ptrc')
        records=c.fetchall()
        conn.close()

        tree =Treeview(ptr,column=("ID","Name","Diagnosed With","Room No.","Bed No.","Age","Gender","Address","Weight","Height"),show="headings")
        tree.place(x=180,y=0)

        tree.heading("ID", text="ID")
        tree.column("ID",width=25)
        tree.heading("Name", text="Name")
        tree.column("Name",width=150)
        tree.heading("Diagnosed With", text="Diagnosed With")
        tree.column("Diagnosed With",width=170)
        tree.heading("Room No.", text="Room No.")
        tree.column("Room No.",width=90)
        tree.heading("Bed No.", text="Bed No.")
        tree.column("Bed No.",width=90)
        tree.heading("Age",text="Age")
        tree.column("Age",width=50)
        tree.heading("Gender",text="Gender")
        tree.column("Gender",width=80)
        tree.heading("Address",text="Address")
        tree.column("Address",width=150)
        tree.heading("Weight",text="weight")
        tree.column("Weight",width=90)
        tree.heading("Height",text="Height")
        tree.column("Height",width=90)
        for record in records:
            tree.insert("", "end", values=record)

    btn_retrive=Button(frame,width=13,text='Show Records',bg='blue',font=8,fg='white',border=0,command=retrive)
    btn_retrive.place(x=112,y=300)

    def delete():
        conn=sqlite3.connect("hospital.db")
        c=conn.cursor()
        c.execute("DELETE FROM ptrc WHERE ID="+delete_box.get())
        conn.commit()
        conn.close()
        delete_box.delete(0,END)
        retrive()

    btn_delete=Button(frame,width=10,text='Delete',bg='blue',font=8,fg='white',border=0,command=delete)
    btn_delete.place(x=240,y=300)

    def edit():
        global editor
        editor=Toplevel()
        editor.iconbitmap('Hospi.ico')
        editor.title('Update Data')
        editor.geometry('300x400')
        con=sqlite3.connect('hospital.db')
        c=con.cursor()
        record_id=updatebox.get()
        c.execute('SELECT * FROM ptrc WHERE ID=?',(record_id,))
        records=c.fetchall()
        global username_editor
        global address_editor
        global role_editor
        global salary_editor

        username_editor=Entry(editor,width=30)
        username_editor.grid(row=0,column=1,padx=20,pady=(10,0))

        address_editor=Entry(editor,width=30)
        address_editor.grid(row=1,column=1)

        role_editor=Entry(editor,width=30)
        role_editor.grid(row=2,column=1)

        salary_editor=Entry(editor,width=30)
        salary_editor.grid(row=3,column=1)
        
        username_label=Label(editor,text="Patient Name")
        username_label.grid(row=0,column=0,pady=(10,0))

        address_label=Label(editor,text="Diesease")
        address_label.grid(row=1,column=0)

        role_label=Label(editor,text="Room no.")
        role_label.grid(row=2,column=0)

        salary_label=Label(editor,text="Bed no.")
        salary_label.grid(row=3,column=0)

        for record in records:
            username_editor.insert(0,record[1])
            address_editor.insert(0,record[2])
            role_editor.insert(0,record[3])
            salary_editor.insert(0,record[4])

        updatebox.delete(0,END)
        btn_save=Button(editor,text='SAVE',command=lambda:update(record_id))
        btn_save.grid(row=5,column=0,columnspan=2, pady=10,padx=10,ipadx=125)
        

    def update(record_id):
        con=sqlite3.connect('hospital.db')
        c=con.cursor()
        c.execute('''
            UPDATE ptrc SET 
                name=:u,
                dies=:a,
                rom=:r,
                bed=:s
                WHERE ID = :id''',
                {
                    'u': username_editor.get(),
                    'a': address_editor.get(),
                    'r': role_editor.get(),
                    's': salary_editor.get(),
                    'id': record_id
                }
        )
        con.commit()
        con.close()
        editor.destroy()
        # retrieve()

    def on_enter(e):
        updatebox.delete(0,'end')

    def on_leave(e):
        name=updatebox.get()
        if name=='':
            updatebox.insert(0,'Update Entry (Id) ')

    updatebox=Entry(frame,width=15,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    updatebox.place(x=30,y=340,height=30)
    updatebox.insert(0,"Details (Id)")
    updatebox.bind('<FocusIn>',on_enter)
    updatebox.bind('<FocusOut>',on_leave)
    Label(frame,text="Use id to see details",bg="light gray",font=('Microsoft YaHei UI Light',8)).place(x=30,y=370)


    btn_edit=Button(frame,width=15,text='See Record',bg='blue',font=8,fg='white',border=0,command=edit)
    btn_edit.place(x=170,y=340)
    def back():
        ptr.destroy()
    ext=Button(ptr,text="<== Back",font=("Arial Bold",10),command=back).place(x=0,y=10)


frame=Frame(win,width=350,height=100,bg="dark gray")
frame.place(x=200,y=400)
lblforc=Label(frame,text="For Patient report info",bg='dark gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=70,y=10)
doc=Button(frame,width=30,text='Report',bg='blue',font=8,fg='white',border=0,command=ptr).place(x=40,y=50)


def stf():
    global stfimg
    stf=Toplevel()
    stf.state('zoomed')
    stf.config(bg='light gray')
    stf.iconbitmap('Hospi.ico')
    stf.title('Doc profile')
    stfimg=PhotoImage(file="stfpic.png")
    Label(stf,image=stfimg).place(x=90,y=-10)
    lbl=Label(stf,text='Staff',bg='light gray',font=('Arial Bold',50)).pack()
    conn=sqlite3.connect('hospital.db')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS staff(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name             TEXT,
                spec             TEXT,
                rol              TEXT,
                slry             INT
    )""")
    frame=Frame(stf,width=350,height=400,bg="light gray")
    frame.place(x=500,y=230)

    lbl=Label(frame,text="Staff Details form",bg="light gray",font=('Microsoft YaHei UI Light',15,'bold'))
    lbl.place(x=50,y=9)

    def on_enter(e):
        username.delete(0,'end')

    def on_leave(e):
        name=username.get()
        if name=='':
            username.insert(0,'Staff Name')
            
    username=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    username.place(x=30,y=50,height=30)
    username.insert(0,"Staff Name")
    username.bind('<FocusIn>',on_enter)
    username.bind('<FocusOut>',on_leave)

    def on_enter(e):
        address.delete(0,'end')

    def on_leave(e):
        name=address.get()
        if name=='':
            address.insert(0,'Address')

    address=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    address.place(x=30,y=100,height=30)
    address.insert(0,"Address")
    address.bind('<FocusIn>',on_enter)
    address.bind('<FocusOut>',on_leave)

    def on_enter(e):
        role.delete(0,'end')

    def on_leave(e):
        name=role.get()
        if name=='':
            role.insert(0,'Role')

    role=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    role.place(x=30,y=150,height=30)
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
    salary.place(x=30,y=200,height=30)
    salary.insert(0,"Salary")
    salary.bind('<FocusIn>',on_enter)
    salary.bind('<FocusOut>',on_leave)

    def on_enter(e):
        delete_box.delete(0,'end')

    def on_leave(e):
        name=delete_box.get()
        if name=='':
            delete_box.insert(0,'Delete')

    delete_box=Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    delete_box.place(x=30,y=250,height=30)
    delete_box.insert(0,"Delete")
    delete_box.bind("<FocusIn>",on_enter)
    delete_box.bind('<FocusOut>',on_leave)

    def add():
        conn=sqlite3.connect('hospital.db')
        c=conn.cursor()
        c.execute("INSERT INTO staff(name,spec,rol,slry) VALUES(?,?,?,?)"
                ,(username.get(),address.get(),role.get(),salary.get()))
        conn.commit()
        conn.close()
        username.delete(0,END)
        address.delete(0,END)
        role.delete(0,END)
        salary.delete(0,END)
        username.insert(0,"Staff Name")
        address.insert(0,"Address")
        role.insert(0,"Role")
        salary.insert(0,"Salary")

    btn_add=Button(frame,width=10,text='Add',bg='blue',font=8,fg='white',border=0,command=add)
    btn_add.place(x=10,y=300)

    def retrive():
        conn=sqlite3.connect("hospital.db")
        c = conn.cursor()
        c.execute('SELECT * FROM staff')
        records=c.fetchall()
        conn.close()

        ptrtree = Treeview(stf,column=("ID","Name","Diagnosed With","Room No.","Bed No."),show="headings")
        ptrtree.place(x=200,y=0)

        ptrtree.heading("ID", text="ID")
        ptrtree.heading("Name", text="Name")
        ptrtree.heading("Diagnosed With", text="Address")
        ptrtree.heading("Room No.", text="Role")
        ptrtree.heading("Bed No.", text="Salary")
        for record in records:
            ptrtree.insert("", "end", values=record)

    btn_retrive=Button(frame,width=12,text='Show records',bg='blue',font=8,fg='white',border=0,command=retrive)
    btn_retrive.place(x=115,y=300)

    def delete():
        conn=sqlite3.connect("hospital.db")
        c=conn.cursor()
        c.execute("DELETE FROM staff WHERE ID="+delete_box.get())
        conn.commit()
        conn.close()
        delete_box.delete(0,END)
        retrive()

    btn_delete=Button(frame,width=10,text='Delete',bg='blue',font=8,fg='white',border=0,command=delete)
    btn_delete.place(x=240,y=300)

    def edit():
        global editor
        editor=Tk()
        editor.iconbitmap('Hospi.ico')
        editor.title('Update Data')
        editor.geometry('300x400')
        con=sqlite3.connect('hospital.db')
        c=con.cursor()
        record_id=updatebox.get()
        c.execute('SELECT * FROM staff WHERE ID=?',(record_id,))
        records=c.fetchall()
        global username_editor
        global address_editor
        global role_editor
        global salary_editor

        username_editor=Entry(editor,width=30)
        username_editor.grid(row=0,column=1,padx=20,pady=(10,0))

        address_editor=Entry(editor,width=30)
        address_editor.grid(row=1,column=1)

        role_editor=Entry(editor,width=30)
        role_editor.grid(row=2,column=1)

        salary_editor=Entry(editor,width=30)
        salary_editor.grid(row=3,column=1)
        
        username_label=Label(editor,text="Staff Name")
        username_label.grid(row=0,column=0,pady=(10,0))

        address_label=Label(editor,text="Address")
        address_label.grid(row=1,column=0)

        role_label=Label(editor,text="Role")
        role_label.grid(row=2,column=0)

        salary_label=Label(editor,text="Salary")
        salary_label.grid(row=3,column=0)

        for record in records:
            username_editor.insert(0,record[1])
            address_editor.insert(0,record[2])
            role_editor.insert(0,record[3])
            salary_editor.insert(0,record[4])

        updatebox.delete(0,END)
        btn_save=Button(editor,text='SAVE',command=lambda:update(record_id))
        btn_save.grid(row=5,column=0,columnspan=2, pady=10,padx=10,ipadx=125)
        

    def update(record_id):
        con=sqlite3.connect('hospital.db')
        c=con.cursor()
        c.execute('''
            UPDATE staff SET 
                name=:u,
                spec=:a,
                rol=:r,
                slry=:s
                WHERE ID = :id''',
                {
                    'u': username_editor.get(),
                    'a': address_editor.get(),
                    'r': role_editor.get(),
                    's': salary_editor.get(),
                    'id': record_id
                }
        )
        con.commit()
        con.close()
        editor.destroy()
        # retrieve()

    def on_enter(e):
        updatebox.delete(0,'end')

    def on_leave(e):
        name=updatebox.get()
        if name=='':
            updatebox.insert(0,'Update Entry (Id) ')

    updatebox=Entry(frame,width=15,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11))
    updatebox.place(x=30,y=340,height=30)
    updatebox.insert(0,"Update Entry (Id)")
    updatebox.bind('<FocusIn>',on_enter)
    updatebox.bind('<FocusOut>',on_leave)


    btn_edit=Button(frame,width=15,text='Update Records',bg='blue',font=8,fg='white',border=0,command=edit)
    btn_edit.place(x=170,y=340)
    def bck():
        stf.destroy()
    back=Button(stf,text="<== Back",font=('Arial Bold',10),command=bck).place(x=0,y=10)





    
frame=Frame(win,width=350,height=100,bg="gray")
frame.place(x=700,y=400)
lblford=Label(frame,text="Staff Info",bg='gray',fg='white',font=('Mycrosoft YaHei UI Light',15,'bold')).place(x=120,y=10)
doc=Button(frame,width=30,text='Staff',bg='blue',font=8,fg='white',border=0,command=stf).place(x=40,y=50)

def log_btn():
    win.destroy()
    import login

Button(win,text="Log out",font=('Mycrosoft YaHei UI Light',8,'bold'),bg="red",fg="white",command=log_btn,border=6).place(x=5,y=0)

win.mainloop()
