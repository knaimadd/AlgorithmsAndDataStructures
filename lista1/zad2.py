import time, random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

############
#Functions which time of working will be measured
############
def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]

    return total

def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]

    return total

def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]

    return total

def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex sums in A."""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1

    return count

############
#Functions that will be used, to measure the times of the above functions working
############
def timer1(func, n, step):
    """Function that measure the times of example[1-3] functions
    Arguments:
    -func -- name of function to check
    -n -- number of times it will measure and return
    -step -- step of next measure
    Returns:
    number and time coordinates"""
    l = []
    times = []
    steps = []
    for i in range(n):
        for j in range(step):
            l.append(random.randint(0, 10))
        start = time.time()
        func(l)
        end = time.time()
        times.append(end-start)
        steps.append((i+1)*step)

    return steps, times

def timer2(func, n, step):
    """The same as above but for example4"""
    l1 = []
    l2 = []
    times = []
    steps = []
    for i in range(n):
        for j in range(step):
            l1.append(random.randint(0, 10))
            l2.append(random.randint(0, 10))
        start = time.time()
        func(l1, l2)
        end = time.time()
        times.append(end-start)
        steps.append((i+1)*step)

    return steps, times

if __name__ == '__main__':
############
#Gathering the data about times
############
    data1 = timer1(example1, 20, 3*10**5)
    data2 = timer1(example2, 20, 3*10**5)
    data3 = timer1(example3, 20, 200)
    data4 = timer2(example4, 20, 15)

############
#Creating the models that should predict the times
############
    x2 = np.linspace(1, 80*10**5, num=100)
    def func1(x, a, b):
        """Linear function O(n)"""
        return a*x+b

    popt1, pcov1 = curve_fit(func1, data1[0], data1[1])
    print(f'example1: {popt1[0]}*x+{popt1[1]}')

    popt2, pcov2 = curve_fit(func1, data2[0], data2[1])
    print(f'example2: {popt2[0]}*x+{popt2[1]}')


    x3 = np.linspace(1, 5000, 100)
    def func3(x, a, b):
        """Quadratic function O(n^2)"""
        return a*x**2+b

    popt3, pcov3 = curve_fit(func3, data3[0], data3[1])
    print(f'example3: {popt3[0]}*x^2+{popt3[1]}')

    x4 = np.linspace(1, 350, 100)
    def func4(x, a, b):
        """Cubic function O(n^3)"""
        return a*x**3+b

    popt4, pcov4 = curve_fit(func4, data4[0], data4[1])
    print(f'example4: {popt4[0]}*x^3+{popt4[1]}')

############
#Checking if models are accurate
############
    S1 = []
    for i in range(79 * 10 ** 5):
        S1.append(random.randint(1, 10))

    start = time.time()
    example1(S1)
    end = time.time()
    P1 = [end - start]


    start = time.time()
    example2(S1)
    end = time.time()
    P2 = [end - start]

    S3 = []
    for i in range(4900):
        S3.append(random.randint(1, 10))

    start = time.time()
    example3(S3)
    end = time.time()
    P3 = [end - start]

    S4 = []
    W4 = []
    for i in range(340):
        S4.append(random.randint(1, 10))
        W4.append(random.randint(1, 10))

    start = time.time()
    example4(S4, W4)
    end = time.time()
    P4 = [end - start]

############
#Drawing the plots with final results
############
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].scatter(data1[0], data1[1], color='red', label='Data')
    axs[0, 0].plot(x2, func1(x2, *popt1), label='Model')
    axs[0, 0].scatter([79 * 10 ** 5], P1, color='green', label='Check')
    axs[0, 0].set_title('example1', fontsize=15)
    axs[0, 0].set_xlabel('Number of elements in array', fontsize=15)
    axs[0, 0].set_ylabel('Time [s]', fontsize=15)
    axs[0, 0].legend()

    axs[0, 1].scatter(data2[0], data2[1], color='red', label='Data')
    axs[0, 1].plot(x2, func1(x2, *popt2), label='Model')
    axs[0, 1].scatter([79 * 10 ** 5], P2, color='green', label='Check')
    axs[0, 1].set_title('example2', fontsize=15)
    axs[0, 1].set_xlabel('Number of elements in array', fontsize=15)
    axs[0, 1].set_ylabel('Time [s]', fontsize=15)
    axs[0, 1].legend()

    axs[1, 0].scatter(data3[0], data3[1], color='red', label='Data')
    axs[1, 0].plot(x3, func3(x3, *popt3), label='Model')
    axs[1, 0].scatter([4900], P3, color='green', label='Check')
    axs[1, 0].set_title('example3', fontsize=15)
    axs[1, 0].set_xlabel('Number of elements in array', fontsize=15)
    axs[1, 0].set_ylabel('Time [s]', fontsize=15)
    axs[1, 0].legend()

    axs[1, 1].scatter(data4[0], data4[1], color='red', label='Data')
    axs[1, 1].plot(x4, func4(x4, *popt4), label='Model')
    axs[1, 1].scatter([340], P4, color='green', label='Check')
    axs[1, 1].set_title('example4', fontsize=15)
    axs[1, 1].set_xlabel('Number of elements in array', fontsize=15)
    axs[1, 1].set_ylabel('Time [s]', fontsize=15)
    axs[1, 1].legend()

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.subplots_adjust(top=0.948,
    bottom=0.071,
    left=0.07,
    right=0.955,
    hspace=0.274,
    wspace=0.15)

    plt.show()