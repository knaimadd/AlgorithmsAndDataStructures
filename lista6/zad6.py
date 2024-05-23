from Stack import Stack
import random


def part(array, low, high):
    """Function used to sort an array in comparison to a pivot which is the last element of this array
    returns an index of pivot"""
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quick_sort(array):
    """Function that sorts an array using quick sort algorithm"""
    stack = Stack()
    low = 0
    high = len(array)-1
    stack.push(low)
    stack.push(high)
    while not stack.is_empty():
        high = stack.pop()
        low = stack.pop()
        pivot = part(array, low, high)
        if pivot - 1 > low:
            stack.push(low)
            stack.push(pivot-1)
        if pivot + 1 < high:
            stack.push(pivot+1)
            stack.push(high)


def is_sorted(array):
    """Function that checks if an array is sorted"""
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True


if __name__ == '__main__':
    array = [i for i in range(10)]
    random.shuffle(array)
    print(array)
    quick_sort(array)
    print(array)
    print(f'Array is sorted: {is_sorted(array)}')
    for i in range(5):
        array = [i for i in range(1000)]
        random.shuffle(array)
        quick_sort(array)
        print(is_sorted(array))
    for i in range(5):
        array = [random.randint(0, 800) for i in range(1000)]
        quick_sort(array)
        print(is_sorted(array))
    array = [i for i in range(1000)]
    quick_sort(array)
    print(is_sorted(array))
