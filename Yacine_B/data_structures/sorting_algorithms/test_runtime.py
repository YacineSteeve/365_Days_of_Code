import timeit
from collections import Counter
from operator import itemgetter
from data import test_arrays, algos


def runtime(f):
    test_code = f'''{f}'''
    return timeit.timeit(stmt=test_code, number=10000)


def best_sorting_algo(arr):
    scores = []
    
    for _ in range(1000):
        runtimes = {func: runtime(func(arr)) for func in algos}
        best_time = min(runtimes.values())
        
        scores.append([f for f in runtimes if runtimes[f] == best_time][0])

    scores = Counter(scores)

    return sorted([(f, scores[f]//10) for f in scores], key=itemgetter(1), reverse=True)


if __name__ == "__main__":
    
    print("\nBest algorithm(s) for your array in average:\n")
    
    array = test_arrays[1]  # Replace test_array[1] by the array to test.
    
    optims = best_sorting_algo(array)
    
    for t in optims:
        print(f"¤ {t[0]} : {t[1]}%")
    
    print()
