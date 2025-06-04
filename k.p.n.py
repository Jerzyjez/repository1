import random 

opcje=("kamien","papier","nozyce")
a=random.choice(opcje)
b=input("podaj swoja opcje(bez polskich znakow i z malej litery);")
print("komputer wybral ", a)
if b not in opcje:
    print ("Niepoprawna opcja wpisana")
elif a == b:
    print("remis")
elif a=="kamien" and b=="papier":
    print("Wygrales")
elif a=="nozyce" and b=="papier":
    print("przegrales")
elif a=="nozyce" and b=="kamien":
    print("przegrales")
elif a=="kamien" and b=="nozyce":
    print("przegrales")
elif a=="papier" and b=="nozyce":
    print("wygrales")
elif a=="nozyce" and b=="nozyce":
    print("wygrales")
elif a=="papier" and b=="kamien":
    print("przegrales")



