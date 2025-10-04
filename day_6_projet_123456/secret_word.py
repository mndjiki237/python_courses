import random

computer_number = random.randint(1, 101)
count = 0
lives = 5
print("Le jeu mystère!")
is_game_end = False

while lives > 0:
    print(f"Il te reste {lives} essaie{'s' if lives > 1 else ''}")
    choice = input("Devine le nombre: ")
    if not choice.isdigit():
        print("Votre saisi est incorect, veuillez saisir un nombre compris entre 1 et 100")
        continue
    choice = int(choice)
    if choice == computer_number:
        
        is_game_end = True
        break
    elif choice < computer_number:
        print(f"Le nombre mystère est plus grand que {choice}")

    else:
        print(f"Le nombre mystère est plus petit que {choice}")
    
    lives -= 1
    count += 1
    
if is_game_end:
    print(f"Le nombre mystere est: {choice}")
    print(f"Bravo! tu as trouvé le nombre mystere en {count} essaie{'s' if lives > 1 else ''}.")
else:
    print(f"Dommage! le nombre mystere etais: {computer_number}")
print("Fin du jeu.")
