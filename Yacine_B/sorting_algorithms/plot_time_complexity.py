import matplotlib.pyplot as plt
from data import plot_arrays, algos
from test_runtime import runtime


for func in algos:
    x_y = [(len(array), runtime(func(array))) for array in plot_arrays]
    x, y = [t[0] for t in x_y], [t[1] for t in x_y]
    plt.plot(x, y)


plt.show()
