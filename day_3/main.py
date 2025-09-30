"""
Votre objectif aujourd'hui est de construire un "Jeu d'aventure à choix". 
vous allez construire une version très simple de ce type de jeu de texte.

Utilisez le diagramme de flux lié ici pour créer la logique du jeu.

Une fois que vous aurez terminé le projet, vous pourrez toujours étendre le jeu et le rendre plus intéressant!

"""


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choose_the_direction_1 = input("choisi ta direction left pour gauche ou l ou right pour droit ou r: ").lower()


if choose_the_direction_1 == "left" or choose_the_direction_1 == "l":
    choice = input("vous êtes arrivés au lac. il y a une île au milieu du lac"
                   "\nTapez \"wait\" ou \"w\" pour attendre le bateau. Tapez \"swim\" ou \"s\" pour traverser à la nage. ").lower()

    if choice == "wait" or choice == "w":
        choice1 = input("Vous arrivez sur l'île sain et sauf. Il y a une maison avec 3 portes : une rouge ou r," 
              "une jaune ou y et une bleue ou b. Quelle est la couleur que vous choisissez ?"
                        "une 'jaune ou y' et une 'bleue ou b'. Quelle couleur choisirez-vous ? ").lower()
        if choice1 == "blue" or choice1 == "b":
            print("Vous avez gagner")
        else:
            print("Game over")    
    else:
        print("Game over")
else:
    print("Game over")