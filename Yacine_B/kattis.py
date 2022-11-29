qaly = 0

for _ in range(int(input())):
    q, d = map(float, input().strip().split())
    qaly += q * d

print(qaly)