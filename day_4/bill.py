import random

"""
developer le jeu d'avanture avec le module random

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
direction = ["left", "rigth"]
direction_2 = ["l", "r"]

color = ["blue", "rouge", "jaune"]
color_2 = ["b", "r", "j"]
a = random.randint(0,1)
b = random.randint(0,2)
computer_choice = direction[a]
computer_choice_2 = direction_2[a]

color_choice = color[b]
color_choice_2 = color_2[b]



if choose_the_direction_1 == computer_choice or choose_the_direction_1 == computer_choice_2:
    choice = input("vous êtes arrivés au lac. il y a une île au milieu du lac"
                   "\nTapez \"wait\" ou \"w\" pour attendre le bateau. Tapez \"swim\" ou \"s\" pour traverser à la nage. ").lower()

    if choice == "wait" or choice == "w":
        choice1 = input("Vous arrivez sur l'île sain et sauf. Il y a une maison avec 3 portes : une rouge ou r," 
              "une jaune ou y et une bleue ou b. Quelle est la couleur que vous choisissez ?"
                        "une 'jaune ou y' et une 'bleue ou b'. Quelle couleur choisirez-vous ? ").lower()
        if choice1 == color_choice or choice1 == color_choice_2:
            print("Vous avez gagner")
        else:
            print("Game over")    
    else:
        print("Game over")
else:
    print("Game over")