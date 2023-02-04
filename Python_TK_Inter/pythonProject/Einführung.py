import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

labe1 = tk.Label(root , text = "Label 1 " , bg = "green")
labe1.pack(side= "bottom" , fill= "both" , expand = True)

label2 = tk.Label(root , text = "Label 2" , bg ="red")
label2.pack(side="bottom" , fill="both" , expand = True)

label3 = tk.Label(root , text = "Label 3" , bg ="Blue")
label3.pack(side="bottom" , fill="both" , expand = True)

root.mainloop()

