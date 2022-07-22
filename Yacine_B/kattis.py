ps = [input() for _ in range(int(input()))]

print(sum(int(p[:-1]) ** int(p[-1]) for p in ps))
