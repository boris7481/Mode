import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("500x500")
root.columnconfigure(0 , weight=1)
root.columnconfigure(1 , weight=1)
root.rowconfigure(0 , weight=1)
root.rowconfigure(5 , weight=1)
#style = ttk.Style()
#style.theme_use("clam")

def greet():
    greet_string = "Hallo" + " " +  nane_entry.get()
    ttk.Label(root , text= greet_string).grid(column=1 , row=1)

name_label = ttk.Label(root , text = "Gebe einen Namen ein:")
name_label.grid(row= 0 , column = 0)

nane_entry = ttk.Entry(root)
nane_entry.grid(row = 0 , column = 1 , sticky="nsew")

test_label = ttk.Label(root , text ="TEST")
test_label.grid(column = 0  , row = 5 )

greet_button = ttk.Button(root , text = "jetzt begrüßen" , command = greet , state="ew" )

greet_button.grid(column= 1 , row=5 , pady= 20 ,  sticky="ew")

root.mainloop()