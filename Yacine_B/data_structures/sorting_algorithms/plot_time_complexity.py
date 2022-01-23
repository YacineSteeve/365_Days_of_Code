import matplotlib.pyplot as plt
from numpy import arange
from scipy.optimize import curve_fit
from data import plot_arrays, plot_colors, algos
from test_runtime import runtime


def objective(x, a, b, c, d, e, f):
    	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e* x**5) + f

for i in range(len(algos)):
    x, y = [], []
    
    print(f"\n{algos[i].__name__} running...")

    for array in plot_arrays:
        x.append(len(array))
        y.append(runtime(algos[i](array)))
    
    # Explanations if phase 2 on https://machinelearningmastery.com/curve-fitting-with-python/
    
    popt, _ = curve_fit(objective, x, y)

    a, b, c, d, e, f = popt

    x_line = arange(min(x), max(x), 1)

    y_line = objective(x_line, a, b, c, d, e, f)

    plt.plot(x_line, y_line, color=plot_colors[i], label=algos[i].__name__)
    
    print(f"{algos[i].__name__} ploted!")

plt.legend()
plt.show()
