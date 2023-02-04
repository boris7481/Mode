import tkinter as tk
from tkinter import ttk

def print_increment(event):
    print("Spinbox wurde incrementiert")

def print_increment(event):
    print("Spinbox wurde decrementiert")

root = tk.Tk()
root.geometry("500x500")

sb_value = tk.IntVar( value = 2 )

#spinbox = ttk.Spinbox(root, from_=0 , to=20 , increment=0.5 , state = "readonly" ,
#                          textvariable= sb_value ) # from_ unterstricht wichtig
#spinbox.pack()

spinbox = ttk.Spinbox(root, values= (5, 10, 15, 20, 25) , state = "readonly" ,
                          textvariable = sb_value ) # from_ unterstricht wichtig
spinbox.pack()

spinbox.bind("<<Increment>>",  print_increment)
spinbox.bind("<<Decrement>>",  print_increment)


label = ttk.Label(root ,textvariable = sb_value )
label.pack()





root.mainloop()