m = int(input())
w = 0
d = {"G": [0, 0], "M": [0, 0]}

for _ in range(m):
    p, c = input().split(":")
    for w in c.split():
        if w.isdigit():
            d[p][0] = w
            d[p][1] += 1

g_weight = d["G"][1] * 2
m_weight = d["M"][1]
if g_weight > m_weight and (d["G"][0] == 19 or d["G"][0] == 20):
    print("Date")
else:
    print("No Date")