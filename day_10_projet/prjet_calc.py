from art_calc import logo

print(logo)

# --- Fonctions de calcul ---
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Erreur : division par zéro interdite.")
        return None
    return a / b


# --- Fonction d'entrée utilisateur ---
def ask_numbers(previous_result=None):
    """Demande à l'utilisateur les nombres et l'opérateur."""

    # Si on continue un calcul, on réutilise le résultat précédent
    if previous_result is not None:
        number_1 = previous_result
    else:
        while True:
            n1 = input("Insère ton premier nombre : ")
            if n1.replace(".", "", 1).isdigit():
                number_1 = float(n1)
                break
            print("❌ Ce n'est pas un nombre valide.")

    # Menu
    print("\nChoisis une opération :")
    print("+\n-\n*\n/")

    operators = input("👉 Opération : ")
    while operators not in ["+", "-", "*", "/"]:
        operators = input("Choisis une opération valide (+, -, *, /) : ")

    while True:
        n2 = input("Insère ton second nombre : ")
        if n2.replace(".", "", 1).isdigit():
            number_2 = float(n2)
            break
        print("❌ Ce n'est pas un nombre valide.")

    return number_1, number_2, operators


# --- Fonction principale de calcul ---
def calc():
    """Boucle principale de la calculatrice."""
    n1, n2, op = ask_numbers()

    while True:
        if op == "+":
            result = addition(n1, n2)
        elif op == "-":
            result = soustraction(n1, n2)
        elif op == "*":
            result = multiplication(n1, n2)
        elif op == "/":
            result = division(n1, n2)

        print(f"Résultat : {result}")

        # On propose à l’utilisateur de continuer
        choice = input(f"Souhaites-tu continuer avec {result}? (y/n) : ").lower()
        if choice == "y":
            n1, n2, op = ask_numbers(previous_result=result)
        else:
            print("👋 Merci d’avoir utilisé la calculatrice !")
            break


# --- Lancement du programme ---
calc()
