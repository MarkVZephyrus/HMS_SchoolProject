import tkinter as tk
from tkinter import *
import customerrec as cr

def submit():
    cr.check_in()

t = tk.Tk()
t.title("Check-In")
Label(text="Name").grid(row=0, column=0)
Label(text="Check in date").grid(row=1, column=0)
Label(text="Check out date").grid(row=2, column=0)
Label(text="Room No.").grid(row=3, column=0)

name = Text(t, height=1, width=20)
checkin = Text(t, height=1, width=20)
checkout = Text(t, height=1, width=20)
room = Text(t, height=1, width=20)

name.grid(row=0, column=1)
checkin.grid(row=1, column=1)
checkout.grid(row=2, column=1)
room.grid(row=3, column=1)

submit = Button(t, text="Submit", command=submit).grid(row=4, column=0)


mainloop()