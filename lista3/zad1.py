import ctypes  # tablice niskopoziomowe


class DynamicArray:

    def __init__(self):
        self._n = 0  # liczba elementów
        self._capacity = 1  # rozmiar tablicy
        self._A = self._make_array(self._capacity)  # właściwa tablica

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def __str__(self):
        return f'{[self._A[i] for i in range(self._n)]}'

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in reversed(range(k, self._n)):
            self._A[i+1] = self._A[i]
        self._A[k] = value
        self._n += 1

    def remove(self, value):  #remove(self, value), usuwa pierwszą wartość o wartości value
        con = True
        for i in range(self._n):
            if self._A[i] == value:
                self._A[i] = None
                p = i
                con = False
                break
        if con:
            raise Exception(f'No element of value {value} in DynamicArray')
        for i in range(p, self._n-1):
            self._A[i] = self._A[i+1]
        self._n -= 1

    def expand(self, seq):
        for i in seq:
            self.append(i)


if __name__ == '__main__':
#testuję rzeczy które zaimplementowałem
    A = DynamicArray()
    for i in range(6):
        A.append(i)
    print(A)
    A.insert(2, 'e')
    print(A)
    A.remove('e')
    print(A)
    A.expand([6, 7, 8, 9])
    print(A)
    for i in range(10):
        A.remove(i)
    print(A)
    A.append(3)
    print(A)
    A.remove(4)