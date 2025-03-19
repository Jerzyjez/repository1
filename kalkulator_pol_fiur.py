import math

a=int(input("Podaj liczbę: 1-trójkąt, 2-prostokąt/kwadrat, 3-trapez, 4-koło, 5-romb"))
def trojkat(bok, wysokość):
    if bok>0 and wysokość>0:
        return bok*wysokość/2
    else:
        return "zła liczba"
    
def prostokat(bok1, bok2):
    if bok1>0 and bok2>0:
        return bok1*bok2
    else:
        return "Zła liczba"
def trapez (podstawa1,podstawa2 ,wysokość):
    if podstawa1>0 and podstawa2 and wysokość>0:
        return (podstawa1+podstawa2)*wysokość/2
    else:
        return "Zła liczba"
def kolo(promień):
    if promień>0:
        return promień*math.pi
    else:
        return "Zła liczba"
def romb(podstawa,wysokość):
    if podstawa>0 and wysokość>0:
        return podstawa*wysokość
    else:
        return "Zła liczba"
if a==1:
    b=float(input("Podaj długość boku:"))
    c=float(input("Podaj dłudość Wysokości"))
    print(trojkat(b,c))
elif a==2:
    b=float(input("Podaj długość pierwszego boku:"))
    c=float(input("Podaj długość drugiego:"))
    print(prostokat(b,c))
elif a==3:
    a=float(input("Podaj długość pierwszej podstawy"))
    b=float(input("Podaj długość drugiej podstawy"))
    d=float(input("Podaj długość wysokości trapezu"))
    print(trapez(a,b,d))
elif a==4:
    b=float(input("Podaj długość promienia koła"))
    print(kolo(b))
elif a==5:
    b=float(input("Podaj długość boku:"))
    c=float(input("Podaj długość wysokośc iopadającej na ten bok: "))
    print(romb(b,c))
else:
    print("Zła liczba")
    
