
continuer = "o"

while continuer == "o":
    print("On continue !")
    choice = input("Voulez-vous continuer ? o/n ").lower()
    if choice == "o":
        continue
    elif choice == "n":
        break
    else:
        print("Mauvaise entrer")