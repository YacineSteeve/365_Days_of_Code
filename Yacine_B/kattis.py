for _ in range(int(input())):
    k, *strips = map(int, input().split())
    print(sum(strips) - k + 1)
