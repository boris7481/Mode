import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")    # vu que l on appel ces deux methides  a l"interieur de notre MainWindow
                                    # alors il faut use le nom self  a la place de root
        self.title("Hauptfenster")

        InputFrame(self).pack()     # ici on erzeugen le Frame directement dans la methode init des Hauptfenster
                                    # En faisant cela en unifi les deux classes

class InputFrame(ttk.Frame):
    def __init__(self , container):
        super().__init__(container)

        self.user_name = tk.StringVar()

        name_label = ttk.Label(self, text="Name eingeben")
        name_label.grid(column=0, row=0)

        name_entry = ttk.Entry(self, textvariable=self.user_name)
        name_entry.grid(column=1, row=0)

        sunmit_button = ttk.Button(self, text="Abschicken", command=self.sey_hello)
        sunmit_button.grid(column=0, row=1, columnspan=2, sticky="EW")

    def sey_hello(self):
        print("Hallo" + " " + self.user_name.get() )

# root = tk.Tk() on le remplace par la classe MainWindow

root = MainWindow()

# input_frame = InputFrame(root)
# input_frame.pack()


root.mainloop()