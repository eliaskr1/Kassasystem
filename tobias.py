import pickle
import tobiasclass

# Laddar objekt sparade i picklesave.txt
try:
    with open("picklesave.txt", "rb") as f:
        lst_varor = pickle.load(f)
except EOFError:
    lst_varor = []
except FileNotFoundError:
    lst_varor = []


# metod för att lägga till en ny vara
def nyvara(namn, varukod, pris):
    nyvara = tobiasclass.vara(namn, varukod, pris)
    lst_varor.append(nyvara)


# Lite exempelkod för att testa
# for x in lst_varor:
#     print(x)
# nyvara("Mjölk", "115", 20)

# Sparar alla objekt till picklesave.txt
with open("picklesave.txt", "wb") as f:
    pickle.dump(lst_varor, f)
