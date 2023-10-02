from utils import *
import os

lst_varor = []
lst_orders = []
lst_varor = Vara.load_varor(lst_varor, "picklesave.txt")
lst_orders = Order.load_orders(lst_orders, "ordersave.txt")

bredd = 99

while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print(f"| {'Café Python'} |".center(bredd))
    print("*" * bredd)
    toprint = ""
    for x in range(1, len(lst_varor) + 1):
        if x % 3 != 0:
            toprint += f"│{lst_varor[x - 1]}".ljust(int(bredd / 3) - 1) + "│"
        else:
            toprint += f"│{lst_varor[x - 1]}".ljust(int(bredd / 3) - 1) + "│\n"
    print(toprint)
    print("*" * bredd)
    print("-" * bredd)
    print("1 | Ny order")
    print("2 | Lägg till vara")
    print("3 | Ta bort vara")
    print("4 | Sök order")
    print("5 | Avsluta program")
    print("-" * bredd)
    val = input("> ")
    if val == "1":
        Order.register_items(lst_varor, lst_orders)
    elif val == "2":
        Vara.ny_vara(lst_varor)
    elif val == "3":
        Vara.delete_vara(lst_varor)
    elif val == "4":
        Order.search_order(lst_orders)
    elif val == "5":
        print("Avslutar program...")
        break
    else:
        input("Fel inmatning, tryck retur för att försöka igen!")

Vara.save_varor(lst_varor, "picklesave.txt")
Order.save_orders(lst_orders, "ordersave.txt")