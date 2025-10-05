"""Énoncé du problème
Ecrire un programme pour montrer ce type de disposition des nombres et des carrés.
Résultat attendu :
Nombre        square

1                1
2                4   
3                9
4                16
5                25
6                36
7                49
8                72
9                81
"""

print("number \t\t square")
for i in range(1,9):
    print(f"{i} \t\t {i*i}")