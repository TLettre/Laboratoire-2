import random
import time

random_number = 69                       ##random.randint(1, 100)
while True:
    choice = int(input("prenez un chiffre entre 1 et 100:"))
    if choice >= 1 and choice <= 100:
        if choice == random_number:
            print("GAME WIN")
            time.sleep(5)
            break
        elif choice > random_number:
            print("Trop haut")
        elif choice < random_number:
            print("Trop bas")
    