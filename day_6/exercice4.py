"""Afficher la table de multiplication d'un nombre
Dans cet exercice, vous devez afficher la table de multiplication d'un nombre.

Dans ce cas-ci, votre script doit afficher la table de multiplication du nombre 7 :

0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
4 x 7 = 28
5 x 7 = 35
6 x 7 = 42
7 x 7 = 49
8 x 7 = 56
9 x 7 = 63
10 x 7 = 70"""

nombre = 7

for i in range(11):
    print(f"{i} x {nombre} = {i * 7}")