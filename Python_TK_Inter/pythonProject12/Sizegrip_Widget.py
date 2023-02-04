import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")
root.resizable(True , True)

root.columnconfigure(0 , weight=1) # cette ligne et celle du bas permettre de positioner le petit
root.rowconfigure(0 , weight=1) #  triangle en bas a droite du GUI


label = ttk.Label(root, text="Beispieltext" , font= ("Arial" , 30) , padding = 20)
label.grid(row = 0 , column = 0)

sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row = 1 , column=0 , sticky = "SE")




root.mainloop()