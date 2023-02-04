import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

entry1 = ttk.Entry(root , width = 15)
entry1.pack()

entry_scroll = ttk.Scrollbar( root , orient= "horizontal" , command = entry1.xview )
entry_scroll.pack(fill = "x")

entry1.configure(xscrollcommand = entry_scroll.set )



root.mainloop()
