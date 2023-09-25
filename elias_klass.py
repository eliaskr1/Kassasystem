class vara:
    # Specifierade 'float' för pris så att man inte försökte räkna ut med
    # sträng eller dylikt
    def __init__(self, namn, varukod, pris: float):
        self.namn = namn
        self.varukod = varukod
        self.pris = pris

    def __str__(self):
        # Ändrade utskriften för att snygga till utskriften av ordern
        return f" ({self.varukod}) {self.namn}: {self.pris} kr"


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
