import tkinter as tk
from tkinter import ttk
from tkinter import *
import customerrec as cr


def chkin(t):
    Label(t, text="Name").grid(row=0, column=0)
    Label(t, text="Check in date").grid(row=1, column=0)
    Label(t, text="Check out date").grid(row=2, column=0)
    Label(t, text="Room No.").grid(row=3, column=0)

    name = Text(t, height=1, width=20)
    checkin = Text(t, height=1, width=20)
    checkout = Text(t, height=1, width=20)
    room = Text(t, height=1, width=20)

    name.grid(row=0, column=1)
    checkin.grid(row=1, column=1)
    checkout.grid(row=2, column=1)
    room.grid(row=3, column=1)

    def submit():
        cr.check_in(room.get("1.0", "end-1c"), name.get("1.0", "end-1c"), checkin.get("1.0", "end-1c"),
                    checkout.get("1.0", "end-1c"))

    Button(t, text="Submit", command=submit).grid(row=4, column=0)
