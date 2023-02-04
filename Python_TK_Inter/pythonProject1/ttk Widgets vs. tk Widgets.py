import tkinter as tk
from tkinter import ttk
from PIL import Image ,ImageTk

root = tk.Tk()
root.geometry("400x400")
image = Image.open("Boris_bild_oth.PNG")
photo = ImageTk.PhotoImage(image)

#image2 = Image.open("Image_created_with_a_mobile_phone.png.webp").resize((200 ,200))
#photo2 = ImageTk.PhotoImage(image2)

# labe1 = ttk.Label(root , text="Hallo welt")
label1 = ttk.Label( root ,text = " Mein eigenes Bild" ,  image = photo , compound = "top" ,
                    padding=20 , relief= "solid" , borderwidth=10 , font = ( "Arial" , 20) , background = "red" )
label1.pack()
# labe1["image"] = photo2
# labe1["text"] = "neuer Text "

for item in label1.keys():
    print(item  ,  ":", label1[item])

root.mainloop()
