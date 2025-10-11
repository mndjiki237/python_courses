# -*- coding: utf-8 -*-
"""
Jeu du Pendu Multilingue 🎭
---------------------------
Auteur : Moïse 

Ce jeu invite le joueur à deviner un mot mystère,
en anglais, français ou italien — selon la langue choisie.
Chaque erreur fait tomber un morceau du pendu... jusqu’au silence final.
"""

import random
from hangman_art import stages, logo
from hangman_word import en_word_list, fr_word_list, it_word_list


def hangman():
    """Fonction principale du jeu du pendu multilingue."""

    # --- Choix de la langue ---
    languages = ["en", "fr", "it"]
    language_text = """
    Choose your language
    Choisis ta langue
    Scegli la tua lingua
        - "en" for English
        - "fr" pour Français
        - "it" per Italiano
    """
    print(language_text)

    choice = ""
    while choice not in languages:
        choice = input("Your choice: ").lower()

    # Dictionnaire pour adapter le texte selon la langue
    messages = {
        "en": {"guess": "Guess a letter: ", "lives": "remaining lives", "lose": "Game Over 💀", "win": "You saved the word! 🎉"},
        "fr": {"guess": "Devine une lettre : ", "lives": "vies restantes", "lose": "Partie terminée 💀", "win": "Tu as sauvé le mot ! 🎉"},
        "it": {"guess": "Indovina una lettera: ", "lives": "vite rimaste", "lose": "Gioco finito 💀", "win": "Hai salvato la parola! 🎉"}
    }

    # --- Choix du mot selon la langue ---
    if choice == "en":
        word = random.choice(en_word_list)
    elif choice == "fr":
        word = random.choice(fr_word_list)
    else:
        word = random.choice(it_word_list)

    # --- Initialisation du jeu ---
    lives = len(stages) - 1  # nombre de vies disponibles
    word_list = list(word)   # liste des lettres du mot
    guessed_letters = []     # lettres déjà tentées
    display = ["_" for _ in word_list]  # mot caché

    print(logo)
    print("\nLet the game begin! / Que le jeu commence ! / Che il gioco cominci!\n")
    print(" ".join(display))

    # --- Boucle principale du jeu ---
    while lives > 0:
        print(f"\n*** {lives} {messages[choice]['lives']} ***")

        # Demande de lettre
        guess = input(messages[choice]['guess']).lower()

        # Vérifications basiques
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Entre une seule lettre valide.")
            continue
        if guess in guessed_letters:
            print(f"⚠️ Tu as déjà essayé la lettre '{guess}'.")
            continue

        guessed_letters.append(guess)

        # Si la lettre est correcte
        if guess in word_list:
            for i, letter in enumerate(word_list):
                if letter == guess:
                    display[i] = guess
            print("✅ Bonne lettre !")
        else:
            lives -= 1
            print(f"❌ Mauvaise lettre... {stages[lives]}")

        # Affiche le mot avec les lettres trouvées
        print(" ".join(display))

        # Condition de victoire
        if "_" not in display:
            print(f"\n{messages[choice]['win']}")
            print(f"✨ Le mot était : {word}")
            return

    # Si le joueur a épuisé ses vies
    print(f"\n{messages[choice]['lose']}")
    print(f"Le mot mystère était : {word}")


# --- Boucle principale pour rejouer ---
while True:
    play_text = """
    Do you want to play again?
    Veux-tu rejouer ?
    Vuoi giocare di nuovo ?
        - "yes" / "oui" / "si" to play
        - "no" to quit
    """
    print(play_text)
    response = input(": ").lower()

    if response in ["yes", "oui", "si"]:
        hangman()
    elif response == "no":
        print("Merci d’avoir joué 🌙 / Thanks for playing / Grazie per aver giocato")
        break
    else:
        print("❗ Réponse non reconnue, essaie encore.")
