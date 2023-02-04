import tkinter as tk
from tkinter import ttk

def hide_tab_2():
    notebook.hide(1)

def show_tab_2():
    notebook.add(frame2 , text="Tab 2")

def switch_to_tab_2():
    notebook.select(1)


root = tk.Tk()
root.geometry("500x500")

switch_button = ttk.Button(root, text = "Zu tab 2 swizchen"  ,  command= switch_to_tab_2)
switch_button.pack()


notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame1.pack()
frame2 = ttk.Frame(notebook)
frame2.pack()

label_frame1 = ttk.Label(frame1 , text = "Ich befinde mich im frame 1")
label_frame1.pack()
label_frame2 = ttk.Label(frame2 , text = "Ich befinde mich im frame 2")
label_frame2.pack()

button1_frame1 = ttk.Button(root , text = "Tab 2 verschwinden lassen" , command = hide_tab_2)
button1_frame1.pack()


button2_frame1 = ttk.Button(root , text = "Tab 2 wieder anzeigen" , command = show_tab_2)
button2_frame1.pack()

notebook.add( frame1 , text = "tab 1")
notebook.add( frame2 , text = "tab 2")


root.mainloop()