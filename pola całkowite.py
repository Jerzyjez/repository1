import math
a=int(input("Podaj liczbę 1-prostopadloscian, 2-walec, 3-stozek, 4-kula: "))
def prostopadloscian(bok1,bok2,bok3):
    if bok1>0 and bok2>0 and bok3>0:
        return 2*(bok1*bok2+bok2*bok3+bok1*bok3)
    elif bok1<=0 and bok2<=0 and bok3<=0:
        return "Niepoprawna długosc wszystkich trzech bokow"
    elif bok1<=0 and bok2<=0:
        return "Niepoprawna dlugość pierwszego i drugiego boku"
    elif bok1<=0 and bok3<=0:
        return "Niepoprawna dlugość pierwszego i trzeciego boku"
    elif bok2<=0 and bok3<=0:
        return "Niepoprawna dlugość drugiego i trzeciego boku"
    elif bok1<=0:
        return "Niepoprawna dlugośc pierwszego boku"
    elif bok2<=0:
        return "Niepoprawna dlugość drugiego boku"
    else:
        return "Niepoprawna dlugość trzeciego boku"
def walec(promien,wysokosc):
    if promien>0 and wysokosc>0:
        return 2*math.pi*promien(promien+wysokosc)
    if promien>0 and wysokosc>0:
        return promien*wysokosc
    elif promien<=0 and wysokosc<=0:
        return "Niepoprawna długość promienia i wysokości"
    elif promien<=0:
        return "Niepoprawna długość promienia"
    else:
        return "Niepoprawna długość wysokości"
def stozek(promien,tworzaca):
    if promien>0 and tworzaca>0:
        return 2*math.pi*promien(promien+tworzaca)
    if promien>0 and tworzaca>0:
        return promien*tworzaca
    elif promien<=0 and tworzaca<=0:
        return "Niepoprawna długość promienia i tworzacej"
    elif promien<=0:
        return "Niepoprawna długość promienia"
    else:
        return "Niepoprawna długość tworzacej"
def kula(promien):
    if promien>0:
        return 4*math.pi*promien*promien
    else:
        return "Niepoprawna dlugosc promienia"
if a==1:
    b=float(input("Podaj długosc:" ))
    c=float(input("Podaj szerokosc:" ))
    d=float(input("Podaj grubosc:" ))
    print(prostopadloscian(b,c,d))
elif a==2:
    b=float(input("podaj dlugosc promienia podstawy"))
    c=float(input("Podaj dlugosz wysokosci" ))
    print(walec(b,c))
elif a==3:
     b=float(input("Podaj dlugosz promienia podstawy" ))
     c=float(input("Podaj dlugosz tworzącej" ))
     print(stozek(b,c))
elif a==4:
    b=float(input("Podaj długosc promienia kuli: "))
    print(kula(b))
else:
    print("Taka cyfra nie odpowiada zadnej bryle. Wprowadź cyfrę jeszcze raz.")
    