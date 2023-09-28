import pickle
class Vara:
    def __init__(self, namn, varukod, pris: int):
        self.namn = namn
        self.varukod = varukod
        self.pris = pris

    def getvarukod(self):
        return self.varukod

    def __str__(self):
        return f" ({self.varukod}) {self.namn}: {self.pris} kr"
    
    def ny_vara(lst_varor):
        '''Skapar nytt objekt av typen Vara och
        lägger till i angiven lista.
        args: lista'''
        namn = input("Ange namn på varan: ")
        varukod = input("Ange varukod på varan: ").upper()
        while True:
            try:
                pris = int(input("Ange pris på varan: "))
                break
            except ValueError:
                print(pris, "är inte ett giltigt pris. Försök igen.")
        ny_vara = Vara(namn, varukod, pris)
        lst_varor.append(ny_vara)
        print(ny_vara.namn, "tillagd.")

    def modify_vara(lst_varor):
        '''Ändrar namn och pris på "Vara" objekt i angiven lista med varor
        args: lista med objekt av typen Vara
        '''
        found = False # För att felhantera felaktig varukod
        sku = input("Ange varukod på Vara du vill ändra > ").upper()
        for i in lst_varor:
            if sku == i.getvarukod():
                found = True
                nytt_namn = input("Ange nytt namn till varan > ")
                i.namn = nytt_namn
                while True: # För att felhantera omvandling av pris till int
                    try:
                        nytt_pris_str = input("Ange nytt pris till Vara > ")
                        nytt_pris = int(nytt_pris_str)
                        i.pris = nytt_pris
                        break  # Bryt loopen om omvandlingen till int lyckades
                    except ValueError:
                        print(nytt_pris_str, "är inte ett giltigt pris. Försök igen.")
        if found == True:
            print(sku, "har ändrats.")
        else:
            print(sku, "är inte en giltig varukod.")
        
    def delete_vara(lst_varor):
        x = -1
        found = False # För att felhantera felaktig varukod
        sku = input("Ange varukod på Vara du vill ta bort > ").upper()
        for i in lst_varor:
            x += 1
            if sku == i.getvarukod():
                found = True
                del lst_varor[x]
        if found == True:
            print(sku, "har tagits bort.")
        else:
            print(sku, "är inte en giltig varukod")
            
    def load_varor(lst_varor, pkl_file):
        '''Laddar lista med objekt av typen Vara till
        angiven lista från angiven pickle fil
        args: lista, pickle fil'''
        try:
            with open(pkl_file, "rb") as f:
                lst_varor = pickle.load(f)
        except EOFError:
            lst_varor = []
        except FileNotFoundError:
            lst_varor = []
        
    def save_varor(lst_varor, pkl_file):
        '''Sparar lista med objekt av typen Vara
        till angiven pickle fil.
        args: lista med varor, pickle fil'''
        with open(pkl_file, "wb") as f:
            pickle.dump(lst_varor, f)
        
            

class Order(list):
    '''
    Genererar ett ordernummer och ett totalpris
    för en lista med objekt av typen Vara.
    args: lista med varor, lista som ordern sparas i.
    '''


    def __init__(self, varor: list, lst_orders):
        self.order_no = len(lst_orders)
        self.varor = varor
        self.tot_pris = sum(Vara.pris for Vara in varor)

    def __str__(self):
        order_info = f"Order {self.order_no}\n"
        order_info += "Varor:\n"
        for Vara in self.varor:
            order_info += str(Vara) + "\n"
        order_info += f"Pris: {self.tot_pris} kr"
        return order_info

    def register_items(lst_varor, lst_order):
        reg_items = []  # tom lista för att spara aktuellt köp
        # evighetsloop tar en inmatning i taget istället för en hel order på samma gång.
        while True:
            item = input("Registrera varukod / Q för huvudmenyn: ").upper()
            if item != "Q":
                for vara in lst_varor:
                    if vara.varukod == item:
                        # utskrift av varan så att det är rätt
                        print(vara)
                        # spara till lista
                        reg_items.append(vara)

            else:
                if len(reg_items) != 0:  # förhindrar att tom order skapas
                    order = Order(reg_items)
                    lst_order.append(order)
                    print(order)

    def load_orders(lst_orders, pkl_file):
        '''Laddar ner sparade ordrar från angiven
        pickle fil till angiven lista.
        args: lista med varor, pickle fil'''
        try:
            with open(pkl_file, "rb") as g:
                lst_orders = pickle.load(g)
        except EOFError:
            lst_orders = []
        except FileNotFoundError:
            lst_orders = []
    
    def save_orders(lst_orders, pkl_file):
        '''Sparar ner angiven lista med ordrar till
        angiven pickle fil.
        args: lista med objekt Vara, pickle fil'''
        with open(pkl_file, "wb") as g:
            pickle.dump(lst_orders, g)
            
    def search_order(lst_orders):
        '''Söker igenom angiven lista efter order
        med angivet ordernummer
        args: lista med objekt av typen Order'''
        i = int(input("Ordernummer: "))
        print(lst_orders[i - 1])

# Exempel på användning av klasserna:


# vara1 = Vara("Produkt 1", "P001", 100)
# vara2 = Vara("Produkt 2", "P002", 150)
# vara3 = Vara("Produkt 3", "P003", 75)

# varor_i_ordern = [vara1, vara2, vara3]

# order = Order(varor_i_ordern)
# print(order)
