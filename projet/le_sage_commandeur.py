""" 

Projet 2 : Le Sage Commandeur (Vers les Fonctions et les Mots)

Maintenant que vous maîtrisez les bases de la structure, nous allons 
nous attaquer à la réutilisation du code (une nécessité pour un développeur 
Python et un expert en n8n/automation !). Notre prochain projet portera sur 
les Fonctions 
Nous allons construire un outil pour les rédacteurs inspirés comme vous, 
un Sage Commandeur qui analysera la richesse et la force d'un texte.

Le programme devra :

Utiliser une fonction nommée analyser_texte qui prend un texte en entrée.

Calculer le nombre total de mots dans le texte.

Calculer le nombre total de phrases dans le texte (en utilisant le point, 
le point d'interrogation et le point d'exclamation comme séparateurs).

Retourner (return) ces deux valeurs (mots et phrases).

Afficher un message inspirant pour le rédacteur, lui donnant ses statistiques.
Votre plan est digne d'un grand stratège ! ✍️ Vous avez parfaitement identifié les éléments fondamentaux de notre Sage Commandeur : l'entrée (le paramètre texte), les mesures de la force du récit (mots et phrases) et la sortie structurée (return).

Pour que notre pseudo-code soit une véritable feuille de route magique pour le code Python, nous allons y insérer l'Algorithme du Sage. C'est le moment d'utiliser les méthodes de chaînes de caractères que vous avez étudiées pour donner corps à ces calculs.

Voici le plan raffiné, décrivant la manière dont les calculs seront effectués :

Correction du Pseudo-Code : L'Algorithme du Sage
Étape 1 : Le Rituel d'Analyse (La Définition de la Fonction)
    Définir la fonction analyser_texte acceptant un paramètre nommé texte.

    Utiliser la méthode de Séparation Magique (split) sur l'argument texte pour le diviser 
    en une liste de mots (par défaut, en utilisant les espaces).

    Stocker la longueur (le compte) de cette liste dans la variable total_mots.

    Initialiser la variable total_phrases à zéro.

    Ajouter à total_phrases le nombre d'occurrences du point (.) dans le texte.

    Ajouter à total_phrases le nombre d'occurrences du point d'interrogation (?) dans le texte.

    Ajouter à total_phrases le nombre d'occurrences du point d'exclamation (!) dans le texte.

    Retourner (Leçon 246) :

    Renvoyer les deux valeurs total_mots et total_phrases.

Étape 2 : La Proclamation des Résultats (L'Appel de la Fonction)
    Définir un bloc de texte inspirant que vous souhaitez analyser (la prose_enchantee).

    Appeler la fonction analyser_texte avec la prose_enchantee et stocker 
    les deux valeurs retournées (mots et phrases) dans deux variables distinctes.

    Afficher un message inspirant (utilisant une f-string, Leçon 119) qui révèle au rédacteur :

    Le nombre de mots qu'il a tissé.

    Le nombre de phrases qu'il a enchanté.

"""
def analyser_texte(texte):
    
    ponctuation = [".", "?", "!"]
    total_mots = len(texte.split())
    total_phrases = len([i for i in texte if i in ponctuation])

    return [total_mots, total_phrases]

mon_texte = """Le copywriting, ce n'est pas juste écrire. C'est sculpter la langue pour qu'elle persuade, 
émeuve et convertisse. Imaginez : un seul mot peut changer toute la perception d'une marque. Incroyable, n'est-ce pas ?

Chaque jour, c'est un nouveau défi. Trouver la phrase qui accroche, le slogan qui reste en tête, 
l'appel à l'action qui est impossible à refuser ! Vous ne vous contentez pas de vendre un produit ;
 vous vendez une émotion, une solution, une histoire.

Alors, prêt à transformer votre passion pour les mots en une force de frappe redoutable ? 
Le pouvoir est entre vos mains. Utilisez-le avec sagesse"""


data = analyser_texte(mon_texte)

print(data)

print(f"Votre texte contient {data[0]} mots et {data[1]} phrases")