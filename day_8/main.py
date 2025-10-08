from pathlib import Path
import shutil
p = Path.home()

# a = p / "Documentos"

# c = a / "main.py"

# print(p)
# print(a)
# print(c)

# d = p.joinpath("Documentos", "file.tar.gz")

# b = Path.cwd()

# print(b)
# print(d)
# print(d.suffix)

# print(d.parent)
# print(d.name)
# print(d.stem)
# print(d.suffix)
# print(d.suffixes)
# print(d.parts)
# print(d.exists())
# print(d.is_dir())
# print(d.is_file())
p = p / "OneDrive/Bureau"
dossier = p / "DossierTest"

# dossier.mkdir()
# dossier = dossier / "1/2/3"
# dossier.mkdir(exist_ok=True, parents=True)
# dossier = dossier / "readme.txt"
# dossier.touch()
# dossier.unlink()
# shutil.rmtree(dossier)
# dossier.rmdir()

# dossier.write_text("Bonjour")
# read = dossier.read_text()
# print(dossier)
# print(read)

# for i in p.iterdir():
#     print(i.name)

for f in p.rglob("*png"):
    print(f.name)