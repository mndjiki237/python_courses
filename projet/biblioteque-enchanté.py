""" Votre Prochain Défi (Projet 6) : Le Conservateur de la Bibliothèque Enchantée
Pour consolider ces nouvelles connaissances avec l'esprit du Brand Storytelling et 
de l'Automatisation, votre prochain projet sera de construire un système qui gère une bibliothèque d'enchantements.

Mission : Le Conservateur de la Bibliothèque
Vous devrez écrire un programme qui gère une liste de titres d'enchantements (des chaînes de caractères).

Créer une liste (Listes - Leçon 144) de 10 titres d'enchantements (ex: "Sortilège de Vitesse", "Miroir d'Illusion").

Créer une fonction nommée organiser_bibliotheque qui prend cette liste en entrée.

À l'intérieur de la fonction :

Nettoyer la liste : Supprimer le titre le plus court et le titre le plus long. 

Trier la liste par ordre alphabétique (Leçon 155).

Ajouter votre propre titre inspirant à la fin de la liste (Leçon 149).

En dehors de la fonction :

Créer un tuple (Tuples - Leçon 160) à partir des deux premiers titres de la liste 
finale pour les désigner comme les "Sceaux Fondateurs".

Afficher les titres des Sceaux Fondateurs (le tuple) et la liste finale, avec un message 
inspirant sur l'ordre et la beauté de la connaissance.

etape 1:
    Créer une liste de 10 titres d'enchantements
    Créer une fonction organiser_bibliotheque qui prend en entré cette liste
    dans la fonction Supprimer le titre le plus court et le titre le plus long
    ensuite trier la liste actuel par ordre alphabetique
    ajouter un titre inspirant a la fin de la liste 
etape 2
    creer un tuple a partir des deux premiere tittre de la liste finale
    les identifier comme sceau fondateur
    Afficher les titres des Sceaux Fondateurs (le tuple) et la liste finale, avec un message 
    inspirant sur l'ordre et la beauté de la connaissance.

"""

enchantements = [
    "Lame de l'Éclipse",
    "Carapace de Granit", 
    "Souffle du Dragon Blanc",
    "Marche sur les Ombres",
    "Lien d'Âmes Sœurs",
    "Barrière de Silence",
    "Valse des Mille Lames",
    "Ouragan de Givre",
    "la Flamme Éternelle",
    "oeil de la Sorcière",
    "Murmures du Néant", 
    "Jardin d'Illusions",
    "Étreinte de la Vigne Vénéneuse",
    "La Couronne de la Sagesse Ancienne",
    "Chant de la Sirène Oubliée"
]

def organiser_bibliotheque(ma_liste):
    # Fissure 1 colmatée : Utilisation de key=len pour trouver le plus long et le plus court
    # On utilise ma_liste dans la fonction max/min.
    
    # 1. Supprimer le titre le plus long
    titre_le_plus_long = max(ma_liste, key=len)
    ma_liste.remove(titre_le_plus_long)
    
    # 2. Supprimer le titre le plus court
    titre_le_plus_court = min(ma_liste, key=len)
    ma_liste.remove(titre_le_plus_court)

    # 3. Fissure 2 colmatée : Tri en place (ma_liste.sort())
    ma_liste.sort()

    # 4. Ajouter votre propre titre inspirant
    ma_liste.append("L'Enchantement de l'Inspiration Suprême") 

    return ma_liste


bibliotheque_finale = organiser_bibliotheque(enchantements)

# Création du Tuple des Sceaux Fondateurs (Leçons 146, 160)
# Nous utilisons les 2 premiers éléments de la liste triée
sceaux_fondateurs = tuple(bibliotheque_finale[0:2])

# --- Proclamation Inspirante ---
print("\n📜 L'ORDRE ET LA BEAUTÉ DE LA CONNAISSANCE ONT PRIS LEUR PLACE 📜")
print("---")
print("Le Secret Récemment Ajouté (Leçon 149) :")
print(f"**{bibliotheque_finale[-1]}**") # Utilisation de l'index -1 pour le dernier élément

print("\nLes Sceaux Fondateurs (Le Tuple Immuable) :")
print(f"Ces deux enchantements sont l'essence de notre Codex : {sceaux_fondateurs}")

print("\nLa Bibliothèque Organisée (Liste Finale - Triée et Filtrée) :")
for titre in bibliotheque_finale:
    print(f"- {titre}")