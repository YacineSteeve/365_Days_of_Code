n = bin(int(input()))[2:]
print(sum(int(n[i]) * (2**i) for i in range(len(n))))
