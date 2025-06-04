import sys

a = input("Podaj pierwszą liczbę całkowitą większą od zera: ")
b = input("Podaj drugą liczbę całkowitą większą od zera: ")

if not a.isdigit() or not b.isdigit():
    print("Jedna z wartości nie jest liczbą. Program zakończony.")
    sys.exit()

a = int(a)
b = int(b)

if a <= 0 or b <= 0:
    if a <= 0 and b <= 0:
        print("Obie liczby nie są większe od zera.")
    elif a <= 0:
        print("Pierwsza liczba nie jest większa od zera.")
    else:
        print("Druga liczba nie jest większa od zera.")
    sys.exit()


c = a
d = b


while a != b:
    if a > b:
        a -= b
    else:
        b -= a

nww = (c * d) // a  
print(f"Najmniejsza wspólna wielokrotność (NWW) liczb {c} i {d} to: {nww}")
