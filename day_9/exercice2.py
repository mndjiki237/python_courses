"""Les dictionnaires
Dans cet exercice, nous avons un dictionnaire qui 
représente plusieurs employés d'une entreprise avec différents id.

Patrick a quitté l'entreprise cette année, nous devons donc l'enlever du dictionnaire.

Julie a fêté son anniversaire hier, il faut donc changer son âge (elle a maintenant 26 ans).

Paul quant à lui fêtera son anniversaire la semaine prochaine. 
Nous voulons donc récupérer son âge pour savoir quel âge il aura.

Notre dictionnaire sera donc égal à la fin du script à :

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 26}
            }
Il faudra également récupérer l'âge de Paul dans une variable 'age_paul', qui devra donc être égale à 32."""


employes = {
    "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
    "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
    "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
}

# On crée une liste des clés à supprimer pour éviter de modifier pendant la boucle
cles_a_supprimer = []

for key, value in employes.items():
    print(value.get("prenom"))
    if value.get("prenom") == "Patrick":  # correction du nom
        cles_a_supprimer.append(key)
    
    if value.get("prenom") == "Julie":  # correction du nom
        value["age"] += 1

for key in cles_a_supprimer:
    employes.pop(key, None)

print(employes)
