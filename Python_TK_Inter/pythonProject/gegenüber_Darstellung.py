import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

labe1 = tk.Label(root , text = "Label 1 " , bg = "green")
labe1.pack(side= "left" ,  expand= True , fill= "both" )

label2 = tk.Label(root , text = "Label 2" , bg ="red")
label2.pack(side="top" , expand=True ,  fill="both" )

label3 = tk.Label(root , text = "Label 3" , bg ="Blue")
label3.pack(side="left" , expand =True , fill="both" )

root.mainloop()