import tkinter as tk
from tkinter import filedialog
import mysql.connector
import ttkbootstrap as tb
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
window.configure(fg_color='#450202',bg_color='#213354')
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



frame4 = ctk.CTkFrame(window, fg_color='#690202', height=1000, width=700)
frame4.pack(side='top', expand=True, fill='x')
frame4.place(x=10)
frame4.tkraise()
print('event')

frame3 = ctk.CTkFrame(window, fg_color='#B90606', height=1000, width=700)
frame3.pack(side='top', expand=True, fill='x')
frame3.place(x=10)
frame3.tkraise()
print('event')

frame2 = ctk.CTkFrame(window,fg_color='#FF5757',height=1000,width=700)
frame2.pack(side='top',expand=True,fill='x')
frame2.place(x=10)
frame2.tkraise()
print('home')


frame1 = ctk.CTkFrame(window,fg_color='#FFDDDD',height=1000,width=700)
frame1.pack(side='top',expand=True,fill='x')
frame1.place(x=10)
frame1.tkraise()
print('home')



#animation
global my_y
my_y = 600/2 + 350

def up():
    global my_y
    my_y -= 20
    if my_y >= 400:
        create.place(x=700/2,y=my_y,anchor='center')
        window.after(5,up)
    my_button1.configure(text='-',command=down,font=('Times',50),height=25,width=25)
    pass
def down():
    global my_y
    my_y += 20
    if my_y <= 900:
        create.place(x=700 / 2, y=my_y, anchor='center')
        window.after(5, down)
    my_button1.configure(text="+", height=25, width= 25, corner_radius=10,font=('Times',40),command=up)

create = ctk.CTkFrame(frame1,fg_color='white',height=480,width=677,border_width=2,border_color='#DACACA',corner_radius=0)
create.place(x=10,y=my_y)



#animated frame widgets
def create_event():
    print(my_option.get(),year_entry1.get(),my_date1.entry.get(),my_date2.entry.get(),my_text.get(0.0,'end'))
    info = (my_option.get(),year_entry1.get(),my_date1.entry.get(),my_date2.entry.get(),my_text.get(0.0,'end'))
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival')
    mycursor = mydb.cursor()
    mycursor.execute("truncate event")
    query = f"INSERT INTO event values(%s,%s,%s,%s,%s)"
    mycursor.execute(query, info)
    mydb.commit()
    mydb.close()
    mb.showinfo(title='Successfull', message='Event Created Successfully !!!!')


lb1 =ctk.CTkLabel(create,text="Type of the event :",text_color='#430101',font=('Times',19,'bold','italic'))
lb1.place(x=5,y=5)
types = [ "College Fest","Technical Event","Expert Talk","Sports Event","Others"]
my_option =ctk.CTkOptionMenu(create, values=types,height=25,width=100,
                             corner_radius=10,fg_color='#430101',dropdown_fg_color='#DACACA',
                             dropdown_text_color='#430101',dropdown_hover_color='white',button_color='#430101',button_hover_color='red')
my_option.place(x=165,y=5)
lb2 =ctk.CTkLabel(create,
            text="Name of the event :",text_color='#430101',font=('Times',19,'bold','italic'))
lb2.place(x=5,y=50)

lb3 =ctk.CTkLabel(create,
            text="Date of the event :",text_color='#430101',font=('Times',19,'bold','italic'))
lb3.place(x=5,y=95)
my_date1 = tb.DateEntry(create, bootstyle="danger")
my_date1.place(x=200,y=120)
lb4 = ctk.CTkLabel(create,text='TO',font=('Times',25,'bold'),text_color='#430101')
lb4.place(x=350,y=93)
my_date2 = tb.DateEntry(create, bootstyle="danger")
my_date2.place(x=580,y=120)
year_entry1 = ctk.CTkEntry(create,text_color='#430101',fg_color='#DACACA',width=300)
year_entry1.place(x=170,y=50)
lb4 =ctk.CTkLabel(create,
            text="Event Tagline :",font=('Times',19,'bold','italic'),text_color='#430101')
lb4.place(x=5,y=150)
my_text = ctk.CTkTextbox(create,height=200,width=300,fg_color='#DACACA',
                         border_width=2,border_color='#430101',text_color='#430101' )
