class vara:
    # Specifierade 'float' för pris så att man inte försökte räkna ut med
    # sträng eller dylikt
    def __init__(self, namn, varukod, pris: int):
        self.namn = namn
        self.varukod = varukod
        self.pris = pris

    def getvarukod(self):
        return self.varukod

    def __str__(self):
        # Ändrade utskriften för att snygga till utskriften av ordern
        return f" ({self.varukod}) {self.namn}: {self.pris} kr"

    def modify_vara(lst_varor):
        '''Ändrar namn och pris på "vara" objekt i angiven lista med varor
        args: lista med objekt av typen vara
        '''
        found = False # För att felhantera felaktig varukod
        sku = input("Ange varukod på vara du vill ändra > ").upper()
        for i in lst_varor:
            if sku == i.getvarukod():
                found = True
                nytt_namn = input("Ange nytt namn till varan > ")
                i.namn = nytt_namn
                while True: # För att felhantera omvandling av pris till int
                    try:
                        nytt_pris_str = input("Ange nytt pris till vara > ")
                        nytt_pris = int(nytt_pris_str)
                        i.pris = nytt_pris
                        break  # Bryt loopen om omvandlingen till int lyckades
                    except ValueError:
                        print(nytt_pris_str, "är inte ett giltigt pris. Försök igen.")
        if found == True:
            print(sku, "har ändrats.")
        else:
            print(sku, "är inte en giltig varukood")

class Order(list):
    '''
    Genererar ett ordernummer och ett totalpris
    för en lista med objekt av typen vara.
    '''
    next_order_no = 1

    def __init__(self, varor: list):
        self.order_no = Order.next_order_no
        Order.next_order_no += 1
        self.varor = varor
        self.tot_pris = sum(vara.pris for vara in varor)

    def __str__(self):
        order_info = f"Order {self.order_no}\n"
        order_info += "Varor:\n"
        for vara in self.varor:
            order_info += str(vara) + "\n"
        order_info += f"Pris: {self.tot_pris}"
        return order_info

# Exempel på användning av klasserna:


# vara1 = vara("Produkt 1", "P001", 100)
# vara2 = vara("Produkt 2", "P002", 150)
# vara3 = vara("Produkt 3", "P003", 75)

# varor_i_ordern = [vara1, vara2, vara3]

# order = Order(varor_i_ordern)
# print(order)
