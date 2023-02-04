import tkinter as tk
from tkinter import ttk
#def print_entry_imput():
#    print(entry1.get())

def print_entry_imput():
    ttk.Label(root , text = entry1.get()).pack()

root = tk.Tk()
root.geometry("500x500")
entry1 = ttk.Entry(root , width=40)
entry1.pack()

entry1.insert(0 ," schreib etwas ")
entry1.insert(2 ,"TESTEN")

button2 = ttk.Button(root , text = "Eingabe eingeben" , command= print_entry_imput)
button2.pack()

for item in entry1.keys():
    print(item , ":",  entry1[item])

root.mainloop()