import timeit
from data import test_arrays, algos


def runtime(f):
    test_code = f'''{f}'''
    return timeit.timeit(stmt=test_code, number=1)


for array in test_arrays:
    print(f"Dataset size: {len(array)}\n"
          f"Runtime: {runtime(algos[-1](array))} s\n")
