import sys
a = input("Podaj pierwsza liczbe calkowita wieksza od zera:")
b = input("Podaj druga liczbe calokowita  wieksza od zera:")
if not a.isdigit():
    print("To nie jest liczba. Program zakończony.")
    sys.exit()
a = int(a)

if not b.isdigit():
    print("To nie jest liczba. Program zakończony.")
    sys.exit()
b = int(b)
if a>0 and b>0:
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
    print("pierwsza liczba <0 ")
    