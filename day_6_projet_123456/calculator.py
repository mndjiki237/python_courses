"""
    
    Déroulé du script
Le script doit demander à l'utilisateur de saisir deux nombres :

>>> Entrez un premier nombre : 5
>>> Entrez un deuxième nombre : 10
Le script doit ensuite afficher la phrase suivante :

"Le résultat de l'addition de 5 avec 10 est égal à 15"

Vous devrez donc utiliser une fonction de Python qui permet de 
récupérer la saisie de l'utilisateur (deux fois), pour ensuite 
additionner ces variables et afficher le résultat.

Vous devez vous assurer que le programme ne retournera pas d'erreur 
si l'utilisateur rentre autre chose que deux nombres.

Il va donc falloir gérer ces cas de figure. Si l'utilisateur rentre 
une lettre, un symbole ou quoi que ce soit d'autre qu'un nombre, 
vous devrez lui demander de nouveau de saisir deux valeurs valides :

>>> Entrez un premier nombre : a
>>> Entrez un deuxième nombre : sgoind
Veuillez entrer deux nombres valides
>>> Entrez un premier nombre
    """




# while True:
#     nombre_1 = input("Entrez un premier nombre : ")
#     nombre_2 = input("Entrez un deuxième nombre : ")
#     if nombre_1.isdigit() and nombre_2.isdigit():
#         nombre_1 = int(nombre_1)
#         nombre_2 = int(nombre_2)
#         print(f"Le résultat de l'addition de {nombre_1} avec {nombre_2} est égal à {nombre_1 + nombre_2}")
#         break
#     else:
#         print("Veuillez entrer deux nombres valides")



# On déclare deux variables
a = b = ""

# Tant que a et b ne sont pas des nombres, on boucle
while not (a.isdigit() and b.isdigit()):
    
    # On demande deux nombres à l'utilisateur
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    # On affiche une phrase si les nombres entrés ne sont pas valides.
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

# On affiche le résultat de l'addition
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
