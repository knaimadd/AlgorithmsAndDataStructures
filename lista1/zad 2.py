import time, random
import matplotlib.pyplot as plt
import numpy as np

def timer(structure, n, step):
    """Function used to measure time of using pop method depending on number of index on given data structure"""
    A = structure()
    times = []
    steps = []
    A.extend(np.random.randint(1, 100, n*step))
    for i in range(n):
        start = time.time()
        A.pop(i*step-i)
        end = time.time()
        times.append(end - start)
        steps.append((i + 1) * step)
    return steps, times


if __name__ == '__main__':

    data = timer(list, 40, 10**7)

    plt.scatter(data[0], data[1], label='Data', s=16)
    plt.xlabel('Index of element popped', fontsize=15)
    plt.ylabel('Time [s]', fontsize=15)
    plt.title('Pop method complexity', fontsize=15)

    plt.legend()
    plt.show()