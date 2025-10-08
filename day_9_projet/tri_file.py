"""

Étape 1 — Observer et trier

    * Lister les extensions :
        - Le programme regarde tous les fichiers dans le dossier “data”

    * Trier selon les extensions :
        - Le programme regarde la fin du nom du fichier (comme .mp3, .jpg, .pdf…)
          pour savoir à quel type il appartient (musique, image, vidéo, etc.).

    * Mettre les fichiers dans une liste :
        - Tous les fichiers trouvés sont mis dans une “boîte temporaire” (une liste Python)
          pour les ranger plus tard.

Étape 2 — Créer et ranger dans les bons dossiers

    * Créer des dossiers :
        -  Le programme fabrique des dossiers (s’il n’existent pas déjà)
           qui s’appellent : Musique, Images, Vidéos, Documents, Autres.

    * Déplacer les fichiers :
        - Ensuite, il prend chaque fichier un par un et le range dans le bon dossier,
"""
# On importe Path pour jouer avec les fichiers et dossiers
from pathlib import Path

# On dit où se trouve notre dossier principal "data"
SOURCE_FILE = Path(__file__).resolve()
CUR_DIR = SOURCE_FILE.parent
DATA_DIR = CUR_DIR / "data"

# On crée un dictionnaire pour dire : "si tu vois cette extension → range dans ce dossier"
data_extension = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents"
}

# On verifie tous les fichiers qui sont dans le dictionnaire "data_extension"
for file in DATA_DIR.iterdir():
    # Si c’est un fichier (et pas un dossier)
    if file.is_file():
        # On verifie l’extension du fichier (.mp3, .jpg, etc.)
        extension = file.suffix
        
        # On cherche le bon dossier, sinon on met dans "Autres"
        dossier_cible = DATA_DIR / data_extension.get(extension, "Autres")
        
        # On crée le dossier s’il n’existe pas déjà
        dossier_cible.mkdir(exist_ok=True)
        
        # On déplace le fichier dans le bon dossier
        file.rename(dossier_cible / file.name)
