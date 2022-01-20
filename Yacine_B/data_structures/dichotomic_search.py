def dicho(x, arr) -> bool:
    """
    Search x in the array arr using dichotomy search algorithm.
    Return True if found, False if not.
    /!\ arr must be sorted in ascending order.
    """
    n = len(arr)
    arr = sorted(arr)
    if n == 1:
        return x == arr[0]
    else:
        if x == arr[n//2]:
            return True
        elif x < arr[n//2]:
            return dicho(x, arr[:n//2])
        elif x > arr[n//2]:
            return dicho(x, arr[n//2:])


if __name__ == "__main__":

    test_arr = [3, 6, 8, 11, 11, 12, 17, 17, 22, 22, 25, 26, 29, 36,
                38, 43, 54, 55, 56, 64, 67, 81, 87, 94, 96, 97, 100]

    print(dicho(64, test_arr))
    print(dicho(9, test_arr))
    print(dicho(22.5, test_arr))
