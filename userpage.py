import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import mysql.connector
import io
# from image_checker import shared_image_data
from PIL import Image, ImageTk
from itertools import cycle
import time

from tkinter import messagebox as mb
def manage():
    window = ctk.CTk()
    ctk.CTkButton(window, text='VOLUNTEERS', fg_color='#037476').pack(expand=True, fill='both', pady=10)
    window.mainloop()
class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.configure(fg_color='#213354',bg_color='#213354')
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(8, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

window = ctk.CTk()
window.title('volunteer HOME')
window.geometry('1000x600')
window.configure(fg_color='#000c38',bg_color='#000c38')
window.resizable(False,False)

win_hm = ctk.CTkFrame(window,height=800,width=600)
win_man = ctk.CTkFrame(window,height=800,width=600)
win_eve = ctk.CTkFrame(window,height=800,width=600)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

desired_width = 1000
desired_height = 600
center_window(window, desired_width, desired_height)


sym_lbl = ctk.CTkLabel(window,text='m',font=('Webdings',550),bg_color='black',height=600)
sym_lbl.pack(expand=True)
sym_lbl.place(x=700,y=0)
win_eve.pack(pady=5, fill='both')
frame2 = ctk.CTkFrame(window, fg_color='#453478', height=1000, width=700)
frame2.pack(side='top', expand=True, fill='x')
frame2.place(x=10)
frame2.tkraise()
print('event')

win_man.pack(pady=5, fill='both')
frame3 = ctk.CTkFrame(window,fg_color='#6d4ad4',height=1000,width=700)
frame3.pack(side='left',expand=True,fill='both')
frame3.place(x=10)
frame3.tkraise()
print('home')


win_hm.pack(pady=5, fill='both')
frame1 = ctk.CTkFrame(window,fg_color='#e1d9f9',height=1000,width=700)
frame1.pack(side='top',expand=True,fill='x')
frame1.place(x=10)
frame1.tkraise()

#event frame
global my_tab2
my_tab2 = ctk.CTkTabview(frame3,width=700,height=570,
                         segmented_button_unselected_color='#C0CCE2',
                         border_width=3,border_color='white',
                             bg_color='#9a82e1',text_color='black',
                             text_color_disabled='white',
                             segmented_button_fg_color='#34265c',
                         segmented_button_selected_hover_color='#3e287d',
                             segmented_button_unselected_hover_color='white',
                             segmented_button_selected_color='#d6fdb7')

eve1_title = 'Treasure_hunt'
my_tab2.pack(pady=10,expand=True,fill='both')
my_tab2.configure(fg_color='#9a82e1')
case_1 = my_tab2.add(eve1_title)
case_2 = my_tab2.add('MURDER_MYSTERY')
case_3 = my_tab2.add('AUCTION')
case_4 = my_tab2.add('NEON \n LAGORI')
case_5 = my_tab2.add('BUZZER UP')
font = ctk.CTkFont(family='Times', size= 25)




lb1 = ctk.CTkLabel(case_1,text='Enter Name',bg_color='#9a82e1',font=font)
lb1.place(x=80,y=60)
lb2 = ctk.CTkLabel(case_1, text='Enter Contact No.', bg_color='#9a82e1', font=font)
lb2.place(x=80,y=95)
e11 =ctk.CTkEntry(case_1,text_color='purple',fg_color='#C0CCE2')
e11.place(x=280,y=65)
e12 = ctk.CTkEntry(case_1, text_color='purple',fg_color='#C0CCE2')
e12.place(x=280, y=98)

def ref1():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title1}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    lb41.configure(text=eve1_count-count)
    for i in range(count):
        slot1[i].configure(text_color='black')
    mydb.commit()
    mydb.close()

def ref2():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title2}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    lb42.configure(text=eve2_count-count)
    for i in range(count):
        slot2[i].configure(text_color='black')
    mydb.commit()
    mydb.close()

