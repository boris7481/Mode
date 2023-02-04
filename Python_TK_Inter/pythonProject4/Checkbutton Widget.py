import tkinter as tk
from tkinter import ttk

def react_to_checkbutton_interaction():
    print("Option an oder abgewählt")
    checkbotton1.configure(state = "disabled") # tk.DISABLED


root = tk.Tk()
root.geometry("500x500")
selected_option = tk.IntVar()

checkbotton1 = ttk.Checkbutton( root ,
                               text =  "Option1" ,
                               variable=selected_option,
                               command = react_to_checkbutton_interaction,
                               onvalue = "On" ,
                               offvalue = "Off",
                                state= tk.DISABLED
                               )
checkbotton1.pack()

for item in checkbotton1.keys():
    print(item, ";" , checkbotton1[item])

root.mainloop()