my_text.place(x=170,y=150)
btn1 = ctk.CTkButton(create,text='CREATE',fg_color='#430101',font=('Times',19,'bold'),hover_color='red',width=100,corner_radius=25,command=create_event)
btn1.place(x=200,y=370)
btn2 = ctk.CTkButton(create,text='CLEAR',fg_color='#430101',font=('Times',19,'bold'),hover_color='red',width=100,corner_radius=25)
btn2.place(x=320,y=370)


title_lbl = ctk.CTkLabel(frame1,text="--ADMIN HOMEPAGE--",font=("Gabriola", 65,"bold","italic"),text_color='Black',width=300)
title_lbl.place(x=100,y=0)

my_label2 =ctk.CTkLabel(frame1,
            text="CREATE EVENT :",text_color='black',font=('Times',25))
my_label2.place(x=40,y=130)

my_button1 =ctk.CTkButton(frame1,
            text="+", height=25, width= 25, corner_radius=25,font=('Times',40),fg_color='#430101',hover_color='red',command=up)
my_button1.place(x=310,y=121)
sym_lbl = ctk.CTkLabel(window,text='C',font=('Webdings',400),bg_color='#450202',height=600,width=100)
sym_lbl.place(x=710,y=100)
sym_lbl = ctk.CTkLabel(window,text='n',font=('Webdings',70),bg_color='#450202')
sym_lbl.place(x=760,y=80)

#Sponsor Advertisement widgets

def clear_banner():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival'
    )


    mycursor = mydb.cursor()
    sql = "truncate images"
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()
    mb.showinfo(title="SUCCESS", message='Banner Cleared Successfully !!!')


def upload_image():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filename:
        try:
            with open(filename, "rb") as img_file:
                img_data = img_file.read()

            # Connect to your MySQL database
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysql022004',
                database='carnival'
            )

            mycursor = mydb.cursor()
            # Insert the image data into the table
            sql = "INSERT INTO images (image_data) VALUES (%s)"
            mycursor.execute(sql, (img_data,))
            mydb.commit()  # Commit the changes

            mycursor.close()
            mydb.close()
            print("Image uploaded successfully!")
            mb.showinfo(title="SUCCESS", message='Image Uploaded Successfully !!!')
        except Exception as e:
            print(f"Error uploading image: {e}")
    else:
        mb.showinfo(title="TRY AGAIN", message="No file selected. Please choose an image.")


ctk.CTkLabel(frame4,text='''UPLOAD YOUR ADVERTISEMENT
BANNER''',font=('Times',40,'bold'),text_color='black',fg_color='#DACACA').place(x=5,y=10)
ctk.CTkLabel(frame4,fg_color='#690202',text='- maximum IMAGE size is 16mb',font=('Times',20,'bold'),text_color='white').place(x=5,y=130)
ctk.CTkLabel(frame4,fg_color='#690202',text='- supported IMAGE types are :- .JPEG,.JPG,.PNG',font=('Times',20,'bold'),text_color='white').place(x=5,y=170)
ctk.CTkLabel(frame4,fg_color='#690202',text='- one button corresponds to one Banner Display',font=('Times',20,'bold'),text_color='white').place(x=5,y=210)
ctk.CTkLabel(frame4,fg_color='#690202',text='- DIMENSIONS: Height =>400, Width => 210',font=('Times',20,'bold'),text_color='white').place(x=5,y=250)


button_upload = ctk.CTkButton(frame4, text="Upload Image",font=('Times',20,'italic'), command=upload_image,corner_radius=0,fg_color='grey',border_width=3,border_color='#DACACA',text_color='#FFDDDD',hover_color='dark grey')
button_upload.place(x=250,y=500)
button_upload = ctk.CTkButton(frame4, text="Clear Banner",font=('Times',20,'italic'), command=clear_banner,corner_radius=25,fg_color='grey',border_width=3,border_color='cyan',text_color='cyan',hover_color='dark grey')
button_upload.place(x=5,y=300)

#Manage Sub-events
ctk.CTkLabel(frame3,text='Assign Subevents....',text_color='white',font=('Times',35,'italic','bold')).place(x=5,y=5)
ctk.CTkLabel(frame3,text='Choose Volunteer :',text_color='white',font=('Times',25)).place(x=15,y=90)
ctk.CTkLabel(frame3,text='Attatch Event :',text_color='white',font=('Times',25)).place(x=15,y=150)
ctk.CTkEntry(frame3,fg_color='#DACACA').place(x=280,y=150)
types1 = []

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql022004',
    database='carnival'
)

cursor = mydb.cursor()
r = cursor.execute("SELECT vname FROM vol_login")
result = cursor.fetchall()
for row in result:
    for name in row:
        types1.append(name)
        break
