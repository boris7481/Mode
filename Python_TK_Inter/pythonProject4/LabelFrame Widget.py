import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")

# label1 = ttk.Label(root , text = "Anderes Label" , font = (("Arial" , 25)))
# label1 = ttk.Button(root , text = "Anderes Label" )
label_frame = ttk.LabelFrame(root , text = "Label-Frame" , labelanchor="ne"
                             , padding = 10)
label_frame.grid(column=0 , row= 0)

button1 = ttk.Button(label_frame , text= "Du kannst mich klicken")
button1.grid(column = 0 , row = 0)

for item in label_frame.keys():
    print(item , ":" , label_frame[item])

root.mainloop()