def bubble(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/
    """
    finished = False

    while not finished:
        finished = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                finished = False

    return arr


def selection(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/visualize/
    """
    for i in range(len(arr)):
        m = arr[i]
        k = i
        for j in range(i, len(arr)):
            if arr[j] <= m:
                m, k = arr[j], j
        arr[i], arr[k] = arr[k], arr[i]

    return arr


def insertion(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/
    """
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and not (arr[j] <= arr[i] <= arr[j + 1]):
            j -= 1
        arr.insert(j + 1, arr.pop(i))

    return arr


def comb(arr):
    """
    See demo: https://en.wikipedia.org/wiki/Comb_sort
    """
    for i in range(len(arr), 0, -1):
        for j in range(len(arr)-i):
            if arr[j+i] < arr[j]:
                arr[j], arr[j+i] = arr[j+i], arr[j]

    return arr


def shaker(arr):
    """
    See demo: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
    """
    for i in range(len(arr)):
        no_switch = True
        if not i % 2:
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    no_switch = False
        else:
            for j in range(-1, -len(arr), -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    no_switch = False

        if no_switch:
            break

    return arr


if __name__ == "__main__":
    from data import test_arrays

    print(test_arrays[1])
    print(shaker(test_arrays[1]))
