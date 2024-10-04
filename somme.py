# Fonction pour faire la somme de deux nombres
def somme(a, b):
    return a + b

# Demande de l'utilisateur
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Affichage du résultat
resultat = somme(nombre1, nombre2)
print(f"La somme de {nombre1} et {nombre2} est {resultat}.")
