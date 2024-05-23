def array_sum(array):
    """Function that sums all elements of nxn array given as list of list"""
    result = 0
    if type(array) != list:
        raise Exception("Incorrect array form")
    n = len(array)
    for li in array:
        if type(li) != list:
            raise Exception("Incorrect array form")
        if len(li) != n:
            raise Exception("Incorrect array form")
        for i in li:
            result += i
    return result

if __name__ == '__main__':
    A = [[1, 2], [3, 4]]
    print(array_sum(A))
    B = [[1, 2, 3], [5, 6], [7, 8, 9]]
    C = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    array_sum(B) #zła forma macierzy
    #array_sum(C) #również