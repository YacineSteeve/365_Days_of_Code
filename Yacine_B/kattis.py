from itertools import combinations
from math import atan, pi


def arg(u, v):
    return abs(atan((v[1] - u[1]) / (v[0] - u[0])))


def solution():
    n = int(input())
    queens, rows, cols = [], [], []
    ok = True

    for _ in range(n):
        queen = input().split()
        if queen[0] in cols or queen[1] in rows:
            ok = False
        else:
            queens.append(tuple(map(int, queen)))
            cols.append(queen[0])
            rows.append(queen[1])

    if not ok:
        return False

    for q1, q2 in combinations(queens, 2):
        if arg(q1, q2) == pi / 4:
            return False

    return True


print("CORRECT") if solution() else print("INCORRECT")
