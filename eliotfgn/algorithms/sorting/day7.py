n = int(input())
arr = list(map(int, input().split()))

for _ in range(int(input())):
    q = int(input())
    low, high = 0, n
    while low <= high:
        mid = int((low + high)/2)
        if q < arr[mid]:
            high = mid-1
        elif q > arr[mid]:
            low = mid+1
        else:
            print(mid+1)
            break