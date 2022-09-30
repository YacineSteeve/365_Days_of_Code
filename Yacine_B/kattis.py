new = True  # Nouvelle série de logs dès au départ
l = 0  # longueur totale initiale nulle
dots = 0  # nombre de points à placer à la fin

while True:
    try:
        curr = input().strip()  # Current line
    except:  # Donc enf of file
        break

    if new:
        l = len(curr)  # Longueur de la ligne (reste la même pour toute la série de logs)

    if curr == '':
        new = True
        dots = 0  # Réinitialise le nombre de points finaux
        print()  # Ligne vide
        continue  # Jump directement vers la prochaine ligne
    else:
        new = False

    # Ex:
    # ...........*........
    # ....*.....*.........
    # .........*..*...*...
    # Qui devient
    # ...................*
    # .................**.
    # ..............***...

    asts = curr.count('*')

    print('.' * (l - (asts + dots)) + '*' * asts + '.' * dots)

    dots += asts  # Le nombre de points finaux = la somme des astérisques des lignes précédentes
