import tkinter as tk

root = tk.Tk()
monitor_center_X = root.winfo_screenwidth()/2 - 250
monitor_center_y  = root.winfo_screenheight()/2 - 250

# root.geometry("500x500+" + str(int(monitor_center_X)) + "+" + str(int(monitor_center_y)))
root.geometry("500x500+%d+%d" % (monitor_center_X, monitor_center_y))
# root.minsize(  height= 250 , width = 250)
# root.maxsize(height=750 , width = 750)
root.resizable(height = True , width = False)
labe1 = tk.Label(root , text = "das ist ein GUI")

labe1.pack()

root.mainloop()
