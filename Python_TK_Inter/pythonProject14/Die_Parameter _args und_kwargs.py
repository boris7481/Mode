import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self , *args ,**kwargs):   # pour qu on puisse manipiler les objets de la classe Mainloop
        super().__init__(*args , **kwargs)
                                            # *arg steht für Positionbezogene Argumente
                                            # **kwarg steht für Keywort Argumente
        self.geometry("500x500")
        self.title("Hauptfenster")

        InputFrame(self , padding=20).pack()


class InputFrame(ttk.Frame):
    def __init__(self , container , **kwargs):
        super().__init__(container , **kwargs)

        self.user_name = tk.StringVar()

        name_label = ttk.Label(self, text="Name eingeben")
        name_label.grid(column=0, row=0)

        name_entry = ttk.Entry(self, textvariable=self.user_name)
        name_entry.grid(column=1, row=0)

        sunmit_button = ttk.Button(self, text="Abschicken", command=self.sey_hello)
        sunmit_button.grid(column=0, row=1, columnspan=2, sticky="EW")

    def sey_hello(self):
        print("Hallo" + " " + self.user_name.get() )


root = MainWindow()

# frame2 = ttk.Frame(root , padding=20)

root.mainloop()