import  tkinter as tk
from  tkinter import ttk

def next_step():
    if pb["value"] < 100:
        pb["value"] += 10
    else:
        step_button.configure(state = tk.DISABLED)


root = tk.Tk()
root.geometry("500x500")
pb = ttk.Progressbar(root , orient = "horizontal" , length=300 , mode= "indeterminate")
pb.pack()

step_button = ttk.Button(root , text="Näschter Schritt" , command= next_step)
step_button.pack()

start_button = ttk.Button(root , text="Start" , command= pb.start)
start_button.pack()

step_button = ttk.Button(root ,  text="Stop" , command = pb.stop)
step_button.pack()

# pb.configure(value = 75)

for item in pb.keys():
    print(item , ":" , pb[item])

root.mainloop()