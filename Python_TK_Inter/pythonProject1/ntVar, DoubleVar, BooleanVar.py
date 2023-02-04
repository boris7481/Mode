import tkinter as tk
from tkinter import ttk
from PIL import Image ,ImageTk

root = tk.Tk()
root.geometry("400x400")
# text_variable = "text der variable"
# text_variable = tk.StringVar()
# text_variable = tk.IntVar()
# text_variable = tk.DoubleVar()
text_variable = tk.BooleanVar()
text_variable.set(True)
label1 = ttk.Label( root ,textvariable = text_variable)
label1.pack()

text_variable.set(False)

root.mainloop()