import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("500x500")


selected_month = tk.StringVar()


month_cb = ttk.Combobox(root , textvariable=selected_month,  width = 30 , state = "readonly")


month_cb.configure( values = ("Januar"  , "Febuar" , "märz" , "April" , "juni" , "July" , "August") )
month_cb.pack()

show_value_label = ttk.Label(root , textvariable = selected_month)
show_value_label.pack()




root.mainloop()