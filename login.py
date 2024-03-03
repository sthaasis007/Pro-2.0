from tkinter import*
from tkinter import messagebox
import sqlite3


def create_database():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT
                )''')

    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")

    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    conn.close()

    return user is not None

def register_user():
    def sign():
        username = user1.get()
        password = code1.get()

        if "@gmail.com" not in username:
            messagebox.showerror("Invalid Username", "Username must be a Gmail address (@gmail.com).")
            return
        
        if len(password) < 8:
            messagebox.showerror("Invalid Password", "Password must be at least 8 characters long.")
            return

        if username == "Username" and password == "Password":
            messagebox.showerror("Error", "Invalid username or password.")
            return

        if username and password:
            add_user(username, password)
            messagebox.showinfo("Registration Successful", f"User '{username}' registered successfully.")
        else:
            messagebox.showerror("Error", "Both username and password are required.")
        win.destroy()
    
    global loimg
    win=Toplevel()
    win.iconbitmap("Hospi.ico")
    win.title("Hospital login")
    win.geometry('950x500') 
    win.resizable(False,False)
    loimg=PhotoImage(file='img2.png')
    Label(win,image=loimg).pack()
    frame=Frame(win,width=350,height=350,bg="white")
    frame.place(x=300,y=70)

    top=Label(win,text='Hospital Management System',font=('Mycrosoft YaHei UI Light',32)).pack()

    heding=Label(frame,text='Sign In',fg='blue',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heding.place(x=100,y=5)

    def on_enter(e):
        user1.delete(0,'end')

    def on_leave(e):
        name=user1.get()
        if name=='':
            user1.insert(0,'Username')

    user1=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    user1.place(x=30,y=75)
    user1.insert(0,'Username')
    user1.bind('<FocusIn>',on_enter)
    user1.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


    def on_enter(e):
        code1.delete(0,'end')

    def on_leave(e):
        name=code1.get()
        if name=='':
            code1.insert(0,'Password')
    def yes():
        win.destroy()

    code1=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    code1.place(x=30,y=140)
    code1.insert(0,'Password')
    code1.bind('<FocusIn>',on_enter)
    code1.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    Button(frame,width=30,text='Register',bg='blue',font=8,fg='white',border=0,command=sign).place(x=35,y=200)
    Label(frame,text="Already have account ",bg="white",font=('Microsoft YaHei UI Light',9)).place(x=45,y=230)
    Button(frame, text="Log In",fg="blue",border=0, command=yes,font=('Microsoft YaHei UI Light',9),bg="white").place(x=160,y=229)




def login():
    username = user1.get()
    password = code1.get()

    if authenticate_user(username, password):
        messagebox.showinfo("Login Successful", f"Welcome, {username} press ok to enter")
        root.destroy()
        import Main_page
        
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root=Tk()
root.iconbitmap("Hospi.ico")
root.title("Hospital login")
root.geometry('950x500') 
root.resizable(False,False)
img=PhotoImage(file='login.png')
Label(root,image=img).place(x=80,y=70)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=500,y=70)

top=Label(root,text='Hospital Management System',font=('Mycrosoft YaHei UI Light',32)).pack()

heding=Label(frame,text='Log in',fg='blue',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heding.place(x=100,y=5)

def on_enter(e):
    user1.delete(0,'end')

def on_leave(e):
    name=user1.get()
    if name=='':
        user1.insert(0,'Username')

user1=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user1.place(x=30,y=75)
user1.insert(0,'Username')
user1.bind('<FocusIn>',on_enter)
user1.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    code1.delete(0,'end')

def on_leave(e):
    name=code1.get()
    if name=='':
        code1.insert(0,'Password')

code1=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code1.place(x=30,y=140)
code1.insert(0,'Password')
code1.bind('<FocusIn>',on_enter)
code1.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
Button(frame,width=30,text='Log in',bg='blue',font=8,fg='white',border=0,command=login).place(x=35,y=200)
Label(frame,text="Don't have account ",bg="white",font=('Microsoft YaHei UI Light',9)).place(x=45,y=230)
Button(frame, text="Sign In",fg="blue",border=0, command=register_user,font=('Microsoft YaHei UI Light',9),bg="white").place(x=160,y=229)

create_database()

root.mainloop()