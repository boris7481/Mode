import tkinter as tk
from tkinter import  ttk

root = tk.Tk()
root.geometry("500x500")

style = ttk.Style()
style.theme_use("clam")

button = ttk.Button(root , text = "Das ist ein Button")
button.place( relx = 0.5 , rely = 0.5 , relwidth= 0.1 , relheight=0.4 , anchor="nw")

root.mainloop()