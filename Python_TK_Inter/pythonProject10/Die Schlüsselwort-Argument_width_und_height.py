import tkinter as tk
from tkinter import  ttk

root = tk.Tk()
root.geometry("500x500")

style = ttk.Style()
style.theme_use("clam")

button = ttk.Button(root , text = "Das ist ein Button")
button.place( x = 250 , y = 250 , width = 200 , height = 200)

root.mainloop()