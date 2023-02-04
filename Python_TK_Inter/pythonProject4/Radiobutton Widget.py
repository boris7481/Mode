import tkinter as tk
from tkinter import ttk

def print_current_value():
    print(selected_option.get())

root = tk.Tk()
root.geometry("500x500")

selected_option = tk.StringVar()

rb1 = ttk.Radiobutton( root ,
                      text = "Option1 1" ,
                      variable= selected_option,
                      value= "value von option 1",
                      command = print_current_value)
rb1.pack()

rb2 = ttk.Radiobutton( root ,
                      text = "Option1 2" ,
                      variable = selected_option,
                      value = "value von option 2",
                      command = print_current_value)
rb2.pack()

rb3 = ttk.Radiobutton( root ,
                      text = "Option1 3" ,
                      variable = selected_option,
                      value = "value von option 3",
                      command = print_current_value)
rb3.pack()

for item in rb3.keys():
    print(item , ":" , rb3[item])

root.mainloop()