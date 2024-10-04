
#Version 4
# Demande à l'utilisateur d'entrer deux nombres
a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxieme nombre : "))

# Définition de la fonction somme
def somme(a, b):
    return a + b

# Appel de la fonction et affichage du résultat
resultat = somme(a, b)
print(f"La somme de {a} et {b} est {resultat}.")
