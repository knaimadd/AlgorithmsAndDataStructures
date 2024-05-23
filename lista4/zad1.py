from LinkedStack import LinkedStack
import time, random
import matplotlib.pyplot as plt
import numpy as np

def timer(method, n, step):
    A = LinkedStack()
    A.push(random.randint(0, 100))
    times = []
    steps = []
    try:
        eval(f'A.{method}()')
        A.push(random.randint(0, 100))
    except TypeError:
        for i in range(n):
            start = time.time()
            eval(f'A.{method}({random.randint(0, 100)})')
            end = time.time()
            times.append(end - start)
            steps.append(len(A))
            for i in range(step):
                A.push(random.randint(0, 100))
        return steps, times
    else:
        for i in range(n):
            start = time.time()
            eval(f'A.{method}()')
            end = time.time()
            times.append(end - start)
            steps.append(len(A))
            for i in range(step):
                A.push(random.randint(0, 100))
        return steps, times

if __name__ == '__main__':

    data1 = timer('push', 200, 10 ** 4)
    data2 = timer('pop', 200, 10 ** 4)
    data3 = timer('top', 200, 10 ** 4)
    data4 = timer('is_empty', 200, 10 ** 4)
    data5 = timer('__len__', 200, 10 ** 4)

    fig, axs = plt.subplots(5, sharex=True, sharey=True)

    axs[0].scatter(data1[0], data1[1])
    axs[0].set_title('push')
    axs[0].set_xlabel('Number of elements in LinkedStack')
    axs[0].set_ylabel('Time [s]')

    axs[1].scatter(data2[0], data2[1])
    axs[1].set_title('pop')
    axs[1].set_xlabel('Number of elements in LinkedStack')
    axs[1].set_ylabel('Time [s]')

    axs[2].scatter(data3[0], data3[1])
    axs[2].set_title('top')
    axs[2].set_xlabel('Number of elements in LinkedStack')
    axs[2].set_ylabel('Time [s]')

    axs[3].scatter(data4[0], data4[1])
    axs[3].set_title('is_empty')
    axs[3].set_xlabel('Number of elements in LinkedStack')
    axs[3].set_ylabel('Time [s]')

    axs[4].scatter(data5[0], data5[1])
    axs[4].set_title('len')
    axs[4].set_xlabel('Number of elements in LinkedStack')
    axs[4].set_ylabel('Time [s]')

    plt.ylim(ymin=0, ymax=0.5)

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.subplots_adjust(top=0.948,
                        bottom=0.071,
                        left=0.07,
                        right=0.955,
                        hspace=0.579,
                        wspace=0.15)

    plt.show()