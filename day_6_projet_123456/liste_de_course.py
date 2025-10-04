"""
    Dans ce projet, tu vas devoir créer un programme en ligne 
    de commande qui permet de manipuler une liste de courses.

Déroulé du script
Le programme doit permettre de réaliser 5 actions :

Ajouter un élément à la liste de courses

Retirer un élément de la liste de courses

Afficher les éléments de la liste de courses

Vider la liste de courses

Quitter le programme

Tu dois donc demander à l'utilisateur de choisir parmi une 
de ces action en entrant un nombre de 1 à 5.

    """


MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]



liste_de_course = []
is_game = True

while is_game:

    print(f"Choisissez parmir les 5 options suivants: ")
    
    user_choice = input(MENU)

    if not user_choice in MENU_CHOICES:
        print("Mauvais élément! veuillez saissir un nombre compris entre 1 et 5")
        continue
        
    if user_choice == "1":
        item = input("Entrer le nom de l'element a ajouter dans la liste de course: ")
        if not item in liste_de_course:
            liste_de_course.append(item)
            print(f"l'element {item} a bien été ajouté a la liste.")
        else:
            print(f"l'element {item} a deja été ajouté a la liste.")
    
    elif user_choice == "2":
        item = input("Entrer le nom de l'element a retirer dans la liste de course: ")

        print(f"l'element {item} a bien été retié a la liste.")
        liste_de_course.remove(item)
    elif user_choice == "3":
        if liste_de_course:
            for i in range(len(liste_de_course)):
                print(f"{i+1}. {liste_de_course[i]}")
        else:
            print("la liste ne contient aucun élément")
    elif user_choice == "4":
        liste_de_course.clear()
        print("La liste de course a été vidé de son contenu.")
    elif user_choice == "5":
        print("A bientot!")
        is_game = False
    
    print("\n" )
    print("-" * 50)

        

  

