import datetime
bredd = 40

def line(value):
  if value:
    print("*" * bredd)
  else:
    print("-" * bredd)

def header(exempel):
    print("|",exempel.center(36),"|")


def echo(text):
    print(text)

def prompt(val):
    print(f"| Val > {val}")

def meny(kaffe, lunch, dessert):
    print("*"*77)
    print(f"*|*|{kaffe[0].ljust(19)} |*|{lunch[0].ljust(25)} |*|{dessert[0].ljust(20)}*")
    print(f"*|*|{kaffe[1].ljust(19)} |*|{lunch[1].ljust(25)} |*|{dessert[1].ljust(20)}*")
    print(f"*|*|{kaffe[2].ljust(19)} |*|{lunch[2].ljust(25)} |*|{dessert[2].ljust(20)}*")
    print("*" * 77)

kaffe = ["Bryggkaffe 12 kr", "Capuccino 30 kr", "Caffe latte 30 kr"]
lunch = ["Billys pizza 30 kr", "Sallad 80 kr", "Pannkakor 3 st, 50 kr"]
dessert = ["Morotskaka 35 kr", "Chokladboll 25 kr", "Mjukglass 25 kr"]
exempel = "Café Python"
altA = "A | Ny order"
altB = "B | Ta bort vara"
altC = "C | Retur"
tid = datetime.datetime.now()


#Implementering av funktioner
meny(kaffe, lunch, dessert)
header(exempel)
line(True)
print(tid)
line(False)
echo(altA)
echo(altB)
echo(altC)
line(False)
#Input går sist ananrs stoppar det hela körningen och utskrift av funktioner
val = input("| Val > ")
#Utskrift av input via funktionen prompt()
prompt(val)