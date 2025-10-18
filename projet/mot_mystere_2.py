""" Projet 5 : Le Scribe de la Prophétie (I/O, JSON et Pathlib)
Maintenant que vous maîtrisez la logique et les boucles, nous allons 
nous concentrer sur le cœur de l'automatisation et du Brand Storytelling : 
la gestion des données et des fichiers.

Ce projet utilisera le jeu que vous venez de créer pour enregistrer 
les exploits (ou les échecs) des joueurs dans un journal magique.

Le programme devra :

Reprendre le code complet du jeu du Labyrinthe.

Utiliser le module json pour enregistrer les résultats dans un fichier.

Créer une fonction nommée enregistrer_resultat qui prend en paramètres : 
le nom du joueur, le statut de la partie (Gagné/Perdu) et le nombre de tentatives restantes.

Cette fonction devra :

Définir le nom du fichier de journal (journal_des_herauts.json).

Lire le contenu existant du fichier JSON (s'il existe).

Ajouter le nouveau résultat à la liste des enregistrements.

Réécrire la liste complète dans le fichier JSON.

etape 1
    importer le module json
    creer une fonction enregistrer_resultat qui prend en entree :
    le nom du joueur, le statut de la partie (Gagné/Perdu) et le nombre de tentatives restantes. 
    creer un fichier journal_des_herauts.json a l interieur de la fonction si non existe
etape 2
    lire le fichier si existe
    ajouter les element du status du jour, initial pour une premiere partie
    pour chacque partie effectuer, lire le fichier et reecrire les unevelles infprmations 




"""
import json
from pathlib import Path 
import random
# NOTE : `os` n'est plus nécessaire car `pathlib` est utilisé.

# --- PARAMÈTRES ET INITIALISATION ---

# Utilisation de Pathlib pour le chemin (meilleure pratique)
# Path(__file__).resolve().parent est l'endroit le plus sûr pour le fichier,
# en assumant que le script est dans un environnement réel.
FICHIER_JOURNAL = Path(__file__).resolve().parent / "journal_des_herauts.json" 

nombre_mystere = random.randint(1, 100)
lives = 5

print("✨ BIENVENUE DANS LE LABYRINTHE DU MYSTÈRE ✨")
print(f"Vous avez {lives} tentatives pour trouver le Nombre Secret, caché entre 1 et 100.")

user_name = input("Entrer votre nom de Héraut (Alias Magique) : ")
# Fissure 3 colmatée : Initialisation du statut
status_du_jour = "Abandon" 
tentatives_utilisees = 5 


# --- DÉFINITION DE LA FONCTION ---

def enregistrer_resultat(nom_joueur, statut_partie, tentatives_finales):
    """Enregistre le résultat de la partie dans un journal JSON structuré."""
    
    # 1. Préparation du nouvel enregistrement
    nouvel_enregistrement = {
        "heraut": nom_joueur,
        "statut": statut_partie,
        "tentatives_restantes": tentatives_finales
    }
    
    # 2. Lecture du Codex Ancien (avec double protection des exceptions)
    enregistrements = []
    try:
        with open(FICHIER_JOURNAL, "r") as f:
            # Fissure 1 colmatée : gestion de deux erreurs spécifiques
            enregistrements = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si le fichier n'existe pas OU s'il est vide/mal formé, on commence avec une liste vide.
        enregistrements = []
        
    # 3. Ajout et Écriture du Fichier
    # Fissure 2 colmatée : Ajout d'un DICTIONNAIRE à la liste
    enregistrements.append(nouvel_enregistrement) 

    try:
        with open(FICHIER_JOURNAL, "w") as f:
            json.dump(enregistrements, f, indent=4)
        print("\n📜 Le Scribe a gravé votre exploit dans le Journal des Hérauts. (journal_des_herauts.json)")
    except Exception as e:
        print(f"\n❌ Erreur critique lors de l'écriture du journal: {e}")


# --- LOGIQUE DE JEU ---

while lives > 0:
    print(f"\n--- Il vous reste {lives} tentatives. ---")
    
    # Boucle Interne pour la Saisie Valide
    while True:
        user_input = input("Entrez votre proposition (un nombre) : ")
        try:
            user_choice = int(user_input)
            break
        except ValueError:
            print("❌ Erreur : Ce n'est pas un nombre valide. Veuillez réessayer.")
            continue
    
    # Logique de Comparaison
    if user_choice == nombre_mystere:
        print(f"\n🌟 FÉLICITATIONS ! Vous avez trouvé le Nombre Mystère : {nombre_mystere} !")
        status_du_jour = "Gagné" # Mettre à jour le statut
        tentatives_utilisees = 5 - lives # Calculer les tentatives
        break 
    elif user_choice > nombre_mystere:
        print("Indice : Le Nombre Mystère est **plus petit** que votre proposition.")
        lives -= 1
    elif user_choice < nombre_mystere:
        print("Indice : Le Nombre Mystère est **plus grand** que votre proposition.")
        lives -= 1

    tentatives_utilisees = 5 - lives # Mettre à jour le nombre de tentatives utilisées


# --- PROCLAMATION FINALE & ENREGISTREMENT ---

if lives == 0:
    print(f"\n🗝️ LABYRINTHE FERMÉ. Vous avez échoué à trouver le Nombre Mystère.")
    print(f"Le Secret était : {nombre_mystere}. Votre Quête s'arrête ici, mais l'inspiration demeure !")
    status_du_jour = "Perdu"
    # tentatives_utilisees reste à 5

# Appel final à la fonction pour sceller l'enregistrement
enregistrer_resultat(user_name, status_du_jour, 5 - lives)