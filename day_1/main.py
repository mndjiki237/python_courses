"""Créez un accueil pour votre programme.
Demandez à l'utilisateur la ville où il a grandi et stockez-la dans une variable.
Demandez à l'utilisateur le nom d'un animal de compagnie et stockez-le dans une variable.
Combine le nom de leur ville et de leur animal de compagnie et montre-leur le nom de leur groupe."""


print("Bienvenue dans le generateur de Nom")

ville = input("Quel est la ville où tu as grandi ? ")
nom_animal_de_compagnie = input("Quel est le nom de ton animal de compagnie ? ")
nom_groupe = f"{ville}-{nom_animal_de_compagnie}"

print(nom_groupe)