import tkinter as tk
from tkinter import *
from tkinter import ttk
import _customer as cr
from tkinter import messagebox
import locale
import checkin as ci
import checkout as co
import display as dp
import meal as ml
import show as sh
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')

root = tk.Tk()
root.title("T.H.E. : Hotel Management Software")
root.geometry("600x400")

tabs = ttk.Notebook(root)

checkin = ttk.Frame(tabs)
checkout = ttk.Frame(tabs)
display = ttk.Frame(tabs)
meals = ttk.Frame(tabs)
shows = ttk.Frame(tabs)

tabs.add(checkin, text="Check In")
tabs.add(checkout, text="Check Out")
tabs.add(display, text="Display")
tabs.add(meals, text="Meals")
tabs.add(shows, text="Show")

tabs.pack(expand=1, fill="both")

ci.chkin(checkin)
co.chkout(checkout)
dp.dsp(display)
ml.ml(meals)
sh.shw(shows)

mainloop()
