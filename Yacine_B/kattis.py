from itertools import combinations

*heigths, h1, h2 = map(int, input().split())

t1, t2 = [], []

for t in combinations(heigths, 3):
    if sum(t) == h1:
        t1 = list(t)
    elif sum(t) == h2:
        t2 = list(t)
        
t1.sort(reverse=True)
t2.sort(reverse=True)

print(*t1, *t2, sep=' ')