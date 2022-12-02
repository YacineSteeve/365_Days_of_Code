n_parts, days = map(int, input().split())
repl = []
every = False

for i in range(days):
    part = input()
    if part not in repl:
        repl.append(part)
    if len(repl) == n_parts and not every:
        print(i+1)
        every = True

if len(repl) < n_parts:
    print("paradox avoided")
