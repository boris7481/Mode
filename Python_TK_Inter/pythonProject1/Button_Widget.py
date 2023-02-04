import tkinter as tk
from tkinter import ttk
from PIL import Image ,ImageTk
def say_hello():
    print("danke , dass du mich gecklick hast")

root = tk.Tk()
root.geometry("500x500")
image = Image.open("Boris_bild_oth.PNG").resize((20 , 20))
photo = ImageTk.PhotoImage(image)
button1 = ttk.Button(root, text = "click mich bitte " , image= photo, compound="left" , padding = 20,
                     command=say_hello)
quit_button = ttk.Button(root , text = "Programm beenden" , command = root.destroy , state= tk.NORMAL)
quit_button.pack()
button1.pack(fill = "x")


for item in button1.keys():
    print(item, ":" , button1[item])

root.mainloop()

