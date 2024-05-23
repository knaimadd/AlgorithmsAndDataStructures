from Stack import Stack

class Queue:
    """Queue data structure based on two Stacks"""

    def __init__(self):
        self._n = 0
        self._A = Stack()
        self._B = Stack()
        self.str = ''

    def __len__(self):
        return self._n

    def __str__(self):
        return self.str


    def push(self, value):
        self._A.push(value)
        self._n += 1
        if self._n == 1:
            self.str += f'({value})'
        else:
            self.str += f'<-({value})'

    def peek(self):
        if self._n == 0:
            raise Exception("Peeking from an empty queue")
        if len(self._B) == 0:
            for i in range(self._n):
                self._B.push(self._A.pop())
        return self._B.peek()

    def pop(self):
        if self._n == 0:
            raise Exception("Popping from an empty queue")
        if len(self._B) == 0:
            for i in range(self._n):
                self._B.push(self._A.pop())
        if self._n == 1:
            self.str = ''
        else:
            self.str = self.str[len(str(self._B.peek()))+4:]
        self._n -= 1
        return self._B.pop()


if __name__ == '__main__':
    A = Queue()
    A.push(1)
    print(A)
    A.push(2)
    A.push(3)
    print(A)
    print(A.pop())
    print(A)
    A.pop()
    A.pop()
    print(A)
    A.push(3)
    print(A)
    A.pop()
    A.pop() #popping from an queue