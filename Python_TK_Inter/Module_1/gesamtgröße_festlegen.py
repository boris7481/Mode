import tkinter as tk

root = tk.Tk()
root.geometry("500x250")
# root.minsize(  height= 250 , width = 250)
# root.maxsize(height=750 , width = 750)
root.resizable(height = False , width = False)
labe1 = tk.Label(root , text = "das ist ein GUI")

labe1.pack()

root.mainloop()
