"""
Nous allons construire un calculateur de pourboire.

(150,00 / 5) * 1,12 = 33,6

Après avoir formaté le résultat à 2 décimales = 33,60

"""

print("Bienvenue dans la calculatrice de pourboire")

bill = int(input("Veuillez entrer le montant de la facture: "))

tip_a_percent = int(input("Quel pourcentage voulez vous payer parmis ces trois choix(10, 12, 15): "))/100

number_of_person = int(input("veuillez renseigner le nombre de personne devant payer: "))

result = bill*(1 + tip_a_percent)/number_of_person

print(f"tout le monde doit payer: {(result):.2f} ")