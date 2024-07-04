import customtkinter as ctk
import tkinter as tr
from tkinter import messagebox as mb
import mysql.connector
window = ctk.CTk()
window.title("ENROLL")
window.geometry('340x400')
window.configure(fg_color='#d1d5fd',borderwidth=5)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

desired_width = 340
desired_height = 400
center_window(window, desired_width, desired_height)

def login():
    username = username_entry.get()
    password = pass_entry.get()

    if(username=="" or password==""):
        mb.showerror(title="Invalid credentials",message="Please Enter Correct credentials")
    else:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql022004',
            database='carnival'
        )

        mycursor = mydb.cursor()
        query = "select * from vol_login"
        mycursor.execute(query)
        row = mycursor.fetchall()
        print(row)
        for i in row:
            if(i[0] == username and i[1] == password):
                msg = 'yes'
                break
            else:
                msg = 'no'

        if(msg == 'yes'):
            window.destroy()
            mb.showinfo(title="SUCCESS", message="LOGIN SUCCESSFULL")
            import vol_homepage

        else:
            mb.showinfo(title="FAILED", message="LOGIN UNSUCCESSFULL")


frame = tr.Frame(bg='#fac6c6')

login_label = tr.Label(window,text='Volunteer Login',bg='#d1d5fd',font=("Times", 35))
username_label = ctk.CTkLabel(window,text='Username',bg_color='#d1d5fd',font=('Arial',18),text_color='#130c5b')
pass_label = ctk.CTkLabel(window,text='Password',bg_color='#d1d5fd',font=('Arial',18),text_color='#130c5b')
username_entry = ctk.CTkEntry(window,font=('Arial',13),width=150,height=26,fg_color='#d1d3e8')
pass_entry = ctk.CTkEntry(window,font=('Arial',13),width=150,height=26,fg_color='#d1d3e8')
login_btn = ctk.CTkButton(window,text='LOGIN',fg_color="#130c5b",corner_radius=50,width=90,command= login)

login_label.place(x=50,y=10)
username_label.place(x=45,y=130)
pass_label.place(x=45,y=170)
username_entry.place(x= 150,y=130)
pass_entry.place(x=150,y=170)
login_btn.place(x=120,y=240)

frame.pack()


window.mainloop()



