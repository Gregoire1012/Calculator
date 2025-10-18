def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro !"
    return a / b


while True:
    print("\n===== CALCULATRICE PYTHON =====")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Choisissez une opération (1-5) : ")

    if choix == "5":
        print("Merci d'avoir utilisé la calculatrice !")
        break

    if choix not in ["1", "2", "3", "4"]:
        print("⚠️ Choix invalide, réessayez.")
        continue

    try:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("⚠️ Erreur : entrez uniquement des nombres.")
        continue

    if choix == "1":
        print("Résultat =", addition(num1, num2))
    elif choix == "2":
        print("Résultat =", soustraction(num1, num2))
    elif choix == "3":
        print("Résultat =", multiplication(num1, num2))
    elif choix == "4":
        print("Résultat =", division(num1, num2))
