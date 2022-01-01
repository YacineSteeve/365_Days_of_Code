def sort_count_swaps(a):
    swaps = 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                is_sorted = False
                c = a[i + 1]
                a[i + 1] = a[i]
                a[i] = c
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")

