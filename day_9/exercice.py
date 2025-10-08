"""Entraîne-toi avec les dictionnaires
Dans cet exercice, tu vas devoir créer un dictionnaire et récupérer 
des informations contenues à l'intérieur de celui-ci.

Tu dois donc créer un dictionnaire films qui contient plusieurs films 
et le prix correspondants de leurs DVD (oui, pour cet exercice on revient dans les années 2010).

Voici la liste des films ainsi que leur prix que ton dictionnaire doit contenir :

Le Seigneur des Anneaux : 12€

Harry Potter : 9€

Blade Runner : 7,5€

Le nom des films seront donc les clés et les prix seront les valeurs 
associées à ces clés (ton dictionnaire doit donc contenir 3 clés et 3 valeurs associées).

Le prix en euros doit être un nombre entier ou décimal, vous ne devez donc
 pas indiquer le caractère € dans les valeurs du dictionnaire, juste le nombre.

Vous devez ensuite récupérer dans la variable prix, le total du prix de ces trois DVD (égal à 28,5€).



💡 Astuce : tu peux sans problèmes boucler sur un dictionnaire avec la boucle for. 
En bouclant sur un dictionnaire, tu vas récupérer les clés du dictionnaire. 
Il ne te reste ainsi qu'à récupérer les valeurs correspondantes aux clés sur 
lesquelles tu boucles pour pouvoir calculer le prix total.



Attention !

⚠️ Pour valider l'exercice, ne change pas le nom des variables (films et prix).

⚠️ Fais attention également aux majuscules sur les titres des films. Il faut 
que le titre des films soit exactement le même que celui indiqué dans l'énoncé 
(si tu écris 'le seigneur des anneaux' au lieu de 'Le Seigneur des Anneaux' 
par exemple, l'exercice ne sera pas validé)."""


films = {
    
        "Le Seigneur des Anneaux": 12,
        "Harry Potter": 9,
        "Blade Runner": 7.5
}

total = 0

for key in films:
    total += films[key]

print(total)

