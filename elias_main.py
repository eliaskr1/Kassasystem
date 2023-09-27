import pickle
from elias_klass import *

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

for i in lst_varor:
    print(i)

vara.modify_vara(lst_varor)