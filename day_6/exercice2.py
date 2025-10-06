"""Dans cet exercice vous devez afficher les lettres du mot 'Python' 
dans le sens inverse. Votre script devra donc afficher :

n
o
h
t
y
P"""

language = "Python"
language = language[::-1]
# language = "".join(reversed(language))
print(language)

for i in range(len(language) -1):
    print(language[i])
