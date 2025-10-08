from pathlib import Path

CUR_DIR = Path(__file__).resolve()


chemin = CUR_DIR.parent / "dossier_test"
 
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

dir = ""

for key, value in d.items():
    first_dir = chemin / key
    first_dir.mkdir(exist_ok=True)
    for dir in value:
        dirs = first_dir / dir
        dirs.mkdir(exist_ok=True)

