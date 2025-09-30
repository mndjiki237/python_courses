a = "1, 2, 3, 4"

b = a.split(", ")

print(b)

c = ",".join(b)
d = "-".join(b)
print(c)
print(d)

chaine = "Pierre, Julien, Anne, Marie, Lucien"

print(f"la chaine: {chaine}")

chaine_en_ordre = ", ".join(sorted(chaine.split(", ")))

print(f"la chaine en ordre: {chaine_en_ordre}")
