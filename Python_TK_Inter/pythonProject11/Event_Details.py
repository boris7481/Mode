import  tkinter as tk
from tkinter import ttk

def show_suprise_label(event):
    ttk.Label(root , text = "Überraschung!").pack()

root = tk.Tk()
root.geometry("500x500")

label = ttk.Label(root , text = "Das ist ein Label" )
label.pack()

# root.bind("<Control-KeyPress-q>" , show_suprise_label)
# root.bind("<Control-KeyPress-3>" , show_suprise_label)

#label.bind("<Double-Button-1>" , show_suprise_label) # 2 fois le linksMousTaske pour trigert l,Event

# label.bind("<Double-Button>" , show_suprise_label )
# ca function  avec links , recht et la souris le rechclick de cette facon
label.bind("<Double-Button-3>" , show_suprise_label ) # declanche levenement avec le rechtklic
# label.bind("<Double-Button-1>" , show_suprise_label )  # linksklick deux fois

root.mainloop()