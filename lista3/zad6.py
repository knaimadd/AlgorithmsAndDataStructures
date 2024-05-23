class Empty(Exception):
    pass


class Deque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._rear = len(self._data)-1

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def addFront(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % -len(self._data)
        self._data[self._front] = e
        self._size += 1

    def addRear(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._rear = (self._rear + 1) % len(self._data)
        self._data[self._rear] = e
        self._size += 1

    def removeFront(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % -len(self._data)
        self._size -= 1
        if self._size >= Deque.DEFAULT_CAPACITY and self._size == len(self._data)//2:
            self._resize(len(self._data) // 2)
        return result

    def removeRear(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        result = self._data[self._rear]
        self._data[self._rear] = None
        self._rear = (self._rear - 1) % len(self._data)
        self._size -= 1
        if self._size >= Deque.DEFAULT_CAPACITY and self._size == len(self._data)//2:
            self._resize(len(self._data) // 2)
        return result

    def peekFront(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def peekRear(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._rear]

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        for i in range(self._front, self._rear+1):
            self._data[i] = old[i]


if __name__ == '__main__':
    A = Deque()
    for i in range(4):
        A.addFront(i)
    print(A._data)
    A.removeRear()
    print(A._data)
    for i in range(7):
        A.addFront(7*i+3)
    print(A._data)
    A.addRear(69)
    print(A._data)
    A.removeFront()
    print(A._data)
    for i in range(9):
        A.removeRear()
    print(A._data)
    A.removeFront()
    print(A._data)
    A.addFront(5)
    print(A._data)
    A.removeRear()
    A.removeRear() #wyciąganie z pustej kolejki
