import sys

a = input("Podaj pierwszą liczbę całkowitą większą od zera: ")
b = input("Podaj drugą liczbę całkowitą większą od zera: ")

if not a.isdigit() or not b.isdigit():
    print("Podano niepoprawne dane. Program zakończony.")
    sys.exit()

a = int(a)
b = int(b)

if a <= 0 and b <= 0:
    print("Obie liczby muszą być większe od zera.")
    sys.exit()
elif a <= 0:
    print("Pierwsza liczba musi być większa od zera.")
    sys.exit()
elif b <= 0:
    print("Druga liczba musi być większa od zera.")
    sys.exit()

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(f"Największy wspólny dzielnik (NWD) to: {a}")
    