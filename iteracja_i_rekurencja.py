def silnia_iter(liczba):
    if liczba<2:
        return 1
    else:
        for i in range(2, liczba):
            liczba*=i
        return liczba
print(silnia_iter(5))

def silnia_rek(liczba):
    if liczba<2:
        return 1
    else:
        return liczba*silnia_rek(liczba-1)
