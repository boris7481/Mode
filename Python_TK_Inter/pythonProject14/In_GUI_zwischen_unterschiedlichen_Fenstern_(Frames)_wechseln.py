import tkinter as tk
from tkinter import ttk

class ExampleApp(tk.Tk):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

        self.geometry("400x400")
        self.title("Beispiel App")
        self.columnconfigure(0 , weight=1)
        self.rowconfigure(0 , weight=1)

        self.frame = {}


        window1 = Frame1(self  , self)
        window1.grid(row=0 , column = 0, sticky = "NSEW")

        window2 = Frame2(self , self)
        window2.grid(row=0 , column = 0 , sticky = "NSEW")

        self.frame[Frame1] = window1   # on speicher les frame dans le dictionaire
        self.frame[Frame2] = window2   # on affaire a une association key vakue pair ici

        self.change_window(Frame1)

    def change_window(self , container):
        frame = self.frame[container]
        frame.tkraise()


class Frame1(ttk.Frame):
    def __init__(self , container, controller ,  **kwargs):
        super().__init__(**kwargs)

        label = ttk.Label(self , text="+++ Das ist Frame 1" , relief="ridge").pack()
        button = ttk.Button(self , text="Wechsel zum Window 2" , command= lambda: controller.change_window(Frame2)).pack()


class Frame2(ttk.Frame):
    def __init__(self, container, controller,  **kwargs): # controller est responsable du changement de frame
        super().__init__(**kwargs)

        label = ttk.Label(self, text="+++ Das ist Frame 2", relief="ridge").pack()
        button = ttk.Button(self, text="Wechsel zum Window 1", command=lambda: controller.change_window(Frame1)).pack()




root = ExampleApp()
root.mainloop()