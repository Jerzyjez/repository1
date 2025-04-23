a=int(input("podaj pierwsza liczbe calkowita wieksza od zera"))
b=int(input("podaj druga liczbe calokowita  wieksza od zera"))
c=a
d=b
if a>0 and b>0:
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    e=c*d/a
    print(e)
elif a<=0 and b<=0:
    print("obie liczby nie sa >0")
elif b<=0:
    print("druga liczba <0")
else:
    print("pierwsza liczba <0 ")