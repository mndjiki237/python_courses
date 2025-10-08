"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""

from pathlib import Path

BASE_FILE = Path(__file__).resolve()

text_file = BASE_FILE.parent / "prenoms.txt"
text_file_2 = BASE_FILE.parent / "prenoms_2.txt"
text_file_2.touch(exist_ok=True)

# read = sorted(text_file.read_text().split(", "))

# with open(text_file_2, "a") as f:
#     for i in range(len(read)-1):

#         f.write(f"{read[i].strip("., ")} \n")


with open(text_file, "r") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(text_file_2, "w") as f:
    f.write("\n".join(sorted(prenoms_final)))