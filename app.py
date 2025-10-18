import tkinter as tk
from tkinter import messagebox

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Couleur de fond
root.configure(bg="#f0f0f0")

# Champ d'affichage
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

# Fonction pour ajouter les caractères à l'entrée
def add_to_entry(value):
    entry.insert(tk.END, value)

# Fonction pour évaluer l'expression
def calculate():
    try:
        result = eval(entry.get().replace('x', '*').replace('%', '/100'))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Expression invalide")
        entry.delete(0, tk.END)

# Fonction pour effacer l'entrée
def clear_entry():
    entry.delete(0, tk.END)

# Définition des boutons
buttons = [
    ('(', 1, 0), (')', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('x', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('7', 4, 0), ('9', 4, 1), ('8', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
]

# Création des boutons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#add8e6", command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#d3d3d3", command=clear_entry)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: add_to_entry(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Ajustement de la taille des colonnes et des lignes
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Lancement de l'application
root.mainloop()
