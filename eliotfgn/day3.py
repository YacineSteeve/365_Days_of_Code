'''
source: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/holiday-season-ab957deb/
'''

n = int(input())
x = input()
s = 0

for a in range(n-3):
    for c in range(a+2, n-1):
        if x[a] == x[c]:
            for b in range(a+1, c):
                print(x[b])
                for d in range(c+1, n):
                    print(x[b], x[d])
                    if x[b] == x[d]:
                        s += 1

print(s)