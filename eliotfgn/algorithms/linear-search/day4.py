
n = int(input())
array = list(map(int, input().split()))
distincts = len(set(array))
s = 0

for i in range(n):
    for j in range(i+1, n+1):
        if len(set(array[i:j])) == distincts:
            s += 1

print(s)
