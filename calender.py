import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def enforce_constraint():
    start_date = start_cal.get_date()
    end_cal.config(minimum=start_date)

# Create the main window
root = tk.Tk()
root.title("Datepicker Constraint")

# Create a frame to hold the date entry widgets
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Create the start date entry widget
start_label = ttk.Label(frame, text="Start Date:")
start_label.grid(row=0, column=0, padx=5, pady=5)
start_cal = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
start_cal.grid(row=0, column=1, padx=5, pady=5)

# Create the end date entry widget
end_label = ttk.Label(frame, text="End Date:")
end_label.grid(row=1, column=0, padx=5, pady=5)
end_cal = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
end_cal.grid(row=1, column=1, padx=5, pady=5)

# Bind the constraint enforcement function to the date change event of the start date entry widget
start_cal.bind("<<DateEntrySelected>>", lambda event: enforce_constraint())

# Run the application
root.mainloop()
