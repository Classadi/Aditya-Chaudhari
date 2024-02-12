import tkinter as tr
from tkinter import messagebox as mb
import mysql.connector

window = tr.Tk()
window.title("ENROLL")
window.geometry('304x400')
window.configure(bg='#fac6c6')

def clear_fields():
    username_entry.delete(0, 'end')
    pass_entry.delete(0, 'end')
    confirm_pass_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')

def register_user():
    username = username_entry.get()
    password = pass_entry.get()
    confirm_password = confirm_pass_entry.get()
    phone = phone_entry.get()

    if username == "" or password == "" or confirm_password == "" or phone == "":
        mb.showerror(title="Invalid credentials", message="Please Enter All Fields")
    elif password != confirm_password:
        mb.showerror(title="Invalid credentials", message="Passwords do not match")
    else:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql022004',
            database='carnival'
        )
        mycursor = mydb.cursor()
        query = f"INSERT INTO user_login (username, password, phone, role) VALUES ('{username}', '{password}', '{phone}', 'user')"
        mycursor.execute(query)
        mydb.commit()
        mb.showinfo(title="SUCCESS", message="User Registration Successful")

def login():
    username = username_entry.get()
    password = pass_entry.get()

    if username == "" or password == "":
        mb.showerror(title="Invalid credentials", message="Please Enter Correct credentials")
    else:
        # Perform login authentication
        pass  # Placeholder for authentication logic

def return_to_login():
    # Clear existing fields
    clear_fields()

    # Remove registration widgets
    username_label.grid_forget()
    pass_label.grid_forget()
    confirm_pass_label.grid_forget()
    phone_label.grid_forget()
    username_entry.grid_forget()
    pass_entry.grid_forget()
    confirm_pass_entry.grid_forget()
    phone_entry.grid_forget()
    register_user_btn.grid_forget()
    return_btn.grid_forget()

    # Display login widgets
    username_label.grid(row=1, column=0)
    pass_label.grid(row=2, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    pass_entry.grid(row=2, column=1, pady=20)
    login_btn.grid(row=3, column=0, pady=10)
    register_btn.grid(row=3, column=1, pady=10)
    login_label.config(text="Login")

def create_registration_page(is_return_to_login=True):
    if is_return_to_login:
        return_to_login()

    # Clear existing fields
    clear_fields()

    # Remove login widgets
    username_label.grid_forget()
    pass_label.grid_forget()
    confirm_pass_label.grid_forget()
    phone_label.grid_forget()
    username_entry.grid_forget()
    pass_entry.grid_forget()
    login_btn.grid_forget()
    register_btn.grid_forget()
    login_label.config(text="Registration")

    # Create registration widgets
    username_label.grid(row=1, column=0)
    pass_label.grid(row=2, column=0)
    confirm_pass_label.grid(row=3, column=0)
    phone_label.grid(row=4, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    pass_entry.grid(row=2, column=1, pady=20)
    confirm_pass_entry.grid(row=3, column=1, pady=20)
    phone_entry.grid(row=4, column=1, pady=20)
    register_user_btn.grid(row=5, column=0, columnspan=2, pady=10)
    return_btn.grid(row=6, column=0, columnspan=2, pady=10)

frame = tr.Frame(bg='#fac6c6')

login_label = tr.Label(frame, text='Login', bg='#fac6c6', font=['Comic Sans MS', 23])
username_label = tr.Label(frame, text='Username', bg='#fac6c6', font=['Arial', 13])
pass_label = tr.Label(frame, text='Password', bg='#fac6c6', font=['Arial', 13])
confirm_pass_label = tr.Label(frame, text='Confirm Password', bg='#fac6c6', font=['Arial', 13])
phone_label = tr.Label(frame, text='Phone', bg='#fac6c6', font=['Arial', 13])
username_entry = tr.Entry(frame, font=['Arial', 13])
pass_entry = tr.Entry(frame, font=['Arial', 13], show='*')
confirm_pass_entry = tr.Entry(frame, font=['Arial', 13], show='*')
phone_entry = tr.Entry(frame, font=['Arial', 13])

login_btn = tr.Button(frame, text='LOGIN', bg="#FF3399", command=login)
register_btn = tr.Button(frame, text='Register', bg="#FF3399", command=lambda: create_registration_page(False))
register_user_btn = tr.Button(frame, text='Register User', bg="#FF3399", command=register_user)
return_btn = tr.Button(frame, text='Return to Login', bg="#FF3399", command=return_to_login)

def create_registration_page(is_return_to_login=True):
    if is_return_to_login:
        return_to_login()

    # Clear existing fields
    clear_fields()

    # Remove login widgets
    username_label.grid_forget()
    pass_label.grid_forget()
    confirm_pass_label.grid_forget()
    phone_label.grid_forget()
    username_entry.grid_forget()
    pass_entry.grid_forget()
    login_btn.grid_forget()
    register_btn.grid_forget()
    login_label.config(text="Registration")

    # Create registration widgets
    username_label.grid(row=1, column=0)
    pass_label.grid(row=2, column=0)
    confirm_pass_label.grid(row=3, column=0)
    phone_label.grid(row=4, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    pass_entry.grid(row=2, column=1, pady=20)
    confirm_pass_entry.grid(row=3, column=1, pady=20)
    phone_entry.grid(row=4, column=1, pady=20)
    register_user_btn.grid(row=5, column=0, columnspan=2, pady=10)
    return_btn.grid(row=6, column=0, columnspan=2, pady=10)

login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1, column=0)
pass_label.grid(row=2, column=0)
username_entry.grid(row=1, column=1, pady=20)
pass_entry.grid(row=2, column=1, pady=20)
login_btn.grid(row=3, column=0, pady=10)
register_btn.grid(row=3, column=1, pady=10)

frame.pack()

window.mainloop()
