a=int(input("podaj pierwsza liczbe calkowita"))
b=int(input("podaj druga liczbe calokowita"))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)
    