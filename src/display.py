from tkinter import *
from tkinter import messagebox
import _customer as cr
import locale
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')


def dsp(t):
    def _dsp(f, _re = False):
        if _re:
            for wid in f.winfo_children():
                wid.destroy()
            f.grid(row=1,column=0,columnspan=2)
        Label(f, text="Sr.No.", justify='center').grid(row=1, column=0)
        Label(f, text="Name", justify='center').grid(row=1, column=1)
        Label(f, text="Check in date", justify='center').grid(row=1, column=2)
        Label(f, text="Check out date", justify='center').grid(row=1, column=3) 
        Label(f, text="Room No.", justify='center').grid(row=1, column=4)
        n = 2
        for i in cr.customers.keys():
            Label(f, text=i, justify='center').grid(row=n, column=0)
            Label(f, text=cr.customers[i][1],
                justify='center').grid(row=n, column=1)
            Label(f, text=cr.customers[i][2],
                justify='center').grid(row=n, column=2)
            Label(f, text=cr.customers[i][3],
                justify='center').grid(row=n, column=3)
            Label(f, text=cr.customers[i][0],
                justify='center').grid(row=n, column=4)
            n += 1
    f = Frame(t)
    f.grid(row=1,column=0,columnspan=2)
    _dsp(f)
    Button(t, text="refresh", command=lambda: _dsp(f,True)).grid(row=0, column=0)
