import random 

opcje=("kamien"," papier"," nozyce")
a=random.choice(opcje)
b=input("podaj swoja opcje;")
if a==b:
    print("remis")
elif a=="kamien" and b=="papier":
    print("Wygrales")
elif a=="nozyce" and b=="papier":
    print("przegrales")
elif a=="kamien" and b=="nozyce":
    print("przegrales")