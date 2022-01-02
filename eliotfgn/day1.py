"""
source: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/sum-as-per-frequency-88b00c1f/
"""

size = int(input())
numbers = list(map(int, input().split()))
t = int(input())

for _ in range(t):
    l, r = [int(i) for i in input().split()]
    occ = {}
    for i in range(size):
        if numbers[i] in occ:
            occ[numbers[i]] += 1
        else:
            occ[numbers[i]] = 1
    s = 0
    for n in occ:
        if l <= occ[n] <= r:
            s += n*occ[n]
    print(s)
