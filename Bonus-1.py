import math

CAD = 1.50
USD = 1.04
BHD = 0.39
montant = 0

while True:
    Eur = int(input("combien voulez-vous convertir: "))
    Demande = input("(CAD = C, USD = U, BHD = B): ")
    if Demande == "C":
        montant = Eur * CAD
        print(math.floor((montant*100))/100)

    if Demande == "U":
        montant = Eur * USD
        print(math.floor((montant*100))/100)
    
    if Demande == "B":
        montant = Eur * BHD
        print(math.floor((montant*100))/100)