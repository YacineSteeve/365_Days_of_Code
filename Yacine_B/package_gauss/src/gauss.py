"""Solve matrix using Gaussian algorithm.
"""

def display_matrix(matrix, n):
    """Display the matrix.
    """
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


def fill_matrix(matrix, n):
    """The user insert the matrix coefficients.
    """
    print("Please enter the coefficients of the system.\n")
    for i in range(n):
        for j in range(n+1):
            ok = False
            while not ok:
                try:
                    if j < n:
                        x = int(input(f"Line {i+1}, Raw {j+1} : "))
                    else:
                        x = int(input(f"Constant Line {i+1} : "))
                except ValueError:
                    print("All coefficients must be integers! Try again...")
                else:
                    ok = True
            matrix[i][j] = x
            
    print("\nSystem registered!\n")
    display_matrix(matrix, n)
    
    return matrix


def correct_matrix(matrix, n):
    """The user have to correct input mistakes.
    """
    finished = False

    while not finished:
        coef = str(input("Coefficient to modify\n"
                         "Format: line,raw,value\n"
                         "(Enter N/n if none) : "))
        finished = (coef == "N" or coef == "n")
        if not finished:
            mod_row = int(coef.split(",")[0]) - 1
            mod_col = int(coef.split(",")[1]) - 1
            new_val = int(coef.split(",")[2])
            if mod_row not in range(n+1) or mod_col not in range(n+1):
                print("Line or raw not found! Try again...")
            else:
                matrix[mod_row][mod_col] = new_val
                print()
                display_matrix(matrix, n)
    
    print("\nFixed system\n")
    display_matrix(matrix, n)
                
    return matrix


def triangularize_matrix(matrix, n):
    """Triangularize the matrix using Gaussian algorithm.
    """
    for i in range(n-1):
        null = True
        line = 0
        while null:
            if line >= n or (not(matrix[line][-1]) and matrix[line][i] != 0):
                null = False
            line += 1

        line_pivot = line - 1 if line < n else 0
        pivot = matrix[line_pivot][i]

        for j in range(line_pivot, n):
            if not(matrix[j][n+1]) and matrix[j][i] != 0 and abs(matrix[j][i]) < abs(pivot):
                pivot = matrix[j][i]
                line_pivot = j

        matrix[line_pivot][n+1] = True

        new_line = matrix[line_pivot][:]
        matrix[line_pivot] = matrix[i][:]
        matrix[i] = new_line[:]

        for k in range(i+1, n):
            if pivot != 0 and matrix[k][i] % pivot == 0:
                factor = matrix[k][i] // pivot
                for m in range(n+1):
                    matrix[k][m] = matrix[k][m] - factor*matrix[i][m]
            else:
                factor = matrix[k][i]
                for m in range(n+1):
                    matrix[k][m] = pivot * matrix[k][m] - factor * matrix[i][m]
    matrix[-1][-1] = True
    
    return matrix
    
    
def compute_solutions(matrix, n):
    """Ascending phase of the Gaussian algorithm.
    """
    sols = [0 for _ in range(n)]
    
    for i in range(n):
        x, *remain = matrix[n-i-1][n-i-1:]
        remain = remain[:-1][::-1]
        terms = [remain[0]] + [-remain[1:][j]*sols[j] for j in range(len(remain[1:]))]
        try:
            sol = sum(terms) / x
        except ZeroDivisionError:
            print("\nUnsolvable system (no solution)! \n")
            exit()
        else:
            sols[i] = sol
        
    solved_matrix = [[0 for _ in range(n + 1)] + [False] for _ in range(n)]
    for i in range(n):
        solved_matrix[i][i] = 1
        solved_matrix[i][-2] = sols[n-i-1] if sols[n-i-1] != 0.0 else 0.0

    print("\nTriangularized system: \n")
    display_matrix(matrix, n)
    
    print("\nSolved system: \n")
    display_matrix(solved_matrix, n)
    
    print("\nSolutions: \n")
    for i in range(n):
        print(f"X{i+1} = {solved_matrix[i][-2]}")
        
    return sols[::-1]
        

if __name__ == "__main__":
    ok = False
    while not ok:
        try:
            n = abs(int(input("\nNumber of variables: ")))
        except:
            print("A positive integer expected as number of variables!")
        else:
            ok = True
    
    mt = [[0 for _ in range(n + 1)] + [False] for _ in range(n)]
    
    print()
    display_matrix(mt, n)
    mt = fill_matrix(mt, n)
    mt = correct_matrix(mt, n)
    mt = triangularize_matrix(mt, n)
    compute_solutions(mt, n)
    print()
