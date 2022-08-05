norm = [1, 1, 2, 2, 2, 8]

for i, n in enumerate(list(map(int, input().split()))):
    print(norm[i] - n, end=' ')
