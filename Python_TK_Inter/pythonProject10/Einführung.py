import tkinter as tk
from tkinter import  ttk

root = tk.Tk()
root.geometry("500x500")

button = ttk.Button(root , text = "Das ist ein Button")
button.place( x = 50 , y = 50)

root.mainloop()