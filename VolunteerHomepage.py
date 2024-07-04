import mysql.connector
from idlelib.tooltip import Hovertip
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='mysql022004',
#     database='carnival'
# )
# mycursor = mydb.cursor()
# mycursor.execute('SELECT * FROM user_login')
# users = mycursor.fetchall()
# for user in users:
#     print(user)
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
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

# win_man.grid(row=0,column=0)
# win_eve.grid(row=0,column=0)

# def hm():
#     btn1 = ctk.CTkButton(win_hm,text='hm_btn1')
#     btn1.pack(pady=10,anchor='center')
#     btn2 = ctk.CTkButton(win_hm, text='hm_btn2')
#     btn2.pack(pady=10, anchor='center')

sym_lbl = ctk.CTkLabel(window,text='I',font=('Webdings',550),bg_color='black',height=600)
sym_lbl.place(x=580,y=0)
win_eve.pack(pady=5, fill='both')
frame2 = ctk.CTkFrame(window, fg_color='#335BA2', height=1000, width=700)
frame2.pack(side='top', expand=True, fill='x')
frame2.place(x=10)
frame2.tkraise()
print('event')

win_man.pack(pady=5, fill='both')
frame3 = ctk.CTkFrame(window,fg_color='#7DAAFB',height=1000,width=700)
frame3.pack(side='top',expand=True,fill='x')
frame3.place(x=10)
frame3.tkraise()
print('home')


win_hm.pack(pady=5, fill='both')
frame1 = ctk.CTkFrame(window,fg_color='#CADDFF',height=1000,width=700)
frame1.pack(side='top',expand=True,fill='x')
frame1.place(x=10)
frame1.tkraise()
print('home')
#wX - Webdings -------for symbolic design
title_lbl = ctk.CTkLabel(frame1,text="HOMEPAGE...",font=("Gabriola", 65,"bold","italic"),text_color='Black',width=300)
title_lbl.place(x=180,y=5)
my_lbl1 =ctk.CTkLabel(frame1,font=("Times", 20,'bold'),fg_color='#CADDFF',text_color='#213354',
            text="NAME OF THE EVENT :", height=30, width= 100)

