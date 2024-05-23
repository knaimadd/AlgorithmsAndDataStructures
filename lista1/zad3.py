from zad2 import timer1
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

data = timer1(sorted, 20, 4*10**5)

xs = np.linspace(1, 90*10**5, 100)
def func(x, a, b):
    """O(nlog(n))"""
    return a * x * np.log(x) + b

popt, pcov = curve_fit(func, data[0], data[1])
print(f'sorted: {popt[0]}*x*ln(x)+{popt[1]}')

plt.scatter(data[0], data[1], color='red', label='Data')
plt.plot(xs, func(xs, *popt), label='Model')
plt.xlabel('Number of elements in array', fontsize=15)
plt.ylabel('Time [s]', fontsize=15)
plt.title('sorted', fontsize=15)


plt.legend()
plt.show()