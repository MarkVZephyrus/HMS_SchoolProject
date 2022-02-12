import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customerrec as cr
import locale
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')

tk = tk.Tk()

Label(text="SrNo").grid(row=0, column=0)
srno = Text(tk, height=1, width=20)
srno.grid(row=0, column=1)


def get_data():
    r = cr.check_out(srno.get("1.0", "end-1c"))
    if r == -1:
        messagebox.showinfo("Error", "Room not found")
    else:
        name.config(text=r[1])
        checkin.config(text=r[2])
        checkout.config(text=r[3])
        room.config(text=r[0])
        n = 7
        netCost = 0
        for i in r[5].keys():
            netCost += r[5][i]
            Label(text="{}".format(i)).grid(row=n, column=0)
            Label(text="{}".format(locale.currency(r[5][i]))).grid(
                row=n, column=1)
            n += 1
        Label(text="____________________________________________________________________________",
              justify='center').grid(row=n, column=1)
        Label(text="Net Cost").grid(row=n+1, column=0)
        Label(text="{}".format(locale.currency(netCost))).grid(row=n+1, column=1)


Button(text="Submit", command=get_data).grid(row=0, column=2)

Label(text="The Grand Budapest Hotel", justify='center',
      font=("Helvetica", 20)).grid(row=1, column=1)
Label(text="Customer Name : ", justify='left',).grid(row=2, column=0)
Label(text="Check in date : ", justify='left',).grid(row=3, column=0)
Label(text="Check out date : ", justify='left',).grid(row=4, column=0)
Label(text="Room No. : ", justify='left',).grid(row=5, column=0)
Label(text="____________________________________________________________________________",
      justify='center').grid(row=6, column=1)

name = Label(text="", justify='left')
checkin = Label(text="", justify='left')
checkout = Label(text="", justify='left')
room = Label(text="", justify='left')
name.grid(row=2, column=1)
checkin.grid(row=3, column=2)
checkout.grid(row=4, column=2)
room.grid(row=5, column=2)

mainloop()