year_entry = ctk.CTkEntry(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2')
year_entry.pack(pady= 20)
year_entry.place(x=400,y=130)

my_lbl1.pack(pady=90)
my_lbl1.place(x=80,y=130)

my_lbl2 =ctk.CTkLabel(frame1,fg_color='#CADDFF',font=("Times", 20,'bold'),text_color='#213354',
            text="MAX NO OF THE PARTICIPANTS :", height=30, width= 100)
year_entry2 = ctk.CTkEntry(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2')
year_entry2.pack(pady= 20)
year_entry2.place(x=400,y=180)

my_lbl2.pack(pady=150)
my_lbl2.place(x=80,y=180)

my_lbl3 =ctk.CTkLabel(frame1,fg_color='#CADDFF',font=("Times", 20,'bold'),text_color='#213354',
            text="TIME PERIOD OF EVENT :", height=30, width= 100)

year_entry3 = ctk.CTkEntry(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2')
year_entry3.pack(pady= 20)
year_entry3.place(x=400,y=230)


my_lbl3.pack(pady=150)
my_lbl3.place(x=80,y=230)
my_lbl4 =ctk.CTkLabel(frame1,fg_color='#CADDFF',font=("Times", 20,'bold'),text_color='#213354',
            text="RULES OF EVENT : ", height=30, width= 100)
year_entry2 = ctk.CTkTextbox(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2',border_width=2,height=100,width=250)
year_entry2.pack(pady= 20)
year_entry2.place(x=400,y=290)

my_lbl4.pack(pady=150)
my_lbl4.place(x=80,y=290)

btn1 = ctk.CTkButton(frame1,text="ENTER",font=('algerian',20),border_width=2)
btn1.place(x=450,y=500)

btn2 = ctk.CTkButton(frame1,text="CLEAR",font=('algerian',20),border_width=2)
btn2.place(x=150,y=500)

#manage events widgets

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival'
    )
myevent = 'treasure_hunt'
def clr_batch():


    cursor = mydb.cursor()
    query = f"truncate {myevent} "
    cursor.execute(query)
    mb.showinfo(message='cleared batch')



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql022004',
    database='carnival'
)

# Function to fetch data from the database

def fetch_data():
    cursor = mydb.cursor()
    query = f"SELECT name, phn_no FROM {myevent} "
    cursor.execute(query)
    return cursor.fetchall()

# Set up the main window


# Create a Treeview widget
tree = ttk.Treeview(frame3, columns=('Name', 'Phone Number'))
tree.heading('#0', text='Index')
tree.heading('Name', text='Name')
tree.heading('Phone Number', text='Phone Number')
tree.column('#0', width=100, stretch=tk.NO)  # Increase the width of the first column
tree.column('Name', width=200, stretch=tk.NO)  # Increase the width of the 'Name' column
tree.column('Phone Number', width=200, stretch=tk.NO)  # Increase the width of the 'Name' column


# Insert data into the Treeview widget
for index, (name, phone_number) in enumerate(fetch_data(), start=1):
    tree.insert('', 'end', text=str(index), values=(name, phone_number))
style = ttk.Style()
style.configure('Treeview', font=('Times', 16),background="gold",
                foreground="black",
                rowheight=40,
                fieldbackground="lightgrey",desired_height=150)
tree.configure(height=10)
tree.place(x=20,y=210)



# mbtn1 = ctk.CTkButton(frame3,text='FETCH CURRENT BATCH',fg_color='#213354')
# mbtn1.place(x=10,y=130)

mbtn2 = ctk.CTkButton(frame3,text='CLEAR CURRENT BATCH',fg_color='#213354',command=clr_batch)
mbtn2.place(x=10,y=520)

mlbl1 =ctk.CTkLabel(frame3,text='MANAGE EVENT...',font=("Gabriola", 65,"bold","italic"))
mlbl1.place(x=140,y=5)

# workspace
my_tab = ctk.CTkTabview(frame2,width=700,height=800,
                            border_width=2,
                             border_color='#bec9f1',
                             fg_color='white',text_color='black',
                             text_color_disabled='white',
                             segmented_button_unselected_color='#bec9f1',
                             segmented_button_fg_color='#bec9f1',
                             segmented_button_unselected_hover_color='#b7d6fd',
                             segmented_button_selected_color='#d6fdb7')
my_tab.pack(pady=10,expand=True,fill='both')
my_tab.configure(fg_color='#081548')
case_1 = my_tab.add('FEEDBACK \nGENERATOR')
case_2 = my_tab.add('IMAGE GALLERY')
case_3 = my_tab.add('VOLUNTEER \nBROADCAST')

#feedback creation
flbl = ctk.CTkLabel(case_1,text='Enter total no of questions',text_color='white')
flbl.place(x=10,y=2)
fe1 = ctk.CTkEntry(case_1,width=40,fg_color='#C0CCE2',text_color='black')
fe1.place(x=170,y=2)

class features:
    def que(self):
        frame = ctk.CTkFrame(case_1, fg_color='#081548', bg_color='#081548', height=500, width=700)
        frame.place(x=10, y=30)
        count = fe1.get()
        print(count)
        r = 10

        if (int(count) < 11):
            global entry_lst
            global entry1
            entry_lst = []
            format = []
            for i in range(int(count)):
                ctk.CTkLabel(frame, text='Q ', font=("Times", 30)).place(x=10, y=r)
                entry1 = ctk.CTkEntry(frame, width=500, fg_color='#C0CCE2', text_color='black')
                entry1.place(x=80, y=r)
                entry_lst.append(entry1)
                chk_box = ctk.CTkCheckBox(frame,text='',border_color='#C0CCE2',checkmark_color='white')
                chk_box.place(x=638,y=r)
                radio = ctk.CTkRadioButton(frame,text='',border_color='#C0CCE2',width=14)
                radio.place(x=597,y=r)
                r += 50



class features2(features):
    def gen(self):
        for i in entry_lst:
            print(i.get())

f1 = features()
f2 = features2()


ebtn = ctk.CTkButton(case_1,text="↵",font=('calibri',15),width=10,height=10,corner_radius=2000,command=f1.que)
ebtn.place(x=230,y=2)

#Vol broadcast
b_innerframe1 = ctk.CTkFrame(case_3,height=300,width=740,fg_color='#081548',border_width=2,border_color='white')
b_innerframe1.place(x=5,y=36)
blbl = ctk.CTkLabel(b_innerframe1,text='MESSAGE:',font=('Times',25,'italic'))
blbl.place(x=5,y=20)

btxtbox = ctk.CTkTextbox(b_innerframe1,width=520,height=200,border_width=3,fg_color='black',border_color='#CADDFF',text_color='grey',font=('calibri',20))
btxtbox.place(x=130,y=20)
ctk.CTkLabel(case_3,text='SEND',font=('Times',15,'bold')).place(x=5,y=0)
ctk.CTkButton(case_3,text='<',border_width=5,border_color='black',height=15,width=15).place(x=40,y=0)

def snd():
    message = btxtbox.get('1.0','end-1c')
    print(message)
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    mycursor.execute("truncate broadcast")
    mycursor.execute("INSERT INTO broadcast values('%s')"%btxtbox.get('1.0','end-1c'))
    mydb.commit()
    mydb.close()
    print('broadcast successfull')



bbtn = ctk.CTkButton(b_innerframe1,text='SEND',font=('Times',25,'bold'),fg_color='#CADDFF',text_color='Black',command=snd)
bbtn.place(x=495,y=250)

rbtn = ctk.StringVar(value='other')
brbtn1 = ctk.CTkRadioButton(b_innerframe1,text='ALERT',font=('Times',20),value='yes',variable=rbtn,border_color='red',fg_color='red')
brbtn1.place(x=5,y=250)
brbtn2 = ctk.CTkRadioButton(b_innerframe1,text='GENERAL',font=('Times',20),value='no',variable=rbtn,border_color='grey',fg_color='grey')
brbtn2.place(x=150,y=250)

gbtn = ctk.CTkButton(case_1,text='GENERATE',font=('Times',15,'italic','bold'),command=f2.gen,
                     fg_color='white',text_color='black',hover_color='grey')
gbtn.place(x=450,y=2)
rb = ctk.CTkLabel(case_1,text='🔘',font=('tahoma',20),fg_color='#081548')
rb.place(x=603,y=2)
my_tip =Hovertip(rb,"Answer Format: radio button")
txtlb = ctk.CTkLabel(case_1,text='Text',font=('tahoma',20),fg_color='#081548',text_color='grey')
txtlb.place(x=640,y=2)
txtlb =Hovertip(rb,"Answer Format: TEXT")


animated_panel = SlidePanel(window, 1.0, 0.7)
animated_panel.configure(fg_color='#C0CCE2',bg_color='#C0CCE2',height=1500,border_width=5)
ctk.CTkButton(animated_panel, text='HOME',text_color='#213354',fg_color='#CADDFF',border_width=2,border_color='#213354',width=200,hover_color='#C0CCE2',command=lambda: frame1.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='MANAGE BATCH',text_color='#213354' ,border_width=2,border_color='#213354',fg_color='#7DAAFB',width=200,hover_color='#C0CCE2',command=lambda: frame3.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='WORKSPACE',fg_color='#335BA2',border_width=2,border_color='#213354',text_color='white',width=200,hover_color='#C0CCE2',command=lambda: frame2.tkraise()).pack(  pady=10)
button_x = 0.5
button = ctk.CTkButton(window, text='☰', command=animated_panel.animate,height=10,width=2,fg_color='#213354',bg_color='black')
button.place(relx=0.98, rely=0.03, anchor='center')



# eventbox = tr.Entry(frame,font=['Arial',13])
# eventbox.gridrow=
window.mainloop()
