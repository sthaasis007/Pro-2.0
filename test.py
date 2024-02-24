# from tkinter import*
# from tkinter import messagebox

# win=Tk()
# win.title("Hospital login")   # for title name 
# win.iconbitmap('C:\\Users\\Accer\\Desktop\\project\\Hospi.ico') # for putting icon should be .ico file
# win.geometry('950x500')     #for hight and weight
# win.resizable(False,False)
# image = PhotoImage(file="C:\\Users\\Accer\\Desktop\\project\\sho.png")  # Provide the path to your image file
# label = Label(win, image=image)
# label.image = image  # Keep a reference to the image
# label.pack()

# def login():
#     username=user.get()
#     password=code.get()
#     if username=='admin' and password=='admin':
#         win.destroy()
#         # import fpage
        
#     else:
#         messagebox.showerror('Invalide',"Invalide username or pass")
        
# frame=Frame(win,width=350,height=350,bg="white")
# frame.place(x=300,y=70)

# top=Label(win,text='Hospital Management System',font=('Mycrosoft YaHei UI Light',32)).pack()

# # heding=Label(frame,text='Log in',fg='blue',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
# # heding.place(x=100,y=5)

# def on_enter(e):
#     user.delete(0,'end')

# def on_leave(e):
#     name=user.get()
#     if name=='':
#         user.insert(0,'Username')

# user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
# user.place(x=30,y=75)
# user.insert(0,'Username')
# user.bind('<FocusIn>',on_enter)
# user.bind('<FocusOut>',on_leave)

# Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


# def on_enter(e):
#     code.delete(0,'end')

# def on_leave(e):
#     name=code.get()
#     if name=='':
#         code.insert(0,'Password')

# code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
# code.place(x=30,y=140)
# code.insert(0,'Password')
# code.bind('<FocusIn>',on_enter)
# code.bind('<FocusOut>',on_leave)
# Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
# Button(frame,width=30,text='Log in',bg='blue',font=8,fg='white',border=0,command=login).place(x=35,y=200)




# win.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    # Create a table named 'users' if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT
                )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    try:
        # Insert a new user into the 'users' table
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    # Check if the provided username and password match a user in the 'users' table
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    # Close the database connection
    conn.close()

    return user is not None

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        add_user(username, password)
        messagebox.showinfo("Registration Successful", f"User '{username}' registered successfully.")
    else:
        messagebox.showerror("Error", "Both username and password are required.")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if authenticate_user(username, password):
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("Login App")

# Create username label and entry field
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Create password label and entry field
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Create register and login buttons
ttk.Button(root, text="Register", command=register_user).pack(pady=10)
ttk.Button(root, text="Login", command=login).pack(pady=10)

# Initialize the database
create_database()

# Run the main event loop
root.mainloop()
