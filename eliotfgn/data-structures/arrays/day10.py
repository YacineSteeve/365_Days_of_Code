'''
source: https://www.hackerearth.com/practice/codemonk/ monk and rotation
'''

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(k):
        arr.insert(0, arr[n-1])
        arr.pop(n)

    for e in arr:
        print(e, end=" ")