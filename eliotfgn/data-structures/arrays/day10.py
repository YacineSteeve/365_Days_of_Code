'''
source: https://www.hackerearth.com/practice/codemonk/ monk and rotation
'''

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    index = n - (k%n)
    for i in range(index, n):
        print(arr[i], end=" ")
    for i in range(index):
        print(arr[i], end=" ")
    print("")