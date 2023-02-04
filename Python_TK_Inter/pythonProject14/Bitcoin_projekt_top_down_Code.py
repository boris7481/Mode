import tkinter as tk
from tkinter import ttk
import requests



def calculated_price():
    try:
        response = requests.get(COINDESK_AOI_URL)
#       print(type(response))
        response_dict = response.json()
        print(type(response_dict))
        print(response_dict)
        current_bitcoin_price = response_dict["bpi"]["EUR"]["rate_float"]
        calculated_price_euro = float(bitcoin_entry.get()) * current_bitcoin_price
        euro_value.set("{:.2f}".format(calculated_price_euro))
 #       print(calculated_price_euro)

    except ValueError:
        print("bitte einen gültigen Zahlenwert eingeben!")

root = tk.Tk()
root.geometry("300x200")
root.title("Bitcoin-Preis-Rechner")

COINDESK_AOI_URL= " https://api.coindesk.com/v1/bpi/currentprice.json"
# euro_value = tk.StringVar()
euro_value = tk.StringVar( value="Hier wird dann der Preis in Euro angezeigt")

bitcoin_label = ttk.Label(root , text = "Anzahl Bitcoin" , font = (("Arial" , 15)))
bitcoin_label.pack(side= "top" , fill= "x" , padx= 5, pady=2)

bitcoin_entry = ttk.Entry(root , font = (("Arial" , 15)))
bitcoin_entry.pack(side="top" , fill="x" , padx=5 , pady=2)

euro_label = ttk.Label(root , text="Preis in Euro" , font= (("Arial" , 15)) )
euro_label.pack(side="top" , fill="x" , padx=5 , pady=2)

bitcoin_display = ttk.Label(root  , textvariable=euro_value , font= (("Arial" , 15)) )
bitcoin_display.pack(side="top" , fill="x" , padx=5 , pady=2)

calculate_button = ttk.Button(root , text= "Berechnung durchführen" ,
                              command = calculated_price)
calculate_button.pack(side="bottom" , fill="x" , padx=10 , pady=10)



root.mainloop()
