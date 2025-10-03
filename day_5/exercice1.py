"""
Récupérer des éléments avec les slices
Dans cet exercice, vous devez récupérer différents morceaux d'une liste grâce aux slices.

La liste de départ est la suivante :

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
L'objectif de cet exercice est de récupérer les informations suivantes grâce aux slices :

Les trois premiers employés ("Maxime", "Martine" et "Christopher") dans une liste trois_premiers

Les trois derniers employés ("Carlos", "Michael" et "Éric") dans une liste trois_derniers

Tous les employés sauf le premier et le dernier dans une liste milieu

Le premier et le dernier employé dans une liste premier_dernier    

    """

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[0:3]# INSÉRER CODE ICI
trois_derniers = liste[3:]# INSÉRER CODE ICI
milieu = liste[1:-1] # INSÉRER CODE ICI
# premier_dernier = liste[:1] + liste[-1:] # INSÉRER CODE ICI
# premier_dernier = liste[::5]
premier_dernier = liste[::len(liste)-1]
print(trois_premiers)
print(trois_derniers)
print(milieu)
print(premier_dernier)