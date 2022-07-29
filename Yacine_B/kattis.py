c = float(input())

cost = 0

for _ in range(int(input())):
    l, w = map(float, input().split())
    cost += l * w * c

print(f'{cost:.8f}')
