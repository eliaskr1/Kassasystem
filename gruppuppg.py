

#måste skapa tom lista först för att kunna lägga till saker med funktionen nyvara
lst_varor = []

# metod för att lägga till en ny vara
def nyvara(namn, varukod, pris):
    nyvara = vara(namn, varukod, pris)
    lst_varor.append(nyvara)
    return lst_varor

#varukod får inte starta på P, ger error
vara1 = nyvara("Bryggkaffe", 100, 12)
vara2 = nyvara("Cappuccino", 101, 30)
vara3 = nyvara("Caffe latte", 102, 30)

vara4 = nyvara("Billys pizza", 200, 30)
vara5 = nyvara("Sallad", 201, 80)
vara6 = nyvara("3 Pannkakor", 202, 50)

vara7 = nyvara("Morotskaka", 300, 35)
#får inte skriva 08, eller 008, får error, python gillar inte det
vara8 = nyvara("Chokladboll", 301, 25)
vara9 = nyvara("Mjukglass", 302, 25)


def meny(bredd):
    print(f"| {'Café Python'} |".center(bredd))
    print("*"*bredd)
    toprint = ""
    for x in range(1, len(lst_varor) + 1):
        if x % 3 != 0:
            toprint += f"│{lst_varor[x - 1]}".ljust(int(bredd/3))
        else:
            toprint += f"│{lst_varor[x - 1]}│\n".rjust(int(bredd/3))
    print(toprint)
    print("*" * bredd)
    print("-" * bredd)
    print("A | Ny order")
    print("B | Ta bort vara")
    print("C | Retur")
    print("-" * bredd)

#Huvudmeny med display och sortiment
def huvudmeny():
    meny(90)
    while True:
        val = input("Ange val (A, B, C): ")
        if val == "A":
            reg_items = register_items(lst_varor)
        elif val == "B":
            print("Gå tillbaka till senaste order?") #Ska detta alt finnas?
        elif val == "C":
            print("Sök i gamla ordrar med hjälp av ordernummer") ########### Alis del ###########
        else:
            print("Fel inmatning")


#denna funktion aktiveras när alt "A" väljs från huvudmenyn
def register_items(lst_varor):
    reg_items = [] #tom lista för att spara aktuellt köp
    #evighetsloop tar en inmatning i taget istället för en hel order på samma gång.
    while True:
        item = input("Registrera varukod / Q för huvudmenyn: ")
        if item != "Q":
            for vara in lst_varor:
                if vara.varukod == int(item):
                    #utskrift av varan så att det är rätt
                    print(vara)
                    #spara till lista
                    reg_items.append(vara)
        else:
            if len(reg_items) != 0: #förhindrar att tom order skapas
                order = Order(reg_items)
                print(order)
                huvudmeny()


huvudmeny()