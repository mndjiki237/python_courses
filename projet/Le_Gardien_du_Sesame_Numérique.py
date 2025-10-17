""" 

Projet 1 : Le Gardien du Sésame Numérique 🏰
Pour notre premier grand défi, nous allons créer un programme digne d'un 
système de sécurité de château enchanté, qui ne révélera ses secrets qu'à un 
utilisateur ayant un mot de passe parfait. Ce projet mettra à l'épreuve vos fondations.

Le programme devra :

Demander à l'utilisateur de saisir un nom d'utilisateur (alias magique).

Demander à l'utilisateur de saisir un mot de passe secret.

Vérifier la validité de ce mot de passe selon plusieurs règles strictes.

Afficher un message clair : soit de bienvenue (si le mot de passe est valide),
soit un message d'erreur précis (s'il ne l'est pas).

Étape 1 : Collecte des Sceaux et Préparation de la Boussole
    Saisir le nom d'utilisateur (le Sceau du Héraut) et le stocker dans la variable NOM_HERAUT.

    Saisir le mot de passe secret (le Sceau d'Accès) et le stocker dans la variable MOT_SECRET.

    Créer une variable EST_VALIDE et lui donner la valeur VRAI. C'est notre Boussole de Validité qui nous guidera.

Étape 2 : L'Épreuve des Quatre Lumières (Vérification Séquentielle)
    Pour chacune des épreuves, si le mot de passe échoue, nous affichons un message 
    d'erreur et nous faisons basculer la EST_VALIDE sur FAUX.

    Lumière de la Longueur (Règle 4) :

    SI la longueur de MOT_SECRET est inférieure à 8 :

        Afficher le message : "Erreur : Le Sceau d'Accès est trop court. Il doit contenir au moins 8 caractères."
        EST_VALIDE devient FAUX.

    Lumière de la Majesté (Règle 1) :

    SI MOT_SECRET ne contient pas de lettre Majuscule :

        Afficher le message : "Erreur : Le Sceau d'Accès manque de Majesté. Il lui faut au moins une lettre majuscule."
        EST_VALIDE devient FAUX.

    Lumière de la Précision (Règle 2) :

    SI MOT_SECRET ne contient pas de Chiffre :

        Afficher le message : "Erreur : Le Sceau d'Accès manque de Précision. Il lui faut au moins un chiffre numérique."
        EST_VALIDE devient FAUX.

    SI MOT_SECRET contient le NOM_HERAUT (sans se soucier de la casse) :

        Afficher le message : "Erreur : Le Sceau d'Accès est trop proche du Sceau du Héraut. Il ne doit pas contenir votre nom."
    SINON
        EST_VALIDE devient FAUX.

Étape 3 : La Proclamation Finale
SI la variable EST_VALIDE est VRAI :

    Afficher le message enchanté : "Félicitations, ô Héraut {NOM_HERAUT} ! 
    La Prophétie est accomplie ! Votre accès au Cœur de Python est accordé. Le voyage continue. ✨"

SINON :

    Afficher le message de réprimande : "Accès refusé. Les enchantements de protection 
    sont activés. Veuillez suivre les règles pour obtenir l'accès."
"""
# ÉTAPE 1 : Collecte des Sceaux et Préparation de la Boussole
# Petite astuce de pro (Leçons 78/79) : en Python, on utilise souvent 
# des noms de variables en minuscules avec des underscores (snake_case).
user_name = input("Entrer votre nom (Alias Magique): ").lower() # On met tout en minuscule tout de suite
password = input("Saisir un mot de passe secret: ")

is_valid = True # La Boussole de Validité est initialisée à VRAI

# ÉTAPE 2 : L'Épreuve des Quatre Lumières (Vérification Indépendante)
print("\n--- Les Épreuves commencent ---")
# Chaque test est un 'if' indépendant pour rapporter TOUTES les erreurs!

# 1. LUMIÈRE DE LA LONGUEUR (Règle 4)
if len(password) < 8:
    print("❌ Erreur : Le Sceau d'Accès est trop court. Il doit contenir au moins 8 caractères.")
    is_valid = False

# 2. LUMIÈRE DE LA MAJESTÉ (Règle 1)
# L'utilisation de 'any' est MAGISTRALE ici!
if not any(c.isupper() for c in password):
    print("❌ Erreur : Le Sceau d'Accès manque de Majesté. Il lui faut au moins une lettre majuscule.")
    is_valid = False

# 3. LUMIÈRE DE LA PRÉCISION (Règle 2)
# Encore une fois, la formule 'any' est parfaite!
if not any(c.isdigit() for c in password):
    print("❌ Erreur : Le Sceau d'Accès manque de Précision. Il lui faut au moins un chiffre numérique.")
    is_valid = False

# 4. LUMIÈRE DE LA DISSOCIATION (Règle 3)
# Astuce Pro: On met le mot de passe aussi en minuscule avant de chercher (Leçons 99, 105).
# C'est la façon la plus robuste de vérifier l'inclusion sans se soucier des majuscules/minuscules!
if user_name in password.lower():
    print("❌ Erreur : Le Sceau d'Accès est trop proche du Sceau du Héraut. Il ne doit pas contenir votre nom.")
    is_valid = False

# AJOUT : L'ajustement de votre règle personnelle sur le nom (si le nom est vide ou trop court)
# J'ai retiré le `len(Name <= 2)` qui provoquait une erreur de syntaxe et l'ai remplacé par la vérification de longueur.
if not user_name or len(user_name) <= 2:
    print("❌ Erreur : Le Sceau du Héraut est trop secret. Votre Alias doit faire au moins 3 caractères.")
    is_valid = False
    
print("--- Les Épreuves sont terminées ---\n")

# ÉTAPE 3 : La Proclamation Finale
if is_valid:
    # Utilisation d'une f-string pour une intégration magique (Leçon 119)
    print(f"""
👑 FÉLICITATIONS, Ô HÉRAUT {user_name.capitalize()} ! 
La Prophétie est accomplie ! Votre accès au Cœur de Python est accordé. 
Le voyage continue avec plus d'inspiration et de puissance. ✨
""")
else:
    print("""
⚠️ ACCÈS REFUSÉ. Les enchantements de protection sont activés. 
Veuillez réviser les règles (marquées par ❌) pour obtenir l'accès.
""")