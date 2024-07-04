import customtkinter as ctk
import tkinter as tr
from tkinter import messagebox as mb
import mysql.connector
window = tr.Tk()
window.title("ENROLL")
window.geometry('340x400')
window.configure(bg='#fac6c6')
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
    # username ='Omkar'
    # password ='123456'
    # if (username_entry.get() == username and pass_entry.get() == password):
    #     mb.showinfo(title="LOGIN SUCCESSFULL!!!",message="You Successfully Logged In")
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
        # mydb = mysql.connector.connect(host='localhost',username='root',password='mysql022004',database='carnival')
        mycursor = mydb.cursor()
        query = "select * from user_login"
        mycursor.execute(query)
        row = mycursor.fetchall()
        print(row)
        for i in row:
            if(i[0] == username and i[1] == int(password)):
                msg = 'yes'
                break
            else:
                msg = 'no'

        if(msg == 'yes'):
            window.destroy()
            mb.showinfo(title="SUCCESS", message="LOGIN SUCCESSFULL")
            import user_home

        else:
            mb.showinfo(title="FAILED", message="LOGIN UNSUCCESSFULL")


frame = tr.Frame(bg='#fac6c6')

def toggle_password():
    if pass_entry.cget('show') == '*':
        hide_btn.configure(text_color='white')
        pass_entry.config(show='')
    else:
        hide_btn.configure(text_color='#FF3399')
        pass_entry.config(show='*')

login_label = tr.Label(frame,text='Login',bg='#fac6c6',font=['Comic Sans MS',23])
username_label = tr.Label(frame,text='Username',bg='#fac6c6',font=['Arial',13])
pass_label = tr.Label(frame,text='Password',bg='#fac6c6',font=['Arial',13])
username_entry = tr.Entry(frame,font=['Arial',13])
pass_entry = tr.Entry(frame,font=['Arial',13],show='*')
login_btn = tr.Button(frame,text='LOGIN',bg="#FF3399",command= login)



login_label.grid(row=0,column=0,columnspan=2, sticky='news',pady=40)
username_label.grid(row=1,column=0)
pass_label.grid(row=2,column=0)
username_entry.grid(row=1,column=1,pady=20)
pass_entry.grid(row=2,column=1,pady=20)
login_btn.grid(row=3,column=0,columnspan=10,pady=30)

frame.pack()
hide_btn = ctk.CTkButton(window,text='👁️',command=toggle_password,text_color='#FF3399',hover_color='pink',font=('Times',25),width=5,height=5,fg_color='#fac6c6')
hide_btn.place(x=305,y=205)


window.mainloop()



