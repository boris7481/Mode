import tkinter as tk
from tkinter import ttk

def handle_event(event):
    ttk.Label(root , text = "Custom Event wurde ausgeführt").pack()

root = tk.Tk()
root.geometry("500x500")

label = ttk.Label(root , text = " Das ist ein label")
label.pack()

label.event_add("<<CustomEvent>>" , "<Button-1>" , "<Button>") # getriegert mit den beden Maustasten
label.bind("<<CustomEvent>>" ,  handle_event)


root.mainloop()