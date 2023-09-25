import pickle
import elias_klass

# Laddar objekt sparade i picklesave.txt
try:
    with open("picklesave.txt", "rb") as f:
        lst_varor = pickle.load(f)
except EOFError:
    lst_varor = []
except FileNotFoundError:
    lst_varor = []

try:
    with open("ordersave.txt", "rb") as g:
        lst_orders = pickle.load(g)
except EOFError:
    lst_orders = []
except FileNotFoundError:
    lst_orders = []


# metod för att lägga till en ny vara
def nyvara(namn, varukod, pris):
    nyvara = elias_klass.vara(namn, varukod, pris)
    lst_varor.append(nyvara)


# ny_vara1 = elias_klass.vara("vara1choklad", "P001", 100)
# ny_vara2 = elias_klass.vara("vara2", "P002", 250)
# ny_vara3 = elias_klass.vara("vara3banan", "P003", 50)
# ny_vara4 = elias_klass.vara("vara4", "P004", 50)
# ny_vara5 = elias_klass.vara("vara5blabla", "P005", 50)

# lst_varor = [ny_vara1, ny_vara2, ny_vara3, ny_vara4, ny_vara5]
def sell():
    new_order = elias_klass.Order(lst_varor, len(lst_orders))
    lst_orders.append(new_order)


def meny(bredd):
    print(f"| {'Café Python'} |".center(bredd))
    print("*"*bredd)
    toprint = ""
    for x in range(1, len(lst_varor) + 1):
        if x % 3 != 0:
            toprint += f"│{lst_varor[x - 1]}".ljust(int(bredd/3))
        else:
            toprint += f"│{lst_varor[x - 1]}│\n".rjust(int(bredd/3))
    print(toprint + "\n")
    print("*" * bredd)
    print("-" * bredd)
    print("A | Ny order")
    print("B | Ta bort vara")
    print("C | Retur")
    print("-" * bredd)


meny(90)
i = int(input("Search for ordernumber: "))
print(lst_orders[i])


# Lite exempelkod för att testa
# for x in lst_varor:
#     print(x)
# nyvara("Mjölk", "115", 20)

# Sparar alla objekt till picklesave.txt
with open("picklesave.txt", "wb") as f:
    pickle.dump(lst_varor, f)

with open("ordersave.txt", "wb") as g:
    pickle.dump(lst_orders, g)
