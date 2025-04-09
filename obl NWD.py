a=int(input("Podaj pierwsza liczbe calkowita wieksza od zera:"))
b=int(input("Podaj druga liczbe calokowita  wieksza od zera:"))
if a and b>0:
        while a!=b:
            if a>b:
                a-=b
            else:
                b-=a
        print(a)
elif a<=0 and b<=0:
    print("obie liczby nie sa >0")
elif b<=0:
    print("druga liczba <0")
else:
    print("druga liczba <0 ")
    