l, d, x = map(int, (input(), input(), input()))


def digit_sum(n):
    return sum(map(int, list(str(n))))


matches = [i for i in range(l, d+1) if digit_sum(i) == x]

print(min(matches))
print(max(matches))
