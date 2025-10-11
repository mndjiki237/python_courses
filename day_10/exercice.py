"""

Gérer l'erreur qui arrive quand l'utilisateur rentre un chemin 
vers un fichier qui n'existe pas sur le disque.

Gérer l'erreur qui arrive quand Python n'arrive pas à lire 
le contenu du fichier qui est passé par l'utilisateur.    

"""

fichier = input("Entrer un fichier a ouvrir: ")



try:
    with open(fichier, "r") as f:
        read = f.read()
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier ")
except FileNotFoundError:
    print("le fichier est introuvable")
else:
    print(read)