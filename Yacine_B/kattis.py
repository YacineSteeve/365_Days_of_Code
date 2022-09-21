for _ in range(int(input())):
    t, n = map(int, input().split())
    print(t, n * (n + 1) // 2, n**2, n * (n + 1))
