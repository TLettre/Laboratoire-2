while True:
    x = int(input())
    y = int(input())
    z = input("+ ou / : ")
    if z == "+":
        answer = x + y
        print(answer)
        choix = input("voulez-vous continuer (y) or (n): ")
        if choix == "y":
            continue
        if choix == "n":
            break
    
    if z == "/":
        answer = x / y
        print(answer)
        choix = input("voulez-vous continuer (y) or (n): ")
        if choix == "y":
            continue
        if choix == "n":
            break
    
    