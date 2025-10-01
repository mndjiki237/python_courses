# pierre papier ciseau

"""
etape:

    importer le module random
    creer une liste contenant les mots pierre papier ciseau
    joueur 1 l'ia doit choisir au hasard son jeu
    joueur 2 qui est l'utilisateur doit choisir son jeu
    verification du vainqueur


"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choice = ["rock", "paper", "scissors"]
choice = ["0", "1", "2"]
game = [rock, paper, scissors]

print("Welcome to the rock paper scissors")
computer = random.randint(0,2)


user = input("Veuiller entrer un nombre entier entre 0 et 2, " \
                        "0 pour rock, 1 pour paper, 2 pour scissors: ")
if user in choice:
    user_int = int(user)
    if user_int == computer:
        print("draw")
    elif user_int == 2 and computer == 0:
        print("you lose")
    elif user_int == 0 and computer == 2:
        print("you win")
    elif user_int > computer:
        print("you win")
    elif computer > user_int:
        print("You lose")
    print(f"you: {game[user_int]}")
    print(f"computer: {game[computer]}")

else:
    print("Mauvaise entrer")
    print(user)