def ref3():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title3}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    lb43.configure(text=eve3_count-count)
    for i in range(count):
        slot3[i].configure(text_color='black')
    mydb.commit()
    mydb.close()

def ref4():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title4}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    lb44.configure(text=eve4_count-count)
    for i in range(count):
        slot4[i].configure(text_color='black')
    mydb.commit()
    mydb.close()

def ref5():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title5}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    lb45.configure(text=eve5_count-count)
    for i in range(count):
        slot5[i].configure(text_color='black')
    mydb.commit()
    mydb.close()

title1 = 'treasure_hunt'
eve1_count = 8
eve2_count = 6
title2 = 'Murder_Mystery'
eve3_count = 15
title3 = 'auction'
eve4_count = 2
title4 = 'Neon_Lagori'
eve5_count = 6
title5 = 'Buzzer_Up'
def eve1():
    if len(e12.get()) == 10:
        params = (e11.get(), e12.get())
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql022004',
            database='carnival')
        mycursor = mydb.cursor()
        count_query = f'SELECT COUNT(*) AS total_entries FROM {title1}'
        mycursor.execute(count_query)
        count = mycursor.fetchone()[0]
        print(count)
        if count < eve1_count:
            query = f"INSERT INTO {title1} values(%s,%s)"
            mycursor.execute(query, params)
            mydb.commit()
            mydb.close()
            mb.showinfo(title='Successfull', message='Enrolled Successfully')

        else:
            mb.showerror(title='BATCH FULL!!!!', message='Sorry the current batch is full ,please try again later :)')
    else:
        mb.showerror(message='Enter correct contact no. !!!!! ')

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
mycursor = mydb.cursor()
count_query = f'SELECT COUNT(*) AS total_entries FROM {title1}'
mycursor.execute(count_query)
count = mycursor.fetchone()[0]
refresh1 = ctk.CTkButton(case_1,text='🗘',font=('Times',30),fg_color='#3e287d',bg_color='#9a82e1',corner_radius=10,width=5,border_spacing=0,border_width=2,border_color='#C0CCE2',hover_color='#7959d7',command=ref1)
refresh1.place(x=350,y=231)
lb41 = ctk.CTkLabel(case_1,text=eve1_count-count,font=font)
lb41.place(x=300,y=240)
btn1 = ctk.CTkButton(case_1,text='Enroll',fg_color='#3e287d',bg_color='#9a82e1',corner_radius=90,width=75,border_width=5,border_color='#C0CCE2',hover_color='#7959d7',command=eve1)
btn1.place(x=220,y=160)
lb3 = ctk.CTkLabel(case_1,text='Availaible Spots :',font=font,bg_color='#9a82e1')
lb3.place(x=60,y=240)
r =50
slot1 = []
for i in range(eve1_count//2):
    captain = ctk.CTkLabel(case_1,text='👤',font=('Times',35))
    captain.place(x=r,y=280)
    slot1.append(captain)
    r += 50

r=50
for i in range(eve1_count//2):
    captain = ctk.CTkLabel(case_1,text='👤',font=('Times',35))
    captain.place(x=r,y=330)
    slot1.append(captain)
    r += 50




def toplvl():

    print(55)
    topwin1 = ctk.CTkToplevel(case_1,fg_color='#7959d7')
    topwin1.geometry('500x500')
    topwin1.resizable(False,False)
    topwin1.attributes('-topmost', True)
    toptb = (ctk.CTkTextbox(topwin1,fg_color='#7959d7',bg_color='black',height=400,width=470,border_width=2))
    toptb.place(x=15,y=10)




ibtn1 = ctk.CTkButton(case_1,text='i',font=('Webdings',30),fg_color='#9a82e1',command=toplvl,
                      width=20,corner_radius=120,hover_color='#7959d7')
ibtn1.place(x=5,y=2)


lb1 = ctk.CTkLabel(case_2, text='Enter Name', bg_color='#9a82e1', font=font)
lb1.place(x=80, y=60)
lb2 = ctk.CTkLabel(case_2, text='Enter Contact No.', bg_color='#9a82e1', font=font)
lb2.place(x=80, y=95)
e21 = ctk.CTkEntry(case_2, text_color='purple',fg_color='#C0CCE2')
e21.place(x=280, y=65)
e22 = ctk.CTkEntry(case_2, text_color='purple',fg_color='#C0CCE2')
e22.place(x=280, y=98)
def eve2():
    if len(e22.get()) == 10:
        params = (e21.get(), e22.get())
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql022004',
            database='carnival')
        mycursor = mydb.cursor()
        count_query = f'SELECT COUNT(*) AS total_entries FROM {title2}'
        mycursor.execute(count_query)
        count = mycursor.fetchone()[0]
        if count < eve2_count:
            query = f"INSERT INTO {title2} values(%s,%s)"
            mycursor.execute(query, params)
            mydb.commit()
            mydb.close()
            mb.showinfo(title='Successfull', message='Enrolled Successfully')
        else:
            mb.showerror(title='BATCH FULL!!!!', message='Sorry the current batch is full ,please try again later :)')
    else:
        mb.showerror(message='Enter correct contact no. !!!!! ')

btn1 = ctk.CTkButton(case_2, text='Enroll',fg_color='#3e287d', bg_color='#9a82e1', corner_radius=90, width=75,border_width=5,border_color='#C0CCE2',command=eve2)
btn1.place(x=220, y=160)
lb3 = ctk.CTkLabel(case_2, text='Availaible Spots :', font=font, bg_color='#9a82e1')
lb3.place(x=60, y=240)
refresh2 = ctk.CTkButton(case_2,text='🗘',font=('Times',30),fg_color='#3e287d',bg_color='#9a82e1',corner_radius=10,width=5,border_spacing=0,border_width=2,border_color='#C0CCE2',hover_color='#7959d7',command=ref2)
refresh2.place(x=350,y=231)
lb42 = ctk.CTkLabel(case_2, text=eve2_count-count, font=font)
lb42.place(x=300, y=240)
ibtn2 = ctk.CTkButton(case_2,text='i',font=('Webdings',30),fg_color='#9a82e1',width=20,corner_radius=120,hover_color='#7959d7')
ibtn2.place(x=5,y=2)


lb1 = ctk.CTkLabel(case_3, text='Enter Name', bg_color='#9a82e1', font=font)
lb1.place(x=80, y=60)
lb2 = ctk.CTkLabel(case_3, text='Enter Contact No.', bg_color='#9a82e1', font=font)
lb2.place(x=80, y=95)
e31 = ctk.CTkEntry(case_3, text_color='purple',fg_color='#C0CCE2')
e31.place(x=280, y=65)
e32 = ctk.CTkEntry(case_3, text_color='purple',fg_color='#C0CCE2')
e32.place(x=280, y=98)
r =50
slot2 = []
for i in range(eve2_count//2):
    captain = ctk.CTkLabel(case_2,text='👤',font=('Times',35))
    captain.place(x=r,y=280)
    slot2.append(captain)
    r += 50

r=50
for i in range(eve2_count//2):
    captain = ctk.CTkLabel(case_2,text='👤',font=('Times',35))
    captain.place(x=r,y=330)
    slot2.append(captain)
    r += 50
def eve3():
    params = (e31.get(),e32.get())
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title3}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    if count < eve3_count:
        query = f"INSERT INTO {title3} values(%s,%s)"
        mycursor.execute(query, params)
        mydb.commit()
        mydb.close()
        mb.showinfo(title='Successfull', message='Enrolled Successfully')
    else:
        mb.showerror(title='BATCH FULL!!!!', message='Sorry the current batch is full ,please try again later :)')


btn1 = ctk.CTkButton(case_3, text='Enroll',fg_color='#3e287d', bg_color='#9a82e1', corner_radius=90, width=75,border_width=5,border_color='#C0CCE2',command=eve3)
btn1.place(x=220, y=160)
lb3 = ctk.CTkLabel(case_3, text='Availaible Spots :', font=font, bg_color='#9a82e1')
lb3.place(x=60, y=240)
refresh3 = ctk.CTkButton(case_3,text='🗘',font=('Times',30),fg_color='#3e287d',bg_color='#9a82e1',corner_radius=10,width=5,border_spacing=0,border_width=2,border_color='#C0CCE2',hover_color='#7959d7',command=ref3)
refresh3.place(x=350,y=231)
lb43 = ctk.CTkLabel(case_3, text=eve3_count-count, font=font)
lb43.place(x=300, y=240)
ibtn3 = ctk.CTkButton(case_3,text='i',font=('Webdings',30),fg_color='#9a82e1',width=20,corner_radius=120,hover_color='#7959d7')
ibtn3.place(x=5,y=2)

lb1 = ctk.CTkLabel(case_4, text='Enter Name', bg_color='#9a82e1', font=font)
lb1.place(x=80, y=60)
lb2 = ctk.CTkLabel(case_4, text='Enter Contact No.', bg_color='#9a82e1', font=font)
lb2.place(x=80, y=95)
e41 = ctk.CTkEntry(case_4, text_color='purple',fg_color='#C0CCE2')
e41.place(x=280, y=65)
e42 = ctk.CTkEntry(case_4, text_color='purple',fg_color='#C0CCE2')
e42.place(x=280, y=98)
r =50
slot3 = []
for i in range(eve3_count//2):
    captain = ctk.CTkLabel(case_3,text='👤',font=('Times',35))
    captain.place(x=r,y=280)
    slot3.append(captain)
    r += 50

r=50
for i in range(eve3_count//2):
    captain = ctk.CTkLabel(case_3,text='👤',font=('Times',35))
    captain.place(x=r,y=330)
    slot3.append(captain)
    r += 50
def eve4():
    params = (e41.get(),e42.get())
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title4}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    if count < eve4_count:
        query = f"INSERT INTO {title4} values(%s,%s)"
        mycursor.execute(query, params)
        mydb.commit()
        mydb.close()
        mb.showinfo(title='Successfull', message='Enrolled Successfully')
    else:
        mb.showerror(title='BATCH FULL!!!!', message='Sorry the current batch is full ,please try again later :)')


btn1 = ctk.CTkButton(case_4, text='Enroll',fg_color='#3e287d', bg_color='#9a82e1', corner_radius=90, width=75,border_width=5,border_color='#C0CCE2',command=eve4)
btn1.place(x=220, y=160)
lb3 = ctk.CTkLabel(case_4, text='Availaible Spots :', font=font, bg_color='#9a82e1')
lb3.place(x=60, y=240)
refresh4 = ctk.CTkButton(case_4,text='🗘',font=('Times',30),fg_color='#3e287d',bg_color='#9a82e1',corner_radius=10,width=5,border_spacing=0,border_width=2,border_color='#C0CCE2',hover_color='#7959d7',command=ref4)
refresh4.place(x=350,y=231)
lb44 = ctk.CTkLabel(case_4, text=eve4_count-count, font=font)
lb44.place(x=300, y=240)
ibtn4 = ctk.CTkButton(case_4,text='i',font=('Webdings',30),fg_color='#9a82e1',width=20,corner_radius=120,hover_color='#7959d7')
ibtn4.place(x=5,y=2)


lb1 = ctk.CTkLabel(case_5, text='Enter Name', bg_color='#9a82e1', font=font)
lb1.place(x=80, y=60)
lb2 = ctk.CTkLabel(case_5, text='Enter Contact No.', bg_color='#9a82e1', font=font)
lb2.place(x=80, y=95)
e51 = ctk.CTkEntry(case_5, text_color='purple',fg_color='#C0CCE2')
e51.place(x=280, y=65)
e52 = ctk.CTkEntry(case_5, text_color='purple',fg_color='#C0CCE2')
e52.place(x=280, y=98)
r =50
slot4 = []
for i in range(eve4_count//2):
    captain = ctk.CTkLabel(case_4,text='👤',font=('Times',35))
    captain.place(x=r,y=280)
    slot4.append(captain)
    r += 50

r=50
for i in range(eve4_count//2):
    captain = ctk.CTkLabel(case_4,text='👤',font=('Times',35))
    captain.place(x=r,y=330)
    slot4.append(captain)
    r += 54
def eve5():
    params = (e51.get(),e52.get())
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    count_query = f'SELECT COUNT(*) AS total_entries FROM {title5}'
    mycursor.execute(count_query)
    count = mycursor.fetchone()[0]
    if count < eve5_count:
        query = f"INSERT INTO {title5} values(%s,%s)"
        mycursor.execute(query, params)
        mydb.commit()
        mydb.close()
        mb.showinfo(title='Successfull', message='Enrolled Successfully')
    else:
        mb.showerror(title='BATCH FULL!!!!', message='Sorry the current batch is full ,please try again later :)')


btn1 = ctk.CTkButton(case_5, text='Enroll',fg_color='#3e287d', bg_color='#9a82e1', corner_radius=90, width=75,border_width=5,border_color='#C0CCE2',command=eve5)
btn1.place(x=220, y=160)
lb3 = ctk.CTkLabel(case_5, text='Availaible Spots :', font=font, bg_color='#9a82e1')
lb3.place(x=60, y=240)
refresh5 = ctk.CTkButton(case_5,text='🗘',font=('Times',30),fg_color='#3e287d',bg_color='#9a82e1',corner_radius=10,width=5,border_spacing=0,border_width=2,border_color='#C0CCE2',hover_color='#7959d7',command=ref5)
refresh5.place(x=350,y=231)
lb45 = ctk.CTkLabel(case_5, text=eve5_count-count, font=font)
lb45.place(x=300, y=240)
ibtn5 = ctk.CTkButton(case_5,text='i',font=('Webdings',30),fg_color='#9a82e1',width=20,corner_radius=120,hover_color='#7959d7')
ibtn5.place(x=5,y=2)
r =50
slot5 = []
for i in range(eve5_count//2):
    captain = ctk.CTkLabel(case_5,text='👤',font=('Times',35))
    captain.place(x=r,y=280)
    slot5.append(captain)
    r += 50

r=50
for i in range(eve5_count//2):
    captain = ctk.CTkLabel(case_5,text='👤',font=('Times',35))
    captain.place(x=r,y=330)
    slot5.append(captain)
    r += 50

#Help desk widgets
# hlb = ctk.CTkLabel(frame2,text='LIST OF VOLUNTEERS :',font=("Times", 20,'italic'))
# hlb.place(x=5,y=5)
# hscroll = ctk.CTkScrollableFrame(frame2,width=440)
# hscroll.place(x=230,y=5)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql022004',
    database='carnival'
)

# Function to fetch data from the database
def fetch_data():
    cursor = mydb.cursor()
    cursor.execute("SELECT vname, phn_no FROM vol_login")
    return cursor.fetchall()

# Set up the main window


# Create a Treeview widget
tree = ttk.Treeview(frame2, columns=('Name', 'Phone Number'))
tree.heading('#0', text='Index')
tree.heading('Name', text='Name')
tree.heading('Phone Number', text='Phone Number')
tree.column('#0', width=100, stretch=tk.NO)  # Increase the width of the first column
tree.column('Name', width=200, stretch=tk.NO)  # Increase the width of the 'Name' column
tree.column('Phone Number', width=200, stretch=tk.NO)

# Insert data into the Treeview widget
for index, (name, phone_number) in enumerate(fetch_data(), start=1):
    tree.insert('', 'end', text=str(index), values=(name, phone_number))
style = ttk.Style()
style.configure('Treeview', font=('Times', 16),background="gold",
                foreground="black",
                rowheight=40,
                fieldbackground="lightgrey",desired_height=150)
tree.configure(height=10)
tree.place(x=70,y=75)
ctk.CTkLabel(frame2,text='Volunteer Info....',text_color='white',font=('Times',35,'italic','bold')).place(x=5,y=5)

def display_image():
    try:
        # Connect to your MySQL database
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql022004',
            database='carnival'
        )

        mycursor = mydb.cursor()
        # Retrieve the image data from the table (assuming you have an 'id' for the image)
        image_id1 = 1
        image_id2 = 2
        image_id3 = 3
        sql = "SELECT image_data FROM images WHERE id = %s"
        mycursor.execute(sql, (image_id1,))
        img_data = mycursor.fetchone()[0]

        # Convert the binary image data to an ImageTk object
        img = Image.open(io.BytesIO(img_data))
        ctk_img = ctk.CTkImage(img, size=(img.width, img.height))

        slbl1 = ctk.CTkLabel(frame1, height=400, width=210, fg_color='white', image=ctk_img)
        slbl1.place(x=10, y=10)
        sql = "SELECT image_data FROM images WHERE id = %s"
        mycursor.execute(sql, (image_id2,))
        img_data = mycursor.fetchone()[0]

        # Convert the binary image data to an ImageTk object
        img = Image.open(io.BytesIO(img_data))
        ctk_img2 = ctk.CTkImage(img, size=(img.width, img.height))
        slbl2 = ctk.CTkLabel(frame1, height=400, width=210, fg_color='white',image=ctk_img2)
        slbl2.place(x=230, y=10)

        sql = "SELECT image_data FROM images WHERE id = %s"
        mycursor.execute(sql, (image_id3,))
        img_data = mycursor.fetchone()[0]
        img = Image.open(io.BytesIO(img_data))
        ctk_img3 = ctk.CTkImage(img, size=(img.width, img.height))
        slbl3 = ctk.CTkLabel(frame1, height=400, width=210, fg_color='white',image=ctk_img3)
        slbl3.place(x=450, y=10)
        mycursor.close()
        mydb.close()
    except Exception as e:
        print(f"Error retrieving image: {e}")
display_image()
def change_color():
    # Get the next color from the cycle

    next_color = next(color_cycle)
    eve_name_lbl.configure(text_color=next_color)

    window.after(400, change_color)

colors = ['#4B0082', '#800080', '#8A2BE2', '#9370DB', '#7B68EE', '#6A5ACD', '#483D8B']

# Create a cycle of colors
color_cycle = cycle(colors)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql022004',
    database='carnival'
)

mycursor = mydb.cursor()
query = "select title from event"
mycursor.execute(query)
row = mycursor.fetchone()
print(row)
main_eve = row[0]

TitleCard = ctk.CTkFrame(frame1,height=300,width=500,fg_color='#e1d9f9')
TitleCard.place(x=60,y=430)
eve_name_lbl = ctk.CTkLabel(TitleCard,text=main_eve,text_color='black',fg_color='#e1d9f9',font=("Georgia", 100))
eve_name_lbl.place(x=140,y=20)
change_color()

#subevents


#Home widgets

animated_panel = SlidePanel(window, 1.0, 0.7)
animated_panel.configure(fg_color='#C0CCE2',bg_color='#C0CCE2',height=1500,border_width=5)
ctk.CTkButton(animated_panel, text='HOME',text_color='#213354',fg_color='#e1d9f9',border_width=2,hover_color='#c7c0dc',border_color='#213354',width=200,command=lambda: frame1.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='EVENTS',text_color='#213354' ,border_width=2,border_color='#213354',hover_color='#c7c0dc',fg_color='#9a82e1',width=200,command=lambda: frame3.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='HELPDESK',fg_color='#453478',border_width=2,border_color='#213354',text_color='white',hover_color='#c7c0dc',width=200,command=lambda: frame2.tkraise()).pack(  pady=10)
button_x = 0.5
button = ctk.CTkButton(window, text='☰', command=animated_panel.animate,height=10,width=2,fg_color='#213354',bg_color='black')
button.place(relx=0.98, rely=0.03, anchor='center')

window.mainloop()
