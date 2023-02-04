import  tkinter as tk
from  tkinter import ttk
import  time

def next_step():
    for task in range(10):
        pb["value"] += 10
        root.update()
        time.sleep(0.2)


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