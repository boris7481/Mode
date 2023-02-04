import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("500x500")
root.columnconfigure(0 , weight=5)
root.columnconfigure(1 , weight=1)



def greet():
    greet_string = "Hallo" + " " +  nane_entry.get()
    ttk.Label(root , text= greet_string).grid(column=2 , row=2)

top_frame = ttk.Frame(root , padding=20 , relief= "ridge")
top_frame.grid(column = 0 , row = 0 , sticky="w" )


name_label = ttk.Label(top_frame , text = "Gebe einen Namen ein:")
name_label.grid( column = 0 ,  row = 0 )

nane_entry = ttk.Entry(top_frame)
nane_entry.grid(column = 1 , row = 0 , sticky="nsew")

test_label = ttk.Label(root)
test_label.grid(column = 0  , row = 5 )


greet_button = ttk.Button(root , text = "jetzt begrüßen" , command = greet , state="ew" )

greet_button.grid(column= 0 , row=1 ,  sticky="ew")

root.mainloop()