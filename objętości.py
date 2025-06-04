import math
import sys
a = input("Podaj liczbę 1-prostopadłościan, 2-walec, 3-stozek, 4-kula: ")
if not a.isdigit():
    print("To nie jest liczba. Program zakończony.")
    sys.exit()
a = int(a)
def prostopadloscian(bok1,bok2,bok3):
    if bok1 >0 and bok2 >0 and bok3>0:
        return bok1*bok2*bok3
    else:
        return "Zła liczba"
def walec(promień,wysokość):
    if promień>0 and wysokość>0:
        return promień*wysokość*math.pi*promień
    elif promień<=0 and wysokość<=0:
        return "Zła dlugosc promienia i wysokosci"
    elif promień<=0:
        return "zla dlugosc promienia"
    else:
        return "zla dlugosc wysokosci"
def stozek(promień, wysokość):
    if promień>0 and wysokość>0:
        return promień*promień*wysokość/3
    else:
        return "Zła liczba"
def kula (promień):
    if promień>0:
        return promień**3*math.pi*4/3
    else:
        return "Zła liczba"
if a==1:
    b=float(input("Podaj długość pierwszego boku: "))
    c=float(input("Podaj długość drugiego boku:"))
    d=float(input("Podaj długość trzeciego"))
    print(prostopadloscian(b,c,d))
elif a==2:
    b=float(input("podaj długość promienia podstawy:"))
    c=float(input("Podaj Dlugość wysokosci walca:"))
    print(walec(b,c))
elif a==3:
    b=float(input("Podaj dlugosc promienpodstawy:"))
    c=float(input("Podaj dlugosc wysokosci stozka:"))
    print(stozek(b,c))
elif a==4:
    b=float(input("Podaj długość promienia kuli:"))
    print(kula(b))
else:
    print("taka liczba nie odpowiada zadnej liczbie")



     
        