import os

# Dictionnaire pour stocker les enchérisseurs et leurs offres
bidders = {}

def clear_terminal():
    """Efface le terminal, compatible Windows / Mac / Linux"""
    os.system('cls' if os.name == 'nt' else 'clear')

def user_information():
    """Demande les informations d'un utilisateur (nom et enchère)"""
    user_name = input("🧑 Entrez votre nom : ")
    while True:
        user_bid = input("💰 Quelle est votre enchère ? $")
        if user_bid.isdigit():  # Vérifie que c’est bien un nombre
            return {user_name: int(user_bid)}
        else:
            print("⚠️ Veuillez entrer un nombre valide.")

# --- Programme principal ---
clear_terminal()
print("🎯 Bienvenue à la vente aux enchères secrète ! 🎯\n")

bidders.update(user_information())

while True:
    other_bidder = input("Y a-t-il un autre enchérisseur ? (yes/no): ").lower()
    
    if other_bidder == "yes":
        clear_terminal()  # Nettoyage du terminal avant le suivant
        bidders.update(user_information())
    
    elif other_bidder == "no":
        clear_terminal()
        print("⏱️ Les enchères sont terminées !\n")
        break
    
    else:
        print("⚠️ Réponse invalide, tapez 'yes' ou 'no'.")
        continue

# --- Trouver le gagnant ---
winner_name = ""
highest_bid = 0

for name, bid in bidders.items():
    if bid > highest_bid:
        highest_bid = bid
        winner_name = name

print(f"🏆 Le gagnant est {winner_name} avec une enchère de ${highest_bid} 💵")

