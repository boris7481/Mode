import tkinter as tk
from tkinter import ttk

def remove_all_items():
    for item in example_tree.get_children(): # nous permet d avoir les index des sous menu
         example_tree.delete(item)

def remove_one_item():
    selected_item = example_tree.selection()[0]  # le premier button selectioner sera eliminer
    # la methode selection nous donne l index de l item selectioner c est un tuple je crois
    print(selected_item)
    example_tree.delete(selected_item)

def remove_all_selected_item():
    selected_items = example_tree.selection() # liste de tuple
    for item in selected_items:
        example_tree.delete(item)

def handle_event(event): # l" argument event est res important
    print("Event wurde getrigert")


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




print(example_tree.insert( parent = "" , index = 0 , text="item_0" , values = ("Boris", "Thibaut" , "017628059114"))) # le rückgabewert nous aide pour le sub:item
example_tree.insert( parent = "" , index = 1 , text="item_1" , values = ("Hermann", "Gadjui" , "017628059116"))
example_tree.insert( parent = "" , index = "end" , text="item_2" , values = ("Davila", "Nengoue" , "017628059117"))
example_tree.insert(  parent = "I001" , index="end" , text="sub_item_0" , values = ( "georvanie", "Kabiwala" , "017628059118") )
print(example_tree.insert(parent = "I001" , index="end" , text="sub_item_0"))
example_tree.insert(parent = "I004" , index="end" , text="sub_sub_item_0")
# example_tree.insert(parent = "I001" , index="end" , text="sub_item_1") pour un sous sous menu

remove_all_button = ttk.Button(root , text="Alle Items entfernen" , command = remove_all_items )
remove_all_button.pack()

remove_one_button = ttk.Button(root , text="Ein selected Item enfernen" , command = remove_one_item)
remove_one_button.pack()

remove_all_selected_button =ttk.Button(root , text="Ale selected item entfernen" , command= remove_all_selected_item )
remove_all_selected_button.pack()

# example_tree.bind( "<<TreeviewSelect>>" , handle_event ) # event getrigert quand tu selectionnes juste un item
# example_tree.bind( "<<TreeviewOpen>>" , handle_event ) # l evenement ci est getrigert quand tu veut voir le sub_item

example_tree.bind( "<<TreeviewClose>>" , handle_event ) # event getrigert quand on ferme le menu deroulant (la petite fleche )


root.mainloop()