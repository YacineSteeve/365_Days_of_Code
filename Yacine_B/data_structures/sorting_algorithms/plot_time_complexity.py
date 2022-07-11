import matplotlib.pyplot as plt
from numpy import arange
from scipy.optimize import curve_fit
from data import plot_arrays, plot_colors, algos
from test_runtime import runtime


def objective(value, params):
    a, b, c, d, e = params
    return (a * value) + (b * value ** 2) + (c * value ** 3) + (d * value ** 4) + e


for i in range(len(algos)):
    x, y = [], []

    print(f"\n{algos[i].__name__} running...")

    for array in plot_arrays:
        x.append(len(array))
        y.append(runtime(algos[i](array)))

    # Explanations if phase 2 on https://machinelearningmastery.com/curve-fitting-with-python/

    popt, _ = curve_fit(objective, x, y)

    x_line = arange(min(x), max(x), 1)

    y_line = objective(x_line, popt)

    plt.plot(x_line, y_line, color=plot_colors[i], label=algos[i].__name__)

    print(f"{algos[i].__name__} plotted!")

plt.legend()
plt.show()
