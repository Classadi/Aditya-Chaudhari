import tkinter as tr

def login():
    print("Log In button clicked")

def registration():
    print("Registration button clicked")

window = tr.Tk()
window.title("Carnival")
window.geometry('800x400')
window.configure(bg='#fac6c6')

# Create a frame to hold the Carnival label
carnival_frame = tr.Frame(window, bg='#fac6c6')
carnival_frame.pack(side="left", fill="both", expand=True)

# Create a label for the Carnival name with a stylish font
carnival_label = tr.Label(carnival_frame, text="Carnival", font=("happy camper", 100), bg='#fac6c6', fg='#FF3399')
carnival_label.pack(expand=True, pady=(20, 0))  # Reduce top padding

# Create a label for the tagline directly below the Carnival label
tagline_label = tr.Label(carnival_frame, text="Event Start With Us...", font=("Arial", 36), bg='#fac6c6', fg='#333333')
tagline_label.pack(expand=True)

# Create a frame to hold the buttons
button_frame = tr.Frame(window, bg='#fac6c6')
button_frame.pack(side="top", anchor="ne")

# Create Log In button
login_button = tr.Button(button_frame, text="Log In", bg="#FF3399", font=("Arial", 14), command=login)
login_button.pack(side="right", padx=10, pady=5)

# Create Registration button
registration_button = tr.Button(button_frame, text="Registration", bg="#FF3399", font=("Arial", 14), command=registration)
registration_button.pack(side="right", padx=10, pady=5)

window.mainloop()
