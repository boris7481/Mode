import  tkinter as tk
from tkinter import ttk

def show_suprise_label(event):
    ttk.Label(root , text = "Überraschung!").pack()

root = tk.Tk()
root.geometry("500x500")

label = ttk.Label(root , text = "Das ist ein Label" )
label.pack()

# label.bind("<MouseWheel>" , show_suprise_label) # Der event ist am label gebunden
label.bind("<Configure>" , show_suprise_label) # Der event ist am label gebunden
# root.bind("<KeyPress>" , show_suprise_label) # Taste auf TastaturNB der  event ist am Root gebunden

root.mainloop()