"""Le but de cet exercice est de modifier le script afin 
d'afficher l'index de chaque lettre du mot 'Python'.

Pour l'instant le script retourne une erreur. À vous de la corriger.

Votre script doit donc afficher :

0
1
2
3
4
5
Petite astuce : vous allez devoir utiliser une fonction qui 
permet de récupérer la longueur d'un élément..."""

language = "Python"

# for i in range(len(language)):
#     print(i)

for i in range(len(language)):
    print(language.index(language[i]))
