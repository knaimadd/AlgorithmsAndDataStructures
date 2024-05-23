class Node:
    """Class defining a single node of Stack class"""

    def __init__(self, el, next=None):
        self.el = el
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_element(self):
        return self.el

    def set_element(self, el):
        self.el = el

class Stack:
    """Class of Stack data structure"""

    def __init__(self):
        self._n = 0  # number of elements
        self.top = Node(None)  # what is on the very top node

    def __len__(self):
        return self._n

    def __str__(self):
        ex = self.top
        result = ''
        while ex:
            result += f'({ex.get_element()})->'
            ex = ex.next
        return result[:-10]

    def is_empty(self):
        return self._n == 0

    def peek(self):
        if self._n == 0:
            raise Exception('Peeking from an empty stack')
        return self.top.get_element()

    def push(self, value):
        node = Node(value)
        node.set_next(self.top)
        self.top = node
        self._n += 1

    def pop(self):
        if self._n == 0:
            raise Exception('Popping from an empty stack')
        result = self.top.get_element()
        self.top = self.top.next
        self._n -= 1
        return result

if __name__ == '__main__':
    A = Stack()
    A.push(1)
    A.push(2)
    A.push(3)
    print(A)
    print(f'peek: {A.peek()}')
    print(A)
    print(f'pop: {A.pop()}')
    print(A)