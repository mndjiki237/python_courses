"""Énoncé du problème
Ecrire un programme Python pour calculer 
l'aire d'un cercle en utilisant la formule Πr2"""

rayon = input("Donner le rayon du cercle dont vous vouler calculer l'air: ")
air = 0

if rayon.isdigit():
    rayon = float(rayon)
    air = 3.14 * rayon * rayon

    print(f"L'air du cercle Πr2 (3,14 x {rayon} x {rayon}) est de: {air}")