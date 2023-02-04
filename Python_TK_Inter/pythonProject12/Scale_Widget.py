import tkinter as tk
from tkinter import ttk

def do_something(value): # on ajouter ce parametre car on avait un fehlermeldung a l ecran
    print("Aktueler Wert der Scale:" + str(scale_value.get())) # print der Wert auf der Konsole
    print("Alternativ:" + value) # cette est lier au parametre que l on ajouter
root = tk.Tk()
root.geometry("500x500")

scale_value = tk.DoubleVar(value = 10.0)  # valeur de depart

scale = ttk.Scale(root ,variable=scale_value,  orient="horizontal" , from_=0, to = 20,
                  command = do_something )

scale.pack(fill = "x")

show_scale_variable = ttk.Label(root , textvariable = scale_value)
show_scale_variable.pack()

root.mainloop()