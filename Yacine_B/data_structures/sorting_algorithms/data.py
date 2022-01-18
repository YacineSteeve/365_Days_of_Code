from random import randint
from functions import *

test_arrays = [[randint(1, 1000) for _ in range(10**i)] for i in range(5)]

plot_arrays = [[randint(1, 1000) for _ in range(2*i)] for i in range(500)]

algos = [bubble, selection, insertion, comb, shaker, gnome, quick, counting,
         merge, shell]
