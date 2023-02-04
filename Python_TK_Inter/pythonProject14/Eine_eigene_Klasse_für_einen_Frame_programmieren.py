import tkinter as tk
from tkinter import ttk

def sey_hello():
    print("Hallo" + " "+ user_name.get())

#  Avec l ecriture user_name.get() nous permet d"acceder a la valeur user_name contenu dans textvariable

root = tk.Tk()
root. geometry("500x500")
root.title("Hauptfenster")

user_name = tk.StringVar()

# le stringvar permet a ce que le text que  l on eintrgen dans le EntryWidget soit imprimer sur la console
# tu vas au niveau du EntryWidget et tu le donne comme textvariable

input_frame = ttk.Frame()
input_frame.pack()

name_label = ttk.Label(input_frame , text="Name eingeben")
name_label.grid(column =0 , row=0)


name_entry = ttk.Entry(input_frame , textvariable= user_name)
name_entry.grid(column=1 , row=0)


sunmit_button = ttk.Button(input_frame , text="Abschicken" , command= sey_hello)
sunmit_button.grid( column=0 , row=1 , columnspan=2 , sticky="EW")



root.mainloop()