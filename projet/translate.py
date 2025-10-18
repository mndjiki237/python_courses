"""
Projet 3 : Le Gardien de la Connaissance (Dictionnaire et Gestion des Erreurs)
Pour consolider vos compétences en Structures de Données (dictionnaires, Leçon 231+) 
et en Robustesse Logicielle (exceptions, Leçon 243+), nous allons créer un Gardien de la Connaissance.

Ce programme sera un outil de traduction simple qui doit pouvoir gérer 
avec élégance les requêtes pour des mots qu'il ne connaît pas.

Le programme devra :

Définir un dictionnaire nommé VOCABULAIRE_SACRE contenant quelques paires de mots Français/Anglais.

Créer une fonction nommée traduire_mot qui prend un mot en français en entrée.

Utiliser la gestion des erreurs (try/except, Leçon 244) pour chercher le mot dans le dictionnaire.

Si le mot est trouvé : la fonction retourne la traduction.

Si le mot n'est PAS trouvé : la fonction retourne un message 
inspirant expliquant qu'il faut aller chercher la connaissance ailleurs.

Demander à l'utilisateur de saisir un mot à traduire, appeler la fonction et afficher le résultat.

etape1
    creer un dictionnaire VOCABULAIRE_SACRE cle valeur chacune representant une langue
    creer une fonction traduire_mot qui prend en entrer un mots en francais
    verifier si le mot existe dans le dictionnaire 
    si oui 
        traduire le mot
    sinon
        recommander une recherche ailleur
etape 2
    creer une variable qui recupere a travers la fonction input qui demande a l'utilisateur d'entrer le mot qu il veux traduire
    appeler la foction VOCABULAIRE_SACRE et qui prend en entré le mot de l utilisateur 
    creer une variable reponse, qui recupere la reponse renvoyer par la fonction

"""

VOCABULAIRE_SACRE = {
    # Termes fondamentaux
    "mot": "word",
    "langue": "language",
    "écrire": "to write",
    "lire": "to read",
    "parler": "to speak",
    "écouter": "to listen",
    
    # Éléments naturels sacrés
    "ciel": "sky",
    "terre": "earth",
    "feu": "fire",
    "eau": "water",
    "vent": "wind",
    "soleil": "sun",
    "lune": "moon",
    "étoile": "star",
    
    # Concepts spirituels
    "âme": "soul",
    "esprit": "spirit",
    "dieu": "god",
    "divin": "divine",
    "sacré": "sacred",
    "prière": "prayer",
    "foi": "faith",
    "éternité": "eternity",
    
    # Émotions profondes
    "amour": "love",
    "paix": "peace",
    "joie": "joy",
    "espoir": "hope",
    "rêve": "dream",
    "sagesse": "wisdom",
    "vérité": "truth",
    
    # Relations humaines
    "famille": "family",
    "ami": "friend",
    "coeur": "heart",
    "vie": "life",
    "mort": "death",
    "naissance": "birth",
    
    # Éléments symboliques
    "lumière": "light",
    "ombre": "shadow",
    "chemin": "path",
    "porte": "door",
    "clé": "key",
    "livre": "book"
}

def traduire_mot(dictionnaire, mot_francais):
    # On garantit que la saisie est toujours en minuscules (Protection anti-casse)
    mot_recherche = mot_francais.lower() 
    
    traduction = ""
    try:
        # Fissure 1 colmatée : on cherche et on stocke dans la variable 'traduction'
        traduction = dictionnaire[mot_recherche]
    except KeyError:
        # Gestion des erreurs élégante et inspirante
        return "La Connaissance est vaste ! " \
               "Ce mot n'est pas encore dans notre Codex. Nous vous encourageons " \
               "à chercher sa magie plus loin dans l'Univers..."

    # Le trésor est retourné !
    return traduction 

# --- Programme Principal ---

mot_a_traduire = input("Entrer le mot à traduire (Alias Magique) : ")

# Appel de la fonction et stockage du résultat (mot trouvé OU message d'erreur)
mot_traduit = traduire_mot(dictionnaire=VOCABULAIRE_SACRE, mot_francais=mot_a_traduire)

# Le Héraut proclame le résultat, qu'il soit une traduction ou un message d'erreur.
print(f"\n✨ La réponse du Gardien pour '{mot_a_traduire}' est : {mot_traduit}")