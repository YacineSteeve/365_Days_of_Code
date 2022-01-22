t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = input()
    maxi = ""
    p = n
    for i in range(n):
        if maxi < a:
            maxi = a
            d = i
        elif maxi == a:
            p = i - d
            break

        a = a[1:] + a[:1]
    print((d + (k-1)*p))
