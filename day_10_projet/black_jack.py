""" 
Distribuez à l'utilisateur et à l'ordinateur une main 
de départ composée de 2 cartes de valeurs aléatoires.

Détecte quand l'ordinateur ou l'utilisateur a 
un blackjack. (As + carte de valeur 10).

Si l'ordinateur obtient un blackjack, l'utilisateur perd 
(même s'il a également un blackjack). S'il obtient un blackjack, 
il gagne (sauf si l'ordinateur a également un blackjack).

Calculez les scores de l'utilisateur et de 
l'ordinateur en fonction des valeurs de leurs cartes.

Si un as est tiré, comptez-le comme 11. 
Mais si le total dépasse 21, comptez l'as comme 1 à la place.

Révéler la première carte de l'ordinateur à l'utilisateur.

Le jeu se termine immédiatement lorsque le score de l'utilisateur 
dépasse 21 ou si l'utilisateur ou l'ordinateur obtient un blackjack.

Demandez à l’utilisateur s’il souhaite obtenir une autre carte.

Une fois que l'utilisateur a terminé et ne souhaite plus piocher 
de cartes, laissez l'ordinateur jouer. Il doit continuer à 
piocher des cartes, sauf si son score dépasse 16.

Comparez les scores des utilisateurs et de l'ordinateur et 
voyez s'il s'agit d'une victoire, d'une défaite ou d'un match nul.

Imprimez la main finale du joueur et de l'ordinateur ainsi 
que leurs scores à la fin de la partie.

Une fois la partie terminée, demandez à l'utilisateur 
s'il souhaite rejouer. Videz la console pour recommencer.


"""

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

user_sum_cards = 0
computer_sum_cards = 0
computer_sum_first_cards = 0
user = False
computer = False


def pick_card(cards):
    return random.choice(cards)




def blackjack_verif(user_cards, computer_cards, user, computer):
    is_user_play = False
    while True:
        if len(user_cards) < 2 and len(computer_cards) < 2:
            user_cards.append(pick_card(cards=cards))
            computer_cards.append(pick_card(cards=cards))
            is_user_play = True
        if is_user_play:
            user_cards.append(pick_card(cards=cards))
            is_user_play = False
        computer_cards.append(pick_card(cards=cards))
        if len(user_cards) == 2 and  sum(user_cards) == 21:
            user_cards[0] = 1
            
        elif len(computer_cards) == 2 and  sum(computer_cards) == 21:
            computer_cards[0] = 1

        elif len(user_cards) == 2 and  sum(user_cards) > 21:
            user = "end"
        elif len(computer_cards) == 2 and  sum(computer_cards) > 21:
            computer = "end"
        elif len(user_cards) == 2 and  sum(user_cards) == 20:
            user = "Blacjack"
        elif len(computer_cards) == 2 and  sum(computer_cards) == 20:
            computer = "blackjack"

        user_choice = input("Voulez vous encore tirer une carte? y/n ")

        if user_choice == "y":
            is_user_play == True

        
        user_sum_cards = sum(user_cards)
        computer_sum_cards = sum(computer_cards)
        print(len(user_cards) == 2 and  sum(user_cards) == 21)
        print(len(computer_cards) == 2 and  sum(computer_cards) == 21)
        print(len(user_cards) == 2 and  sum(user_cards) == 20)
        print(len(computer_cards) == 2 and  sum(computer_cards)== 20)
        print(user_sum_cards)
        print(computer_sum_cards)
        print(user_cards)
        print(computer_cards)
        print(user)
        print(computer)
            
        
    


blackjack_verif(user_cards=user_cards, computer_cards=computer_cards, user=user, computer=computer)