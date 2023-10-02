import pickle


class Vara:
    def __init__(self, namn, varukod, pris: int):
        if pris < 0 or pris > 9999:
            raise ValueError
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
        exit_check = True
        lst_varukoder = []
        for x in lst_varor:
            lst_varukoder.append(x.varukod)
        while exit_check:
            namn = input("Ange namn på varan (0 för att återgå till menyn) > ")
            if len(namn) > 23:
                print("Namn får inte vara längre än 23 tecken. Försök igen")
            elif namn == "":
                print("Ogiltigt namn. Försök igen.")
            elif namn == "0":
                exit_check = False
            else:
                break
        while exit_check:
            varukod = input("Ange varukod på varan (0 för att återgå till menyn) > ").upper()
            if len(varukod) > 3:
                print("Varukod får inte vara längre än 3 tecken. Försök igen.")
                continue
            elif varukod in lst_varukoder:
                print(f"Varukod {varukod} används redan för en annan vara. Försök igen.")
                continue
            elif varukod == "":
                print("Ogiltig varukod. Försök igen.")
            elif varukod == "0":
                exit_check = False
            else:
                break
        while exit_check:
            try:
                pris = int(input("Ange pris på varan (0 för att återgå till menyn) > "))
                if pris == 0:
                    exit_check = False
                else:
                    ny_vara = Vara(namn, varukod, pris)
                    break
            except ValueError:
                print("Ange ett giltigt pris. Försök igen.")
        if exit_check == True:
            ny_vara = Vara(namn, varukod, pris)
            lst_varor.append(ny_vara)
            print(ny_vara.namn, "tillagd.")
            input("Tryck på retur för att fortsätta...")

    def delete_vara(lst_varor):
        found = False  # För att felhantera felaktig varukod
        while not found:
            print("Ange varukod på vara du vill ta bort (0 för att återgå till menyn) > ")
            sku = input("> ").upper()
            if sku == "0":
                break  # Avsluta och återgå till menyn om användaren anger 0
            for i in lst_varor:
                if sku == i.getvarukod():
                    found = True
                    lst_varor.remove(i)
                    print(sku, "har tagits bort.")
                    input("Tryck på retur för att fortsätta...")
                    break
            if not found:
                print(sku, "är inte en giltig varukod. Försök igen.")
                input("Tryck på retur för att fortsätta...")

    def load_varor(lst_varor, pkl_file):
        '''Laddar lista med objekt av typen Vara till
        angiven lista från angiven pickle fil
        args: lista, pickle fil
        returns: lista med tillgängliga varor'''
        try:
            with open(pkl_file, "rb") as f:
                lst_varor = pickle.load(f)
        except EOFError:
            lst_varor = []
        except FileNotFoundError:
            lst_varor = []
        return lst_varor

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
        self.order_no = len(lst_orders) + 1
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
        '''Registrerar varor från angiven lista
        med objekt av typen Vara till en
        lista som skrivs till angiven lista
        med objekt av typen Order
        args: lista med varor, lista med ordrar'''
        reg_items = []  # tom lista för att spara aktuellt köp
        # evighetsloop tar en inmatning i taget istället för en hel order på samma gång.
        print("Registrera varukod / Q för att ta betalt / 0 för att avbryta köp")
        while True:
            # Undantagsfall ifall cafémenyn skulle vara helt tom, fastnar i en loop annars
            if len(lst_varor) == 0:
                input("Det finns inga varor att lägga till")
                break

            item = input("> ").upper()
            if item == "0":
                break
            elif item != "Q":
                found = False
                for vara in lst_varor:
                    if vara.varukod == item:
                        found = True
                        # utskrift av varan så att det är rätt
                        print(vara)
                        # spara till lista
                        reg_items.append(vara)
                if found == False:
                    print("Varukod hittas ej.")
                print("Total:", sum(vara.pris for vara in reg_items), "kr")
            else:
                if len(reg_items) != 0:  # förhindrar att tom order skapas
                    order = Order(reg_items, lst_order)
                    lst_order.append(order)
                    print(order)
                    input("")  # Pausar för utskrift av kvitto.
                    break
                else:
                    break  # Förhindrar evighetsloop om man inte har några varor att sälja

    def load_orders(lst_orders, pkl_file):
        '''Laddar ner sparade ordrar från angiven
        pickle fil till angiven lista.
        args: lista med varor, pickle fil
        returns: lista med tillgängliga ordrar'''
        try:
            with open(pkl_file, "rb") as g:
                lst_orders = pickle.load(g)
        except EOFError:
            lst_orders = []
        except FileNotFoundError:
            lst_orders = []
        return lst_orders

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
        while True:
            try:
                i = int(input("Ordernummer / 0 för att återgå till menyn): "))
                if i == 0:
                    break  # Avsluta loopen och gå tillbaka till menyn
                elif i < 1 or i > len(lst_orders):
                    print("Ogiltigt ordernummer! Försök igen.")
                else:
                    # Ändrade så att den visar ordernumret man sökte på
                    for order in lst_orders:
                        if order.order_no == i:
                            print(order)
            except ValueError:  # Lösning för except error om man anger felaktig order nummer.
                print("Ogiltig inmatning! Försök igen.")