import tkinter as tk
from tkinter import ttk

class InputFrame(ttk.Frame):
    def __init__(self , container): # on transmet le container a root a niveau de imput_frame root est notre hauptfenster
                                    # le container contient root , Ensuite on transmet le container au niveau de la
                                    # methode __init__ de la classe parent ttk.Frame
        super().__init__(container) # on fait appel a la methode init de la classe parent ttk.Frame

        self.user_name = tk.StringVar()  # user_name devient un Attribut der InputFrame

        name_label = ttk.Label(self, text="Name eingeben") # mit self referenzieren wir den frame Instance, die wir
        name_label.grid(column=0, row=0)                   # mit unserer Klasse erzeugen.

        name_entry = ttk.Entry(self, textvariable=self.user_name)
        name_entry.grid(column=1, row=0)

        sunmit_button = ttk.Button(self, text="Abschicken", command=self.sey_hello)
        sunmit_button.grid(column=0, row=1, columnspan=2, sticky="EW")

    def sey_hello(self):             # say_hello devient une methode de notre classe
        print("Hallo" + " " + self.user_name.get() )

#
root = tk.Tk()
root. geometry("500x500")
root.title("Hauptfenster")

user_name = tk.StringVar()


input_frame = InputFrame(root) # input_frame ist jetzt eine Kopie von der Klasse ttk.Frame
input_frame.pack()


root.mainloop()