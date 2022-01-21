from random import randint
from functions import *

test_arrays = [[randint(1, 1000) for _ in range(10**i)] for i in range(7)]

plot_arrays = [[randint(1, 1000) for _ in range(2*i)] for i in range(500)]

algos = [sorted, 
         bubble_sort, 
         selection_sort, 
         insertion_sort, 
         comb_sort, 
         shaker_sort, 
         gnome_sort, 
         quick_sort, 
         counting_sort,
         merge_sort, 
         shell_sort, 
         bucket_sort, 
         timsort
]
