import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

labe1 = tk.Label(root , text = "Label 1 " , bg = "green")
labe1.pack(pady=10  , padx= 10 , ipady=30 ,  fill = "both")

label2 = tk.Label(root , text = "Label 2" , bg ="red")
label2.pack(pady=10   , ipadx=30)

root.mainloop()