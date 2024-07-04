import tkinter as tr
import customtkinter as ctk
from tkinter import messagebox as mb
from tkinter import StringVar

def login():
    print("Log In button clicked")

def registration():
    print("Registration button clicked")

window = tr.Tk()
window.title("Carnival")
window.geometry('1000x600')
window.configure(bg='#fac6c6')
window.resizable(False,False)


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

desired_width = 1000
desired_height = 600
center_window(window, desired_width, desired_height)


# Create a frame to hold the Carnival label
carnival_frame = tr.Frame(window, bg='#fac6c6')
carnival_frame.pack(side="left", fill="both", expand=True)


design_label = ctk.CTkLabel(carnival_frame, text="", font=("Helvetica", 230))
design_label.place(x=0,y=0)

# Create a label for the Carnival name with a stylish font
carnival_label = ctk.CTkLabel(carnival_frame, text="Carnival", font=("Times", 120,'italic'),text_color='#FF3399', bg_color='#fac6c6', fg_color='#fac6c6')
carnival_label.pack(expand=True, pady=(20, 0))  # Reduce top padding

# Create a label for the tagline directly below the Carnival label
tagline_label = tr.Label(carnival_frame, text="Tag along and create...", font=("Times", 36,'italic'), bg='#fac6c6', fg='#333333')
tagline_label.pack(expand=True)

def choose():
    text = button_text_variable.get()
    if text == 'PARTICIPANT':
        button_text_variable.set('VOLUNTEER')
    elif text == 'VOLUNTEER':
        button_text_variable.set('ADMIN')
    elif text == 'ADMIN':
        button_text_variable.set('PARTICIPANT')


button_text_variable = StringVar()
ctk.CTkLabel(carnival_frame,text='login as ?',text_color='grey',bg_color='#fac6c6',font=('Georgia',25,'italic')).place(x=400,y=350)
type_btn = ctk.CTkButton(carnival_frame,textvariable=button_text_variable,font=('Georgia',23,'italic','underline'),command=choose
                         ,text_color='grey',fg_color='#fac6c6',hover_color='#FAB0B0')
type_btn.place(x=510,y=350)
button_text_variable.set('PARTICIPANT')
# Create a frame to hold the buttons
button_frame = tr.Frame(window, bg='#fac6c6')
button_frame.pack(side="top", anchor="ne")

# Create Log In button
def register():
    pass
def select():
    ch = button_text_variable.get()
    if ch == 'PARTICIPANT':
        window.destroy()
        import login
    elif ch == 'VOLUNTEER':
        window.destroy()
        import vol_login
    elif ch == 'ADMIN':
        window.destroy()
        import admin_login
    elif ch == '< select login >':
        mb.showwarning(title='LOGIN',message='please select login type !!!')



# logins = ['< select login >','USER LOGIN','VOLUNTEER LOGIN','ADMIN LOGIN']
# login_combo = ctk.CTkComboBox(window,values=logins,width=350,bg_color='#fac6c6',button_color='#7d003f',
#                               fg_color='#FF3399',font=("Terminal", 18,'bold'),corner_radius=90,dropdown_fg_color='#7d003f',
#                               text_color='white',border_width=3,border_color='#7d003f',dropdown_hover_color='pink',dropdown_text_color='ghost white')
# login_combo.place(x=650,y=0)

login_btn = ctk.CTkButton(window,text='LOGIN',bg_color="#fac6c6",border_width=4,border_color='#7d003f',hover_color='#563855',
                          fg_color='#FF3399',corner_radius=50,font=("Arial", 14,'bold'),command=select)
login_btn.place(x=360,y=300)

reg_btn = ctk.CTkButton(window,text='REGISTER',bg_color="#fac6c6",border_width=4,border_color='#7d003f',hover_color='#563855',
                        fg_color='#FF3399',corner_radius=50,font=("Arial", 14,'bold'),command=register)
reg_btn.place(x=550,y=300)

#design
design_label1 = ctk.CTkLabel(window, text="❆",text_color='ghost white', font=("Helvetica", 230))
design_label1.place(x=5,y=10)
design_label2 = ctk.CTkLabel(window, text="❆",text_color='ghost white', font=("Helvetica", 230))
design_label2.place(x=750,y=350)
window.mainloop()
