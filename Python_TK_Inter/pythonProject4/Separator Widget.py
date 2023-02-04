import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

button1 = ttk.Button(root , text = "Button 1")
button1.grid(column= 0 , row = 0 )

separaror = ttk.Separator(root)

button2 = ttk.Button(root ,  text = "Button 2")
button2.grid(column= 0 , row= 1, rowspan=2 , sticky= "ns")


root.mainloop()