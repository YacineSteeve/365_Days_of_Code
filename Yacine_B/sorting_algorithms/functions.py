def bubble(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/tutorial/
    """
    finished = False
    turn = 0

    while not finished:
        finished = True
        for i in range(1, len(arr)-turn):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                finished = False
        turn += 1

    return arr


def selection(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/tutorial/
    """
    for i in range(len(arr)):
        k = i
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[k]:
                k = j
        if k != i:
            arr[i], arr[k] = arr[k], arr[i]

    return arr


def insertion(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/
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
    gap = len(arr)
    no_permut = False

    while not no_permut or gap > 1:
        gap = int(gap//1.3)
        no_permut = True
        if gap < 1:
            gap = 1
        for j in range(len(arr)-gap):
            if arr[j+gap] < arr[j]:
                arr[j], arr[j+gap] = arr[j+gap], arr[j]
                no_permut = False

    return arr


def shaker(arr):
    """
    See demo: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
    """
    for i in range(len(arr)):
        no_permut = True
        if not i % 2:
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    no_permut = False
        else:
            for j in range(-1, -len(arr), -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    no_permut = False

        if no_permut:
            break

    return arr


def gnome(arr):
    """
    See demo: https://en.wikipedia.org/wiki/Gnome_sort
    """
    pos = 1
    while pos < len(arr):
        if arr[pos] >= arr[pos-1]:
            pos += 1
        else:
            i = pos
            while i > 0 and arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                i -= 1

    return arr


def quick(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/tutorial/
    """
    if arr:
        pivot = arr[-1]
        smaller = [x for x in arr if x < pivot]
        bigger = [x for x in arr[:-1] if x >= pivot]

        return quick(smaller) + [pivot] + quick(bigger)
    else:
        return []


def counting(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/counting-sort/tutorial/
    """
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]

    frequencies = {n: 0 for n in range(1, max+1)}

    for i in range(len(arr)):
        frequencies[arr[i]] += 1

    arr = []

    for elem in frequencies.items():
        arr.extend([elem[0] for _ in range(elem[1])])

    return arr


def merge(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/
    """
    def merging(left, right):
        """
        To merge two arrays.
        """
        if not left:
            return right
        elif not right:
            return left

        res = []

        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            elif right[0] < left[0]:
                res.append(right.pop(0))

        if right:
            res.extend(right)
        elif left:
            res.extend(left)

        return res

    def cut(a):
        """
        Dividing the array recursively and merging each stage.
        """
        if len(a) <= 1:
            return a

        left = a[:len(a)//2]
        right = a[len(a)//2:]
        left = cut(left)
        right = cut(right)

        return merging(left, right)

    return cut(arr)


if __name__ == "__main__":
    from data import test_arrays

    print(test_arrays[1])
    print(merge(test_arrays[1]))
