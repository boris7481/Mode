import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

text = tk.Text( root , height = 6)
text.grid(column = 0 ,  row = 0)

text_scroll = ttk.Scrollbar( root , orient= "vertical" , command = text.yview)
text_scroll.grid(column = 1 , row = 0 , sticky = "ns")

text.configure(yscrollcommand = text_scroll.set )



for item in text.keys():
    print(item, ":" , text[item])



root.mainloop()
