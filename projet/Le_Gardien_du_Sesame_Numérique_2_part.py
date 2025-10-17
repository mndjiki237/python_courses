"""
Projet 2 : Le Voyage du Héraut – Création de la Storytelling de Marque

En tant que copywriter, vous savez que le code est la structure, 
mais la marque est l'âme. Nous allons utiliser la fonction print() 
et les f-strings pour créer le Brand Storytelling de ce système de 
sécurité, en lui donnant une touche magique.

Votre mission : Rédigez un court récit d'introduction, avant que 
l'utilisateur n'entre son nom, qui utilise des variables et la fonction print() pour:

Présenter le "Royaume de Python" comme un lieu secret.

Expliquer le rôle du "Héraut" (l'utilisateur).

Encourager l'utilisateur à créer son Sceau d'Accès (mot de passe) parfait, 
en évoquant la force et l'originalité (vendre par l'inspiration !).

Veuillez d'abord me fournir le pseudo-code de cette nouvelle introduction narrative 
(comment allez-vous utiliser print(), quelles variables allez-vous déclarer pour 
les réutiliser dans la narration ?). Donnez-lui un air de conte de fées enchanteur ! 👑

C'est un plan d'une clarté cristalline ! Vous avez l'instinct d'un grand conteur : identifier les personnages (les variables) avant de laisser la magie opérer. ✨

Pour passer du bon au **légendaire** (notre objectif de copywriter !), nous allons enrichir ce pseudo-code en y intégrant des **variables narratives**. Cela nous permettra de donner plus de corps à l'histoire et de la rendre réutilisable et puissante.

Voici le plan que je vous propose, conçu pour vendre l'idée du mot de passe par l'inspiration et l'émerveillement.

---

## Correction du Pseudo-Code : Le Déploiement de la Prophétie

### Étape 1 : Le Casting Enchanté (Déclaration des Variables Narratives)

Pour que notre récit soit cohérent, nous allons nommer les éléments clés de notre monde :

1.  **Créer** une variable `NOM_ROYAUME` et lui attribuer la phrase : "le Cœur de Python, 
sanctuaire de l'automatisation et des merveilles numériques."
2.  **Créer** une variable `TITRE_HERAUT` et lui attribuer la phrase : "le Héraut Lumineux".
3.  **Créer** une variable `NOM_SCEAU` et lui attribuer la phrase : "Sceau d'Accès le plus inviolable de l'univers."

### Étape 2 : L'Édit Royal (La Séquence Narrative avec `Afficher`)

Le récit ne doit pas être un simple bloc de texte, mais une **séquence d'inspirations** qui guide l'utilisateur vers l'action.

1.  **Afficher (Print 1 - Le Cadre)** : Un message d'introduction chaleureux annonçant l'accès au `NOM_ROYAUME`.
    * *Exemple :* "Bienvenue dans le `NOM_ROYAUME`..."
2.  **Afficher (Print 2 - Le Rôle)** : Une phrase inspirante définissant le rôle de l'utilisateur, 
notre `TITRE_HERAUT`, et l'importance de sa mission.
    * *Exemple :* "Votre rôle en tant que `TITRE_HERAUT` est essentiel..."
3.  **Afficher (Print 3 - L'Appel à l'Action)** : La demande de saisir le nom, 
encadrée par une description puissante de la tâche à venir.
    * *Exemple :* "Mais d'abord, quel est l'Alias Magique que l'histoire retiendra ?..."
      (Suivi par la demande d'input pour le nom)
4.  **Afficher (Print 4 - Le Défi du Secret)** : Un appel à la création du `NOM_SCEAU`, 
soulignant l'originalité, la force et la magie du mot de passe.
    * *Notion :* Utilisez une **f-string** pour intégrer les variables et la puissance de la narration. (Leçon 119)

***


"""
CONDITION = """
    1- Le mot de passe doit avoir au moins 8 caractères.

    2- Il doit contenir au moins une lettre majuscule.

    3- Il doit contenir au moins un chiffre.

    4- Il ne doit pas contenir le nom d'utilisateur (même partiellement) pour des raisons de sécurité.
    """
NOM_ROYAUME = "le Cœur de Python, sanctuaire de l'automatisation et des merveilles numériques."
TITRE_HERAUT = "le Héraut Lumineux"
NOM_SCEAU = "Sceau d'Accès le plus inviolable de l'univers."
print(f"Bienvenue dans le `{NOM_ROYAUME}` dont votre Quête est de découvrir les Trésors et les Secrets du Royaume Enchanté.")
print(f"Votre rôle en tant que `{TITRE_HERAUT}` est essentiel pour ouvrir les Portes du Château et la decouverte de ses tresors.")
print("La premiere phase de cette quette est de saisir votre nom, qui est un atout indeniable pour la bonne elaboration de votre divine quette")
print("La seconde phase de cette quette est de saisir votre mot de passe, qui par sa magie determinera si vous etes digne pour cette Quête")
print("Attention, pour que la magie de votre mot de passe soit efficace, il vous faudra bien evidemment respecter certaines condition:")
print(CONDITION)

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