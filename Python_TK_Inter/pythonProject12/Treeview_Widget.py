import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

style = ttk.Style()
style.theme_use("clam")

example_tree = ttk.Treeview(root)
example_tree.pack()

example_tree.configure(columns=( "firstname" , "lastname" , "phone" ))
example_tree.heading("#0" , text="true colum") #  le symbol #0 est un symbol particulier pour la premiere colonne
example_tree.heading("firstname" , text="Vorname")
example_tree.heading("lastname" , text="Nachname")
example_tree.heading("phone" , text = "Telefonummer")

# Spalten konfigurieren
example_tree.column("#0" , width=100)
example_tree.column("firstname" , width=100)
example_tree.column("lastname" , width=100 , minwidth=80) # mindestens 80 pixcel gros sein
example_tree.column("phone" , width=150)


# Daten Hinzufügen
#example_tree.insert( parent = "" , index = 0 , text="item_0" , values = ("Boris", "Thibaut" , "017628059114"))
#example_tree.insert( parent = "" , index = 1 , text="item_1" , values = ("Hermann", "Gadjui" , "017628059116"))
##xample_tree.insert( parent = "" , index = "end" , text="item_2" , values = ("Davila", "Nengoue" , "017628059117")) # il sera toujours a la dernier ligne


print(example_tree.insert( parent = "" , index = 0 , text="item_0" , values = ("Boris", "Thibaut" , "017628059114"))) # le rückgabewert nous aide pour le sub:item
example_tree.insert( parent = "" , index = 1 , text="item_1" , values = ("Hermann", "Gadjui" , "017628059116"))
example_tree.insert( parent = "" , index = "end" , text="item_2" , values = ("Davila", "Nengoue" , "017628059117"))

example_tree.insert(  parent = "I001" , index="end" , text="sub_item_0" , values = ( "georvanie", "Kabiwala" , "017628059118") )

print(example_tree.insert(parent = "I001" , index="end" , text="sub_item_0"))
example_tree.insert(parent = "I004" , index="end" , text="sub_sub_item_0")
# example_tree.insert(parent = "I001" , index="end" , text="sub_item_1") pour un sous sous menu

root.mainloop()