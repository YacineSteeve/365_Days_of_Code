for _ in range(int(input())):
    _, n = input(), int(input())

    candies = [int(input()) for _ in range(n)]

    print("YES" if not sum(candies) % n else "NO")
