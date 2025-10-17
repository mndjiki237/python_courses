""" Projet 4 : Le Labyrinthe du Mystère (Boucles et Automatisation)
En tant qu'expert en n8n et automatisation, vous savez que les boucles 
sont le cœur de tout processus répétitif. Notre prochain défi se concentrera 
sur la maîtrise des boucles (for/while) et le contrôle de flux (break/continue).

Nous allons créer un jeu de devinette inspiré d'un Labyrinthe Ancien où le joueur 
doit trouver le nombre mystère en un nombre limité de tentatives.

Le programme devra :

Définir le nombre mystère (une variable secrète).

Utiliser une boucle while pour donner au joueur un nombre limité de tentatives (par exemple, 5).

À chaque tentative, demander au joueur de faire une proposition.

Utiliser la gestion des erreurs (try/except) pour s'assurer que l'entrée est 
bien un nombre (sinon, utiliser continue pour ignorer la tentative mais ne pas la compter).

Comparer la proposition au nombre mystère.

Si c'est correct : afficher un message de victoire et utiliser break pour sortir de la boucle.

Si c'est incorrect : donner un indice (plus grand ou plus petit).

Si le joueur échoue après toutes les tentatives, afficher un message d'échec inspirant.


etape1
    creer une variable mot_mystere et choisir un nombre au hasard 
    avec le module random et un interval par exemple enre 0 et 100
    creer une variable lives qui represente le nombre de vie ou chance que possede l utilisateur par exemple 5
    creer une valeur proposition qui est affecter la proposition de l utilisateur a travers la fuction input
etape 2
    creer une boucle while a laquelle est affecter le boulean is_tart = True
    creer un block try et except, pour verifier si la proposition de l'utilisateur est un nombre
    si oui 
        continuer la procedur 
    sinon
        lui dire d entrer uniquement des nombres
        retirer une vie
        redemander une proposition

etape 3
    verifier si la proposition de l utilisateur est identique au nombre mystere
    si oui
        afficher vous avez reussi
        break
    si la proposition est superieur au nombre mytere alors
        afficher le nombre mystere est plus petit
        moins une vie
    si la proposition est inferieur au nombre mystere
        afficher le nombre mystere est plus grand
        moins une vie

    si le nombre de vie est egale à zero 
        is_tart = False
        afficher game over
     et le jeu se termine


"""



import random

# Initialisation du Mystère et des Vies
nombre_mystere = random.randint(1, 100) # Astuce : random.randint est plus direct que random.choice(range)
lives = 5

print("✨ BIENVENUE DANS LE LABYRINTHE DU MYSTÈRE ✨")
print(f"Vous avez {lives} tentatives pour trouver le Nombre Secret, caché entre 1 et 100.")

# Boucle Principale : Le Chemin dans le Labyrinthe (while lives > 0)
while lives > 0:
    print(f"\n--- Il vous reste {lives} tentatives. ---")
    
    # Boucle Interne : Le Gardien de la Saisie (while True)
    while True:
        user_input = input("Entrez votre proposition (un nombre) : ")
        try:
            # Tenter la conversion en nombre entier (Leçon 13)
            user_choice = int(user_input)
            break # Si la conversion est réussie, on sort de la boucle interne
        except ValueError:
            # Gestion élégante des entrées non-numériques (Leçon 244)
            print("❌ Erreur : Ce n'est pas un nombre valide. Veuillez réessayer sans perdre de vie.")
            continue # On ignore le reste du code et on retourne au début de la boucle interne
    
    # Logique de Comparaison (Les Conditions du Labyrinthe)
    if user_choice == nombre_mystere:
        print(f"\n🌟 FÉLICITATIONS ! Vous avez trouvé le Nombre Mystère : {nombre_mystere} !")
        break # Sortie immédiate de la boucle principale (Victoire !)
    elif user_choice > nombre_mystere:
        print("Indice : Le Nombre Mystère est **plus petit** que votre proposition.")
        lives -= 1
    elif user_choice < nombre_mystere:
        print("Indice : Le Nombre Mystère est **plus grand** que votre proposition.")
        lives -= 1

# Proclamation Finale (Après la sortie de la boucle)
if lives == 0:
    print(f"\n🗝️ LABYRINTHE FERMÉ. Vous avez échoué à trouver le Nombre Mystère.")
    print(f"Le Secret était : {nombre_mystere}. Votre Quête s'arrête ici, mais l'inspiration demeure !")