print(types1)


my_option1 =ctk.CTkOptionMenu(frame3, values=types1,height=25,width=100,
                             corner_radius=10,fg_color='#430101',dropdown_fg_color='#DACACA',
                             dropdown_text_color='#430101',dropdown_hover_color='white',button_color='#430101',button_hover_color='red')
my_option1.place(x=280,y=90)
#create volunteer widgets
def deploy():
    params =(v_entry.get(),v_pass.get(),v_phn.get())
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql022004',
        database='carnival'
    )
    mycursor = mydb.cursor()
    query = f"INSERT INTO vol_login values(%s,%s,%s)"
    mycursor.execute(query, params)
    mydb.commit()
    mydb.close()
    mb.showinfo(title='SUCCESSFULL !!!',message='Volunteer Deployed Successfully !!!')

vtitle_lbl = ctk.CTkLabel(frame2,text="--CREATE VOLUNTEER--",font=("Gabriola", 55,"bold","italic"),text_color='#FFEBD3',width=300)
vtitle_lbl.place(x=100,y=0)

vmy_lbl1 =ctk.CTkLabel(frame2,font=("Times", 20,'bold'),fg_color='#FF5757',text_color='white',
            text="VOLUNTEER USERNAME:", height=30, width= 100)

v_entry = ctk.CTkEntry(frame2,text_color='red',bg_color='#FF5757',fg_color='#DACACA')
v_entry.pack(pady= 20)
v_entry.place(x=400,y=130)

vmy_lbl1.pack(pady=90)
vmy_lbl1.place(x=80,y=130)

vmy_lbl2 =ctk.CTkLabel(frame2,fg_color='#FF5757',font=("Times", 20,'bold'),text_color='white',bg_color='#FF5757',
            text="VOLUNTEER PASSWORD:", height=30, width= 100)
v_pass = ctk.CTkEntry(frame2,text_color='red',bg_color='#FF5757',fg_color='#DACACA')
v_pass.pack(pady= 20)
v_pass.place(x=400,y=180)
vmy_lbl2.pack(pady=150)
vmy_lbl2.place(x=80,y=180)

vmy_lbl3 =ctk.CTkLabel(frame2,fg_color='#FF5757',font=("Times", 20,'bold'),text_color='white',bg_color='#FF5757',
            text="VOLUNTEER PHONE NO.:", height=30, width= 100)
vmy_lbl3.place(x=80,y=230)
v_phn = ctk.CTkEntry(frame2,text_color='red',bg_color='#FF5757',fg_color='#DACACA')
v_phn.pack(pady= 20)
v_phn.place(x=400,y=230)
vdeploy = ctk.CTkButton(frame2,text='DEPLOY',font=('Times',18,'italic','bold'),command=deploy,
                        fg_color='#FFEBD3',width=100,hover_color='#DACACA',border_width=3,border_color='#FFD4A0',text_color='crimson')
vdeploy.place(x=250,y=280)













animated_panel = SlidePanel(window, 1.0, 0.7)
animated_panel.configure(fg_color='#DACACA',bg_color='#C0CCE2',height=1500,border_width=5,corner_radius=0)
ctk.CTkButton(animated_panel, text='HOME',text_color='#213354',fg_color='#FFDDDD',border_width=2,border_color='#213354',width=200,hover_color='grey',command=lambda: frame1.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='MANAGE VOLUNTEER',text_color='#213354' ,border_width=2,border_color='#213354',fg_color='#FF5757',width=200,hover_color='grey',command=lambda: frame2.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='MANAGE SUB-EVENTS',fg_color='#B90606',border_width=2,border_color='#213354',text_color='white',width=200,hover_color='grey',command=lambda: frame3.tkraise()).pack(  pady=10)
ctk.CTkButton(animated_panel, text='ADVERTISE',text_color='white' ,border_width=2,border_color='#213354',fg_color='#690202',width=200,hover_color='grey',command=lambda: frame4.tkraise()).pack( pady=10)

button_x = 0.5
button = ctk.CTkButton(window, text='☰', command=animated_panel.animate,height=10,width=2,fg_color='#430101',bg_color='black',hover_color='grey',border_color='#FFDDDD',border_width=2)
button.place(relx=0.98, rely=0.03, anchor='center')



# eventbox = tr.Entry(frame,font=['Arial',13])
# eventbox.gridrow=
window.mainloop()
