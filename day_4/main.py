import random

"""
Exercice module random
Dans cet exercice, vous devez générer deux nombres aléatoires et 
indiquer à l'utilisateur lequel des deux nombres est le plus grand.

Par exemple :

Un nombre a est généré aléatoirement et prend la valeur de 15.

Un nombre b est généré aléatoirement et prend la valeur de 26.

Votre script doit afficher la phrase suivante :

"Le nombre b est plus grand que le nombre a."

Dans le cas contraire, le script devra afficher :

"Le nombre a est plus grand que le nombre b."

Si les nombres sont égaux, le script devra afficher :

"Le nombre a et le nombre b sont égaux."



"""
a = random.randint(0, 100)
b = random.randint(0, 100)

choice = input("Entrer 'a' ou 'b' et pour designer le nombre le plus grand: ")

if choice == "a" and a > b :
    print(f"Le nombre a: {a} est plus grand que le nombre b: {b}.")
elif choice == "b" and a < b:
    print(f"Le nombre b {b} est plus grand que le nombre a {a}.")

else:
    print(f"Le nombre a et le nombre b sont égaux = {a}.")

