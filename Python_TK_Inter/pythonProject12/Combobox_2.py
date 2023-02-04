import tkinter as tk
from tkinter import ttk

def handle_selected(event):
    print("Aktueller monat :" + selected_month.get())
    print(month_cb.current())
    print(month_cb.get())

def change_option():
    month_cb.configure(values=("september" , "Oktober" , "November" , "Dezember"))

root = tk.Tk()
root.geometry("500x500")


selected_month = tk.StringVar()


month_cb = ttk.Combobox(root , textvariable=selected_month,  width = 30 , state = "readonly",
                        postcommand = change_option )

month_cb.configure( values = ("Januar"  , "Febuar" , "märz" , "April" , "juni" , "July" , "August") )
month_cb.pack()

show_value_label = ttk.Label(root , textvariable = selected_month)
show_value_label.pack()

month_cb.bind("<<ComboboxSelected>>" , handle_selected)


root.mainloop()