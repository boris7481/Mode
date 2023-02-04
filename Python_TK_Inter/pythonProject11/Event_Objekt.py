import  tkinter as tk
from tkinter import ttk

# def show_suprise_label(event):
#    print("Maus geklickt bei x = "   +  str(event.x) + "y=" + str(event.y) )
#    ttk.Label(root , text = "Überraschung!").pack()



#def show_suprise_label(event):
#    print("Maus geklickt bei x = "   +  str(event.x_root) + "y=" + str(event.y_root) )
#    print("Maustaste:" + str(event.num))
#    ttk.Label(root , text = "Überraschung!").pack()
# les coordonnees affichees ici sont relatif au Bildschirm de mon Destop

#label = ttk.Label(root , text = "Das ist ein Label" )
#label.pack()
#label.bind("<Double-Button-1>" , show_suprise_label )


#def show_suprise_label(event):
#    print("Gedrückte Tast: " + event.keysym)
#    print( "Zugehörige Keycode :" + str(event.keycode) ) # pour avoir les valeurs ASCI
#    ttk.Label(root , text = "Überraschung!").pack()


#entry = ttk.Entry(root , width = 60)
#entry.pack()
#entry.bind("<KeyPress>" , show_suprise_label )


def show_suprise_label(event):
    print(" Breite  " + str(event.width))
    print("Hohe" + str(event.height))
    ttk.Label(root, text="Überraschung!").pack()


root = tk.Tk()
root.geometry("500x500")


entry = ttk.Entry(root , width = 60)
entry.pack(fill = "x")

entry.bind("<Configure>" , show_suprise_label )



root.mainloop()