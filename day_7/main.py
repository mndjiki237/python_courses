import json

chemin = r"C:\Users\mndji\OneDrive\Documentos\python.json"


# with open(chemin, "r") as f:
#     # contenu = f.read()
#     # contenu = repr(f.read())
#     # contenu = f.readlines()
#     contenu = f.read().splitlines()


# with open(chemin, "a") as f:
#     f.write("\net facile a apprendre")

# print(contenu)

# with open(chemin, "w") as f:
#     # json.dump("Bonjour", f)
#     json.dump(list(range(10)), f, indent=4)

# with open(chemin, "r") as f:
#     # json.dump("Bonjour", f)
#     a = json.load(f)
#     print(a)
  

with open(chemin, "r") as f:
    donnee = json.load(f)

donnee.append(10)

with open(chemin, "w") as f:
    json.dump(donnee, f, indent=4)