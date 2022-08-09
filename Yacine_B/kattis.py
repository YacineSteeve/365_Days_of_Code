for _ in range(int(input())):
    k, n = map(int, input().split())
    print(k, sum(1 + i for i in range(1, n + 1)))
