"""
Règles du jeu
Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.

Le jeu comporte deux joueurs : vous et un ennemi.

Vous commencez tous les deux avec 50 points de vie.

Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.

L'ennemi ne dispose d'aucune potion.

Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.

Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.

L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.

Lorsque vous utilisez une potion, vous passez le prochain tour.

Déroulé de la partie
Lorsque vous lancez le script, vous devez demander à l'utilisateur
s'il souhaite attaquer ou utiliser une potion :

"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "

Cette phrase sera demandée à l'utilisateur au début de chaque tour.

?  Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi.

Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme.

?  Si l'utilisateur choisi la deuxième option (2), vous prenez une potion.

Les points de vie que la potion vous donne doivent être compris 
entre 15 et 50 et générés aléatoirement par le programme Python.

Vous devez vérifier que l'utilisateur dispose de suffisamment de potion 
et décrémenter le nombre de potions qu'il a dans son inventaire lorsqu'il en boit une. 
Si l'utilisateur n'a plus de potions, vous devez lui indiquer 
et lui proposer de nouveau de faire un choix (attaquer ou prendre une potion).

Quand le joueur prend une potion, il passe le prochain tour.

Une fois l'action du joueur exécutée, et si l'ennemi est encore vivant, 
il vous attaque. Si l'ennemi est mort, vous pouvez terminer 
le jeu et indiqué à l'utilisateur qu'il a gagné ?

L'attaque de l'ennemi inflige des dégâts au joueur compris 
entre 5 et 15, là encore déterminés aléatoirement par le script.

Si vous n'avez plus de points de vie, le jeu se termine et vous avez perdu la partie.

À la fin du tour, vous devez afficher le nombre de 
points de vie restants du joueur et de l'ennemi.

Toutes ces opérations se répètent tant que le joueur et l'ennemi sont en vie.

À chaque tour, vous attaquez en premier. Il ne peut donc pas y 
avoir de match nul. Si lorsque vous attaquez, votre attaque fait 
descendre les points de vie de l'ennemi en dessous (ou égal à) 0, 
vous gagnez la partie sans que l'ennemi n'ait le temps de vous attaquer en retour.

    

"""
import random


user_lives = computer_live = 50
user_potion = 3
SKIP_TURN = False

get_live = 0
user_choice = ""

while user_lives > 0 and computer_live > 0:
    computer_attack = random.randint(5, 15)
    user_attack = random.randint(5, 10)
    get_live = random.randint(15, 50)
    
    
                
    if SKIP_TURN:
        print(f"Vous avez passé votre tour")
        SKIP_TURN = False

    else:
        user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if not (user_choice == "1" or user_choice == "2"):
            print("Mauvaise entrer, veuillez saisir soit 1 ou 2")
            continue
        
        if user_choice == "1":
            computer_live -= user_attack
            print(f"Vous avez infligé {user_attack} point{'s' if user_lives > 1 else ''} de dégats à l'énémi")
        elif user_choice == "2":
            if user_potion:
                user_lives += get_live
                user_potion -= 1
                SKIP_TURN = True

                print(f"Vous avez recuperé {get_live} point{'s' if user_lives > 1 else ''} de vie (il vous reste {user_potion})")
            
            else:
                print("Vous n'avez plus de potion.")
                print("_" * 50)
        
        

    user_lives -= computer_attack
    print(f"L'énémi vous à infligé {computer_attack} point de dégats")
    print(f"il vous reste {user_lives} point{'s' if user_lives > 1 else ''}. de vie")
    print(f"il  reste {computer_live} point{'s' if computer_live > 1 else ''}. de vie à l'énémi")
   
    print("_" * 50)

if user_lives > 0 and user_lives > computer_live:
    print("Vous avez gagner!")

else:
    print("Vous avez perdu!")