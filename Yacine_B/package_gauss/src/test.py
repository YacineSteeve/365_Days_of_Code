from .gauss import *


"""Run this in order to see a display template for the matrix/system:

        X1   X2   X3   X4   Cste
    L1   2    0    3   -5    11   
    L2  -6    0  -10   17   -35  
    L3   4    4    7  -13    17   
    L4  10   16   22  -38    36
"""


if __name__ == "__main__":
    n = 4

    mt = [[2, 0, 3, -5, 11, False],
          [-6, 0, -10, 17, -35, False],
          [4, 4, 7, -13, 17, False],
          [10, 16, 22, -38, 36, False]]

    print("\nTest matrix:\n")
    display_matrix(mt, n)
    mt = triangulate_matrix(mt, n)
    compute_solutions(mt, n)
    print()
