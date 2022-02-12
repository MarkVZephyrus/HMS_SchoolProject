from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("T.H.E. : Hotel Management Software")

tabs = ttk.Notebook(root)

checkin = ttk.Frame(tabs)
checkout = ttk.Frame(tabs)

tabs.add(checkin, text="Check In")
tabs.add(checkout, text="Check Out")

tabs.pack(expand=1, fill="both")

mainloop()