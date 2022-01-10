import timeit
from selection import selection
from bubble import bubble
from data import test_arrays


def runtime(f):
    test_code = f'''{f}'''
    return timeit.timeit(stmt=test_code, number=1)


for array in test_arrays:
    print(f"Dataset size: {len(array)}\n"
          f"Runtime: {runtime(bubble(array))} s\n")
