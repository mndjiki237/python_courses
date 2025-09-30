    
"""
Introduction au projet
Vous voici arrivé au premier projet de cette formation.

Rien de bien incroyable encore, on va se laisser un peu de temps avant de réaliser 
un site web qui analyse les données de la bourse en temps réel 😉

Ce projet de la calculatrice reviendra dans la suite du cours sous 
différentes formes, à chaque fois avec une petite difficulté supplémentaire.

👉 Dans la première version de ce projet, vous allez devoir créer une calculatrice 
en ligne de commande qui demande à l'utilisateur de saisir deux nombres et qui affiche 
ensuite le résultat de l'addition de ces deux nombres.

Rien de bien compliqué si vous avez suivi attentivement toutes les sessions et 
réalisé avec soin les quiz et exercices de code jusqu'ici.

Bonne chance pour ce premier projet !
Thibault.
    
    """
print("Calculer l'addition entre deux nombre")
number_1 = int(input("Entrer un premier nombre: "))
number_2 = int(input("Entrer un deuxieme nombre: "))

resultat = number_1 + number_2

print(f"le resultat de {number_1} + {number_2} = {resultat}")