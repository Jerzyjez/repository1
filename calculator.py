liczba=int(input("Podaj liczbę 1- dodawanie 2- odejmowanie 3- mnozenie 4- dzielenie 5- dzielenie modulo 5 potegowanie"))
liczba1=float(input("podaj pierwszą liczbę"))
liczba2=float(input("podaj druga liczba"))
def dodawanie(skladnik1, skladnik2):
    return skladnik1+skladnik2
def odejmowanie (skladnik3, skladnik4):
    return skladnik3-skladnik4
def mnozenie (skladnik5, skladnik6):
    return skladnik5*skladnik6
def dzielenie (skladnik7, skladnik8):
    if skladnik8==0:
        return print("Nie mozna dzielić przez 0. Podaj inną liczbę")
    else:
        return skladnik7+skladnik8
def dzieleniemodulo(dzielnik2, dzielna3):
    if dzielna3==0:
        return print("Nie mozna dzielić przez 0. Podaj inną liczbę")
    else:
        return 
def potegowanie(potegowana,potega):
    if potegowana==0 and potega==0:
        return print("Nie ma określonej wartości liczbowej")
    elif potega==0:
        return 1
    else:
        return potegowana**potega
if liczba==1:
    print(dodawanie(liczba1,liczba2))
elif liczba==2:
    print(odejmowanie(liczba1,liczba2))
elif liczba==3:
    print(mnozenie(liczba1,liczba2))
elif liczba==4:
    print(dzielenie(liczba1,liczba2))
elif liczba==5:
    print(dzieleniemodulo(liczba1,liczba2))
elif liczba==6:
    print(potegowanie(liczba1,liczba2))
else:
    print("Zla liczba")
