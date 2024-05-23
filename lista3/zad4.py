import time, random
import matplotlib.pyplot as plt
import numpy as np

def append_timer(structure, n, step):
    """Function used to measure time of appending a data structure multiple times"""
    times = []
    steps = []
    for i in range(n):
        A = structure()
        r = random.randint(0, 100)
        start = time.time()
        for j in range(i*step):
            A.append(r)
        end = time.time()
        times.append(end - start)
        steps.append((i + 1) * step)
    return steps, times

def extend_timer(structure, n, step):
    """Function used to measure time of extending a data structure with growing list length"""
    times = []
    steps = []
    for i in range(n):
        A = structure()
        ex = np.random.randint(0, 100, i*step)
        start = time.time()
        A.extend(ex)
        end = time.time()
        times.append(end - start)
        steps.append((i + 1) * step)
    return steps, times


if __name__ == '__main__':

    data1 = append_timer(list, 50, 3*10**5)
    data2 = extend_timer(list, 50, 3*10**5)

    plt.scatter(data1[0], data1[1], label='append', s=18)
    plt.scatter(data2[0], data2[1], label='extend', s=18)
    plt.xlabel('Number of elements to add to list', fontsize=15)
    plt.ylabel('Time [s]', fontsize=15)
    plt.title('Comparing append and extend complexity', fontsize=15)

    plt.legend()
    plt.show()