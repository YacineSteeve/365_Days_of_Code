def three_half(w: int, k: int, passengers=[0]) -> int:
    if w == k:
        passengers[-1] = 0

    if k == 0:
        return int(passengers[-1])
    else:
        passengers[-1] = 2 * (0.5 + passengers[-1])
        return three_half(w, k-1)


for _ in range(int(input())):
    n = int(input())
    print(three_half(n, n))
