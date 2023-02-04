import tkinter as tk
from tkinter import ttk
import requests

class BitcoinPreisConverter(tk.Tk):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

        self.geometry("300x200")
        self.title("Bitcoin-Preis-Rechner")


        BitcoinToEuro(self).pack(fill="both")


class BitcoinToEuro(ttk.Frame):

    def __init__(self , container , **kwargs):
        super().__init__(container , **kwargs)

        self.COINDESK_AOI_URL = " https://api.coindesk.com/v1/bpi/currentprice.json"
        self.euro_value = tk.StringVar(value="Hier wird dann der Preis in Euro angezeigt")

        bitcoin_label = ttk.Label(self, text="Anzahl Bitcoin", font=(("Arial", 15)))
        bitcoin_label.pack(side="top", fill="x", padx=5, pady=2)

        self.bitcoin_entry = ttk.Entry(self, font=(("Arial", 15)))
        bitcoin_entry.pack(side="top", fill="x", padx=5, pady=2)

        euro_label = ttk.Label(self, text="Preis in Euro", font=(("Arial", 15)))
        euro_label.pack(side="top", fill="x", padx=5, pady=2)

        bitcoin_display = ttk.Label(self, textvariable=self.euro_value, font=(("Arial", 15)))
        bitcoin_display.pack(side="top", fill="x", padx=5, pady=2)

        calculate_button = ttk.Button(self, text="Berechnung durchführen",
                                      command=self.calculated_price)
        calculate_button.pack(side="bottom", fill="x", padx=10, pady=10)


    def calculated_price(self):
        try:
            response = requests.get(self.COINDESK_AOI_URL)
    #       print(type(response))
            response_dict = response.json()
            print(type(response_dict))
            print(response_dict)
            current_bitcoin_price = response_dict["bpi"]["EUR"]["rate_float"]
            calculated_price_euro = float(self.bitcoin_entry.get()) * current_bitcoin_price
            self.euro_value.set("{:.2f}".format(calculated_price_euro))
        except ValueError:
            print("bitte einen gültigen Zahlenwert eingeben!")

root = BitcoinPreisConverter()



root.mainloop()
