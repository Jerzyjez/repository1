a=int(input("podaj pierwsza liczbe calkowita wieksza od zera"))
b=int(input("podaj druga liczbe calokowita  wieksza od zera"))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)
    