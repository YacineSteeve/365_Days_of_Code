import timeit
from data import test_arrays, algos


def runtime(f):
    test_code = f'''{f}'''
    return timeit.timeit(stmt=test_code, number=1)


if __name__ == "__main__":
    for array in test_arrays:
        print(f"Size: {len(array)}\n"
              f"Built-in Runtime: {runtime(algos[0](array))} s\n"
              f"Custom Runtime: {runtime(algos[-2](array))} s\n")
