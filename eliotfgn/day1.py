from collections import Counter
import sys

sys.stdin = open("input.in", 'r')
size = int(input())
numbers = list(map(int, input().split()))
occ = dict(Counter(numbers))
occ = sorted(occ.items(), key=lambda x: x[1], reverse=True)
occ = dict(occ)
print(occ)
t = int(input())

for k in range(t):
    left, right = [int(i) for i in input().split()]
    s = 0
    for n in occ:
        if occ[n] >= left:
            if occ[n] <= right:
                s += n*occ[n]
        else:
            break
    print(s)
