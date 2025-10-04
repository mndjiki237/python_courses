"""
etape

    creer une liste de lettre miniscule et majuscule
    creer un liste de nombre de 0 a 9
    creer une liste de symbole
    afficher le nom du programme
    demander a l'utilisateur le nombre de lettre qu'il veut sur son mot de passe
    demander a l'utilisateur le nombre de chiffre qu'il veut sur son mot de passe
    demander a l'utilisateur le nombre de symbole qu'il veut sur son mot de passe
    reunir tous pour former un mot de passe


"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_choice = input("Quel est le nombre de lettre que vous voulez sur votre mot de passe? ")
numbers_choice = input("Quel est le nombre de chiffre que vous voulez sur votre mot de passe? ")
symbols_choice = input("Quel est le nombre de symbole que vous voulez sur votre mot de passe? ")

password = []

if letters_choice.isdigit() and numbers_choice.isdigit and symbols_choice.isdigit():
    letters_choice = int(letters_choice)
    numbers_choice = int(numbers_choice)
    symbols_choice = int(symbols_choice)
    
    password = [random.choice(letters) for i in range(letters_choice)]
    password += [random.choice(numbers) for i in range(numbers_choice)]
    password += [random.choice(symbols) for i in range(symbols_choice)]

    random.shuffle(password)

print(f"Votre mot de passe est: {"".join(password)}")