import math

a=int(input("Podaj liczbę: 1-trójkąt, 2-prostokąt/kwadrat, 3-trapez, 4-koło, 5-romb 6- rownoleglobok,7-deltoid"))
def trojkat(bok, wysokość):
    if bok>0 and wysokość>0:
        return bok*wysokość/2
    elif bok<=0 and wysokość<=0:
        return "Zła długość boku i wysokości"
    elif bok<=0:
        return "zla dlugosc"
    else:
        return "zla wysokosc"
def prostokat(bok1, bok2):
    if bok1>0 and bok2>0:
        return bok1*bok2
    elif bok1<=0 and bok2<=0:
        return "zla dlugosc onu bokow"
    elif bok1<=0:
        return "zla dlugosc pierwszego boku"
    else:
        return "Niepoprawna dlugosc drugiego bku"
def trapez (podstawa1,podstawa2 ,wysokość):
    if podstawa1>0 and podstawa2 and wysokość>0:
        return (podstawa1+podstawa2)*wysokość/2
    elif podstawa1<=0 and podstawa2<=0 and wysokość<=0:
        return "Zła dlugosc obu bokow i wysokosci"
    elif podstawa1<=0 and podstawa2<=0:
        return "zla dlugosc obu podstaw"
    elif podstawa1<=0 and wysokość<=0:
        return "zla dlugosc pierwszej podstawy i wyskokosci"
    elif podstawa2<=0 and wysokość<=0:
        return "niepoprawna dlugosc drugiej podstawy i wysokosci"
    elif podstawa1<=0: 
        return "zla dlugosc podstawy 1"
    elif podstawa2<=0:
        return "zla dlugosc podstawy2"
    else:
        return "zla dlugosc wysokosci"

def kolo(promień):
    if promień>0:
        return promień*math.pi
    else:
        return "Zła dlugos  promienia kola"
def rownoleglobok(podstawa,wysokość):
    if podstawa>0 and wysokość>0:
        return podstawa*wysokość
    else:
        return "Zła liczba"
def romb(przekatna1,przekatna2):
    if przekatna1>0 and przekatna2>0:
        return 1/2*przekatna1*przekatna2
    else:
        return "zła liczba"
def deltoid(przekatna1,przekatna2):
    if przekatna1>0 and przekatna2>0:
        return 1/2*przekatna1*przekatna2
    else:
        return "zła liczba"
def szesciokat(bok):
    if bok>0:
        return bok*bok*1.5*3**0.5
    else:
        return "zla dlugosc boku" 
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
    liczba=int(input("Podaj sposób w jaki sposób chcesz obliczyć pole rombu: 1-0,5*przękątna1*przekątna2  2-podstawa*wysokość: "))
    if liczba==2:
        b=float(input("Podaj długość boku: "))
        c=float(input("Podaj długość wysokości opadającej na ten bok: "))
        print(rownoleglobok(b,c))
    else:
        b=float(input("Podaj długość pierwszej przekątnej: "))
        c=float(input("Podaj długość drugiej przekątnej: "))
        print(romb(b,c))
elif a==6:
        b=float(input("Podaj długość boku: "))
        c=float(input("Podaj długość wysokośc iopadającej na ten bok: "))
        print(rownoleglobok(b,c))
else:
    print("Takiej figury nie obsługujemy")
if liczba==7:
        b=float(input("Podaj pierwszej przekątnej: "))
        c=float(input("Podaj długość drugiej przekątnej:: "))
        print(deltoid(b,c))
if liczba==8:
        b=float(input("Podaj dlugosc boku: "))
        print(szesciokat(b))