import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")


style = ttk.Style()
style.theme_use("classic")

paned_window = ttk.PanedWindow(root , orient= "horizontal")
paned_window.pack(fill="both"  , expand=True)

label1 = ttk.Label(root, text="Ich bin label 1")
label1.pack( side= "left")

label2 = ttk.Label(root ,text="Ich bin label 2" )
label2.pack( side = "left")

label3 = ttk.Label(root , text="Ich bin label 3")
label3.pack(side="left")

paned_window.add(label1)
paned_window.add(label2)
paned_window.add(label3)

root.mainloop()