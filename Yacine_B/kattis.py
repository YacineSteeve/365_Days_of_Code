def swap(x):
    return int(''.join(reversed(list(x))))


a, b = map(swap, input().split())

print(max(a, b))
