n = int(input("\nNombre de variables du système: "))

matrix = [[0 for _ in range(n + 1)] + [False] for _ in range(n)]
# matrix =[[2, 0, 3, -5, 11, False],[-6, 0, -10, 17, -35, False],[4, 4, 7, -13, 17, False],[10, 16, 22, -38, 36, False]]


def afficher_matrice():
    """Affiche la matrice dans son état actuel"""
    for i in range(n + 2):
        if i == 0:
            print("     ", end="")
        elif i == n + 1:
            print("Cste", end="")
        else:
            print(f"X{i}", end="   ")
    print()

    k = 1
    for line in matrix:
        print(f"L{k}", end="   ")
        for x in line:
            if type(x) is not bool:
                print(x, end=" " * (5 - len([c for c in str(x)])))
        print()
        k += 1
    print()


def remplir_matrice():
    print("Veuillez entrer les coefficients du système.\n")
    for i in range(n):
        for j in range(n+1):
            if j < n:
                x = int(input(f"Ligne {i+1}, Colonne {j+1} : "))
            else:
                x = int(input(f"Constante Ligne {i+1} : "))
            matrix[i][j] = x
    print("\n Système enregistré! \n")
    afficher_matrice()


def corriger_matrice():
    """L"utilisateur indique les coefficients de la matrice"""
    finished = False

    while not finished:
        coef = str(input("Coefficient du système à modifier, au format ligne,colonne,valeur\n(Tapez N si aucun) : "))
        finished = coef == "N"
        if not finished:
            mod_row = int(coef.split(",")[0]) - 1
            mod_col = int(coef.split(",")[1]) - 1
            new_val = int(coef.split(",")[2])
            if mod_row not in range(n+1) or mod_col not in range(n+1):
                print("Ligne ou colonne introuvable! Réessayez...")
            else:
                matrix[mod_row][mod_col] = new_val
                print()
                afficher_matrice()


def triangularisation_matrice():
    for i in range(n-1):
        null = True
        line = 0
        while null:
            if line >= n or (not(matrix[line][-1]) and matrix[line][i] != 0):
                null = False
            line += 1

        ligne_pivot = line - 1 if line < n else 0
        pivot = matrix[ligne_pivot][i]

        for j in range(ligne_pivot, n):
            if not(matrix[j][n+1]) and matrix[j][i] != 0 and abs(matrix[j][i]) < abs(pivot):
                pivot = matrix[j][i]
                ligne_pivot = j

        matrix[ligne_pivot][n+1] = True

        new_line = matrix[ligne_pivot][:]
        matrix[ligne_pivot] = matrix[i][:]
        matrix[i] = new_line[:]

        for k in range(i+1, n):
            if pivot != 0 and matrix[k][i] % pivot == 0:
                facteur = matrix[k][i] // pivot
                for m in range(n+1):
                    matrix[k][m] = matrix[k][m] - facteur*matrix[i][m]
            else:
                facteur = matrix[k][i]
                for m in range(n+1):
                    matrix[k][m] = pivot * matrix[k][m] - facteur * matrix[i][m]

    print("\nSystème triangularisé: \n")
    afficher_matrice()


print()
afficher_matrice()
remplir_matrice()
corriger_matrice()
triangularisation_matrice()
