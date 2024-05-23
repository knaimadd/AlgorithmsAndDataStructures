from zad10 import Queue

class Stack2:
    """Stack data structure based on a Queue"""

    def __init__(self):
        self._A = Queue()

    def __len__(self):
        return len(self._A)

    def __str__(self):
        return str(self._A).replace('->', '<-')

    def push(self, value):
        l = len(self)
        self._A.push(value)
        for i in range(l):
            self._A.push(self._A.pop())

    def peek(self):
        return self._A.peek()

    def pop(self):
        return self._A.pop()

if __name__ == '__main__':
    A = Stack2()
    A.push(1)
    A.push(2)
    A.push(3)
    print(A)
    print(f'peek: {A.peek()}')
    print(A)
    print(f'pop: {A.pop()}')
    print(A)
    A.pop()
    A.pop()
    A.push(5)
    print(f'pushing to emptied stock: {A}')
    A.pop()
    A.pop() #wyciąganie z pustego stosu