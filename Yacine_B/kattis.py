s = input()
res = []

for c in s:
    if not res or (res and c != res[-1]):
        res.append(c)

print(''.join(res))
