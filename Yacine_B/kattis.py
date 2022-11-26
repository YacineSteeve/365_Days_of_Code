parts, days = map(int, input().split())
repl = []

while days > 0 or len(repl) < parts:
    days -= 1
    part = input()
    if part not in repl:
        repl.append(part)

if len(repl) == parts:
    print(days)
elif days == 0:
    print("paradox avoided")
