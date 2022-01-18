'''
source: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/easy-sum-set-problem-7e6841ca/
'''

x = int(input())
sa = set(map(int, input().split()))
y = int(input())
sc = set(map(int, input().split()))
sb = set()

for c in sc:
    for a in sa:
        b = c - a
        sb.add(c - a)

s = sb.copy()
for a in sa:
    for b in sb:
        if (a + b) not in sc:
            s.remove(b)

s = sorted(s)
for b in s:
    print(b, end=" ")
