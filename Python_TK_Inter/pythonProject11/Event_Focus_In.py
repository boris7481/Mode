import  tkinter as tk
from tkinter import ttk

def show_suprise_label(event):
    ttk.Label(root , text = "Überraschung!").pack()

root = tk.Tk()
root.geometry("500x500")

label = ttk.Label(root , text = "Das ist ein Label" )
label.pack()

entry = ttk.Entry(root , width = 60)
entry.pack()

entry2 = ttk.Entry(root , width = 60)
entry2.pack()

label.bind("<FocusOut>" , show_suprise_label)
# il ya un pb ici ca ne done pas le text Überaschung comme pour la video donc a revoir
# label.bind("<FocusIn>" , show_suprise_label) # Der event ist am label gebunden
# root.bind("<KeyPress>" , show_suprise_label) # Taste auf TastaturNB der  event ist am Root gebunden

root.mainloop()