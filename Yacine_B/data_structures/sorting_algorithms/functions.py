from collections import deque


def bubble_sort(arr):
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


def selection_sort(arr):
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


def insertion_sort(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/tutorial/
    """
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            j -= 1
        arr.insert(j + 1, arr.pop(i))

    return arr


def comb_sort(arr):
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


def shaker_sort(arr):
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


def gnome_sort(arr):
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


def quick_sort(arr):
    """
    See demo: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/tutorial/
    """
    if arr:
        pivot = arr[-1]
        smaller = [x for x in arr if x < pivot]
        bigger = [x for x in arr[:-1] if x >= pivot]

        return quick_sort(smaller) + [pivot] + quick_sort(bigger)
    else:
        return []


def counting_sort(arr):
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


def merge_sort(arr):
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
            if left[0] <= right[0]:
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

        return merging(cut(left), cut(right))

    return cut(arr)


def shell_sort(arr):
    """
    See demo: https://en.wikipedia.org/wiki/Shellsort
    """

    # Computing the appropriate gaps to use based on optimal ones and a growth factor.
    opt_gaps = [1, 4, 10, 23, 57, 132, 301, 701]

    if len(arr) > 701:
        new_gap = round(opt_gaps[-1] * 2.3)

        while new_gap < len(arr):
            opt_gaps.append(new_gap)
            new_gap = round(opt_gaps[-1] * 2.3)
    else:
        opt_gaps = list(filter(lambda x: x < len(arr), opt_gaps))

    # Sorting
    for gap in opt_gaps[::-1]:
        for i in range(gap):
            # Insertion sort
            for j in range(i+gap, len(arr), gap):
                k = j
                while k-gap >= i and arr[k-gap] > arr[j]:
                    k -= gap
                arr.insert(k, arr.pop(j))

    return arr


def bucket_sort(arr, a=None, b=None):
    """
    See demo: https://en.wikipedia.org/wiki/Bucket_sort
    """
    
    # For merging the sorted buckets.
    def merging(l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

        merged = []

        while l1 and l2:
            if l1[0] <= l2[0]:
                merged.append(l1.pop(0))
            elif l2[0] < l1[0]:
                merged.append(l2.pop(0))

        if l1:
            merged.extend(l1)
        elif l2:
            merged.extend(l2)

        return merged

    # Auxiliary sorting algorithm.
    def insertion(t):
        for i in range(1, len(t)):
            j = i - 1
            while j >= 0 and t[j] > t[i]:
                j -= 1
            t.insert(j + 1, t.pop(i))

        return t

    # The array numbers range [a, b[.
    if a is None:
        a = 1
    if b is None:
        b = 1001

    n = len(arr)
    packs = [[] for _ in range(n)]

    # Creating the buckets.
    for x in arr:
        packs[n * (x - a) // (b - a)].append(x)

    # Sorting each bucket.
    for k in range(n):
        packs[k] = insertion(packs[k])

    # Merging the buckets
    res = packs[0]

    while packs:
        res = merging(res, packs.pop(0))

    return res


def timsort(arr):
    """
    See demo:
    """
    def merging(l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        
        merged = []
        
        while l1 and l2:
            if l1[0] <= l2[0]:
                merged.append(l1.pop(0))
            elif l2[0] < l1[0]:
                merged.append(l2.pop(0))
        
        if l1:
            merged.extend(l1)
        elif l2:
            merged.extend(l2)
            
        return merged
    
    def insertion(a):
        for i in range(1, len(a)):
            j = i - 1
            while j >= 0 and a[j] > a[i]:
                j -= 1
            a.insert(j+1, a.pop(i))
    
        return a
    
    n = len(arr)
    MIN = 32
    # Computing the value of minrun.
    r = 0
    while n >= MIN:
        r |= n & 1
        n >>= 1
        
    minrun =  n + r
    
    # Sorting each subarray of size minrun.
    for i in range(0, len(arr) - minrun + 1, minrun):
        arr[i:i+minrun] = insertion(arr[i:i+minrun])
    
    # Merging the sorted subarrays.
    size = minrun
    
    #for i in range()


if __name__ == "__main__":
    from data import test_arrays

    print(test_arrays[1])
    print(timsort(test_arrays[1]))
    