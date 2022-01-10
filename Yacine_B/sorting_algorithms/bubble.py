from data import *


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


if __name__ == "__main__":
    for array in test_arrays:
        print(bubble(array))
