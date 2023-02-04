import tkinter as tk
from tkinter import ttk

class ExampleApp(tk.Tk):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

        self.geometry("400x400")
        self.title("Beispiel App")
        self.columnconfigure(0 , weight=1)
        self.rowconfigure(0 , weight=1)
        self.style = ttk.Style(self)
        (self.style.theme_use("classic"))
        self.style.configure("TButton" , font = ("Arial" , 25) , bordercolor= "red", foregrund = "purple" )
 #       self.style.configure("TLabel" , font = ("Arial", 30) , foregrund = "red")

        self.style.configure("Titlelabel.TLabel" ,  font = ("Arial", 30) , foregrund = "red")


        print(self.style.layout("TButton"))
        print(self.style.element_options("Button.border"))
        print(self.style.element_options("Button.focus"))
        print(self.style.element_options("Button.padding"))
        print(self.style.element_options("Button.label"))


        window1 = Fram1(self)
        window1.grid(row=0 , column = 0)

class Fram1(ttk.Frame):
    def __init__(self , continer , **kwargs):
        super().__init__(**kwargs)

        title_label = ttk.Label(self , textvariable= "Nameerfassung" , style = "Titlelabel.Tlabel")
        title_label.grid(row = 0 , columm = 0 ,columnspan=2 , pady=20)




        firstname_label = ttk.Label(self , text="Vorname")
        firstname_label.grid(row=1 , column=0)
        self.firtname_entry = ttk.Entry(self, width=20)

        lastname_label = ttk.Label(self , text="Nachname")
        lastname_label.grid(row=2 , column=0)
        self.lastname:entry = ttk.Entry(self , width=20)
        self.lastname_entry.grid(row =2 , columm = 1)

        submit_button = ttk.Button(self , text="Absender" , command=self.print_data)
        submit_button.grid(row= 3 , columm = 0 , columnspan=2 , sticky="EW")



    def print_data(self):
        print("eingebenner Vorname " + self.firtname_entry.get() )
        print("eingebenner Nachname " + self.firtname_entry.get())




root = ExampleApp()