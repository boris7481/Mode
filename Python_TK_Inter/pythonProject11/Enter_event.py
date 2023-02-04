import  tkinter as tk
from tkinter import ttk

def show_suprise_label(event):
    ttk.Label(root , text = "Überraschung!").pack()

root = tk.Tk()
root.geometry("500x500")

label = ttk.Label(root , text = "Das ist ein Label" )
label.pack()

label.bind("<ButtonRelease>" , show_suprise_label)

root.mainloop()