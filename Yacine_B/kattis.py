n, t = map(int, input().split())
potions = []

ok = True

for i in range(n):
    potions = list(map(lambda x: x - t, potions))
    potions.append(int(input()))

    if i == n - 1 and 0 in potions:
        ok = False
        break

print("YES") if ok else print("NO")
