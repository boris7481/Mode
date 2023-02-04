import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):                # concept d heritage
    def __init__(self):                 # ici on fait appel a la methode init de la classe  MainWindow
        super().__init__()              #  on fait appel a la methode init de la classe parent (tk.Tk)

        self.geometry("500x500")        # ici on fait appel a une methode la classe parent en passant par la classe enfant
        self.title("Hauptfenster")      # meme chose

        ttk.Label(self , text= "Ich bin ein Label").pack() # root est referencer ici par self: root est speichern dans le parametre self

root = MainWindow()                     # root est un objet de la classe MainWindow


root.mainloop()