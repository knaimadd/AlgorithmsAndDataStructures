import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np

def bubbleSort(arr):
    n = len(arr)
    steps = []
    js = []
    for i in range(n):
        change = True
        for j in range(0, n - i - 1):
            js.append(j+1)
            if arr[j] > arr[j + 1]:
                change = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            step = arr.copy()
            steps.append(step)
        if change:
            return steps, js
    return steps, js


n = 80
x = [i+1 for i in range(n)]
arr = [i+1 for i in range(n)]
random.shuffle(arr)

steps = bubbleSort(arr)

palette = []
for i in steps[1]:
    color = ['deepskyblue' for k in range(n+1)]
    color[i] = 'crimson'
    palette.append(color)
palette[-1] = ['deepskyblue' for k in range(n+1)]

fig, ax = plt.subplots(figsize=(11, 7))
ydata = steps[0]
fig.suptitle('Bubble sort', fontsize=18)

def update(frame):
    ax.clear()
    return plt.bar(x, ydata[frame], color=palette[frame])

anim = FuncAnimation(fig, update, frames=range(len(ydata)), interval=1, blit=True)
anim.save('BubbleSort.gif', writer='Pillow', fps=40)
#plt.show()