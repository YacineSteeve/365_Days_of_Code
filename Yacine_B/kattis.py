n = int(input())

c, layers = 1, 0

while True:
    if c % 2:
        rem = n - c**2
        if rem >= 0:
            layers += 1
            n = rem
        else:
            break
    c += 1

print(layers)
