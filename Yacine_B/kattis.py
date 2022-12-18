values = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

cpr = list(input().strip())
cpr.remove('-')

test = sum(v * int(n) for v, n in zip(values, cpr))

if test % 11:
    print(0)
else:
    print(1)
