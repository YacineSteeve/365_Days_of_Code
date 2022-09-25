grades = [sum(map(int, input().split())) for _ in range(5)]

print(grades.index(max(grades)) + 1, max(grades))
