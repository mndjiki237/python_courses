# -*- coding: utf-8 -*-
"""
Mini chiffreur universel 🔐
---------------------------
Auteur : Moïse ✨
Version simplifiée et commentée par GPT-5

Ce programme permet de chiffrer ("encode") ou déchiffrer ("decode")
un message composé de lettres, chiffres ou symboles.
Le principe : décaler chaque caractère d’un certain nombre dans sa catégorie.
"""

import string

def ceasar(groups, menu):
    # --- 3. Fonction principale ---
    while True:
        print(menu)
        choice = input("Your choice: ").strip().lower()

        if choice not in ["1", "2", "encode", "decode"]:
            print("⚠️ Invalid choice. Please try again.\n")
            continue

        message = input("Enter your message: ")
        shift = input("Enter your encrypt number: ")

        if not shift.isdigit():
            print("⚠️ Please enter a valid number.\n")
            continue

        shift = int(shift)
        encrypt_word = ""  # Réinitialisé à chaque boucle

        # --- 4. Pour chaque caractère dans le message ---
        for char in message:
            encrypted_char = char  # Par défaut inchangé

            # On parcourt les groupes (lettres, chiffres, symboles)
            for group in groups:
                
                if char in group:

                    index = group.index(char)
                    if char == " ":
                        encrypted_char = group[index] 
                    elif choice in ["encode", "1"]:
                        index = (index + shift) % len(group)  # Décalage circulaire
                    else:
                        index = (index - shift) % len(group)
                    encrypted_char = group[index]
                    break  # On a trouvé le bon groupe, inutile de continuer
            encrypt_word += encrypted_char

        # --- 5. Résultat ---
        action = "Encrypted" if choice in ["encode", "1"] else "Decrypted"
        print(f"\n✅ {action} message: {encrypt_word}\n")

        # --- 6. Option pour rejouer ---
        again = input("Do you want to try again? (yes/no): ").lower()
        if again not in ["yes", "y", "oui", "si"]:
            print("\n🪶 Goodbye! Stay encrypted 💫")
            break


# --- 1. Définition des groupes de caractères ---
letters = list(string.ascii_letters)  # Lettres majuscules + minuscules
numbers = list(string.digits)         # Chiffres de 0 à 9
symbols = list(string.punctuation) # Symboles
space = [" "]  # espace
# On regroupe tout pour traitement facile
groups = [letters, numbers, symbols, space]

# --- 2. Messages d’introduction ---
menu = """
--------------------------------
🔐 Simple Encrypt / Decrypt Tool
--------------------------------
1 - Type "encode" or "1" to encrypt
2 - Type "decode" or "2" to decrypt
"""
ceasar(groups=groups, menu=menu)
