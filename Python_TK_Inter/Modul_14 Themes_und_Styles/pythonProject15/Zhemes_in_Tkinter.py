# Ce Code ne functionne pas car j ai pas pu avoir tous le Code la video

import tkinter as tk
from tkinter import ttk

class ExampleApp(tk.Tk):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

        self.geometry("400x400")
        self.title("Beispiel App")
        self.columnconfigure(0 , weight=1)
        self.rowconfigure(0 , weight=1)
        self.style = ttk.Style(self)
        print(self.style.theme_names())
        (self.style.theme_use("classic"))


        window1 = Frame1(self)
        window1.grid(row=0 , column = 0)




class Frame1(ttk.Frame):
    def __init__(self , container, controller ,  **kwargs):
        super().__init__(**kwargs)

        label = ttk.Label(self , text="+++ Das ist Frame 1" , relief="ridge").pack()
        button = ttk.Button(self , text="Wechsel zum Window 2" , command= lambda: controller.change_window(Frame1)).pack()



root = ExampleApp()
root.mainloop()