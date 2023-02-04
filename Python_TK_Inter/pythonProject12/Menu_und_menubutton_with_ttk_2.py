import tkinter as tk
from tkinter import ttk

def change_bg_to_green():
    root.configure( bg= "green")

def change_bg_to_red():
    root.configure( bg= "red")

def change_bg_to_blue():
    root.configure( bg= "blue")



root = tk.Tk()
root.geometry("500x500")

application_menu = tk.Menu(root)
root.configure(menu = application_menu)


# color_menu = tk.Menu(application_menu)

menu_button = ttk.Menubutton(root,  text="Whäle Hintergrungfarbe" , direction = "right")
# direction permet de derouler le sous menu a droite
menu_button.pack()


color_menu = tk.Menu(menu_button)
menu_button.configure(menu = color_menu )

color_menu.add_radiobutton(label="grün" , command = change_bg_to_green) # une seule action wird gemacht en plus
color_menu.add_separator()
color_menu.add_radiobutton(label="rot" , command = change_bg_to_red) # tu peut voir le Hacken sur loption choisit
color_menu.add_separator()
color_menu.add_radiobutton(label="blaue" , command = change_bg_to_blue)

for item in menu_button.keys():
    print(item , ":" , menu_button[item])
# application_menu.add_cascade(label="Wähle farbe" , menu = color_menu) # ici onn fait apparaitre le untermenu



root.mainloop()