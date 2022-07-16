n = int(input())

if n % 2:
    print("still running")
else:
    press = [int(input()) for _ in range(n)]

    print(sum(press[i + 1] - press[i] for i in range(0, n, 2)))
