import tkinter as tk
from tkinter import *
from tkinter import ttk
import _customer as cr
import locale
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')


def ml(t):
    def _ml(srno):
        Label(t, text="Adding Meal For: {}".format(cr.customers[srno][1]), justify="left").grid(
            row=1, column=0, columnspan=2)
        options = list(cr.meals.keys())
        v = StringVar()
        v.set(options[0])

        drop = OptionMenu(t, v, *options, command=lambda x: Label(t, text="Price : {}".format(
            locale.currency(cr.meals[v.get()]))).grid(row=3, column=0))
        # TypeError: <lambda>() takes 0 positional arguments but 1 was given
        # | if i remove that x after lambda, dunno how to fix it
        drop.grid(row=2, column=1)

        def _add():
            cr.customers[srno][5][v.get()] = cr.meals[v.get()]
        Button(t, text="Add", command=_add).grid(row=4, column=1)
        cr.customers[srno][5][v.get()] = cr.meals[v.get()]

    Label(t, text="Sr.No.", justify='center').grid(row=0, column=0)
    srno = Text(t, height=1, width=10)
    srno.grid(row=0, column=1)
    Button(t, text="Submit", command=lambda: _ml(
        srno.get('1.0', 'end-1c'))).grid(row=0, column=2)
