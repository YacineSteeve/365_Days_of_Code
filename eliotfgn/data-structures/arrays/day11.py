t = int(input())

for _ in range(t):
    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(int, input().split())))

    count = 0
    for i in range(n):
        for j in range(n):
            nb = m[i][j]
            for p in range(i, n):
                for q in range(j, n):
                    if m[p][q] < nb:
                        count += 1

    print(count)