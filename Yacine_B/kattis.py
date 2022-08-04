_ = input()
print(len(list(filter(lambda x: x < 0, map(int, input().split())))))
