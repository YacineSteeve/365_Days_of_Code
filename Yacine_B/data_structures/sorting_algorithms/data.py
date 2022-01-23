from random import randint
from functions import *
import matplotlib.colors as mcolors




test_arrays = [[randint(1, 1000) for _ in range(10**i)] for i in range(6)]

plot_arrays = [[randint(1, 100) for _ in range(50*i)] for i in range(1, 201)]

plot_colors = ['black', 'gold', 'mediumblue'] + list(map(lambda s: s[4:], mcolors.TABLEAU_COLORS.keys()))

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
