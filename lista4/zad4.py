import ctypes

class Empty(Exception):
    """Class made for handling exceptions"""
    pass

class BinaryTree():
    """Class representing a binary tree data structure using array implementation
    root (optional) - the root of an object of this class"""

    def __init__(self, root=None):
        if root == None:
            self._n = 0
        else:
            self._n = 1
        self._h = 0
        self._tree = self._make_array(2 ** (self._h+1) - 1)
        self._tree[0] = root

    def __str__(self):
        result = ''
        levels = [0] + [2 ** (i+1) - 1 for i in range(self._h)]
        for i in range(2 ** (self._h+1) - 1):
            if len(levels) > 1:
                if i == levels[1]:
                     result += '\n'
                     levels.pop(0)
            try:
                self._valid(i, '')
            except Empty:
                result += '( )'
            else:
                result += f'({self._tree[i]})'
        return result

    def __len__(self):
        return self._n

    def height(self, p):
        """returns number of layers the tree has"""
        return self.segment(p)._h

    def is_empty(self):
        """checks if a tree is empty"""
        return not self._exist(0)

    def is_leaf(self, p):
        """checks if node with number p doesn't have children"""
        self._valid(p, 'node')
        left = False
        right = False
        try:
            self._valid(p * 2 + 1, '')
        except Empty:
            left = True
        try:
            self._valid(p * 2 + 2, '')
        except Empty:
            right = True
        if left and right:
            return True
        else:
            return False

    def depth(self, p):
        """returns on which layer the node numbered p is"""
        self._valid(p, 'node')
        for i in range(self._h+1):
            if 2 ** i - 1 <= p < 2 ** (i + 1) - 1:
                return i

    def __getitem__(self, p):
        self._valid(p, 'node')
        return self._tree[p]

    def set(self, p, value):
        """sets a value of a node numbered p"""
        self._valid((p - 1) // 2, 'parent')
        if 2 ** (self._h + 1) - 1 <= p < 2 ** (self._h + 2) - 1:
            self._h += 1
            self._resize(2 ** (self._h + 1) - 1)
        if not self._exist(p):
            self._n += 1
        self._tree[p] = value

    def add(self, p, value):
        """adds a value to a node numbered p"""
        if self._exist(p):
            raise Empty("Can't overwrite an exiting node")
        else:
            self.set(p, value)

    def set_root(self, value):
        if not self._exist(0):
            self._n += 1
        self._tree[0] = value

    def set_left(self, value, parent):
        """sets value of left children of node numbered parent"""
        self._valid(parent, 'parent')
        if 2 ** self._h - 1 <= parent < 2 ** (self._h + 1) - 1:
            self._h += 1
            self._resize(2 ** (self._h + 1) - 1)
        if not self._exist(parent * 2 + 1):
            self._n += 1
        self._tree[parent * 2 + 1] = value

    def set_right(self, value, parent):
        """sets value of right children of node numbered parent"""
        self._valid(parent, 'parent')
        if 2 ** self._h - 1 <= parent < 2 ** (self._h + 1) - 1:
            self._h += 1
            self._resize(2 ** (self._h + 1) - 1)
        if not self._exist(parent * 2 + 2):
            self._n += 1
        self._tree[parent * 2 + 2] = value

    def get_left_child(self, parent):
        """returns value of left children of node numbered parent"""
        self._valid(parent, 'parent')
        self._valid(parent * 2 + 1, 'left child')
        return self._tree[parent * 2 + 1]

    def get_right_child(self, parent):
        """returns value of right children of node numbered parent"""
        self._valid(parent, 'parent')
        self._valid(parent * 2 + 2, 'left child')
        return self._tree[parent * 2 + 2]

    def has_left_child(self, parent):
        """returns a bool of the parent numbered parent having left child"""
        return self._exist(parent * 2 + 1)

    def has_right_child(self, parent):
        """returns a bool of the parent numbered parent having right child"""
        return self._exist(parent * 2 + 2)

    def get_left_child_pos(self, parent):
        """returns an index of left child of node numbered parent"""
        return parent * 2 + 1

    def get_right_child_pos(self, parent):
        """returns an index of right child of node numbered parent"""
        return parent * 2 + 2

    def get_parent(self, child):
        """returns parent value of node numbered child"""
        self._valid(child, 'child')
        if child == 0:
            raise Empty("Root have no parents")
        return self._tree[(child - 1) // 2]

    def get_children(self, p):
        """returns values of both children of node numbered p"""
        self._valid(p, 'node')
        result = []
        left = True
        right = True
        try:
            self._valid(2 * p + 1, '')
        except Empty:
            left = False
        try:
            self._valid(2 * p + 2, '')
        except Empty:
            right = False
        if left:
            result.append(2 * p + 1)
        if right:
            result.append(2 * p + 2)
        return [self._tree[result[0]], self._tree[result[1]]]

    def pop(self, p):
        """removes a single node numbered p that must be a leaf"""
        self._valid(p, 'node')
        if not self.is_leaf(p):
            raise Empty("Can't remove a node with children")
        else:
            value = self._tree[p]
            self._tree[p] = None
            self._n -= 1
            if self._h == 0:
                return value
            for i in range(2 ** self._h - 1, 2 ** (self._h+1) - 1):
                try:
                    self._valid(i, '')
                except Empty:
                    continue
                else:
                    return value
            self._h -= 1
            self._resize(2 ** (self._h + 1) - 1)

    def remove(self, p):
        """removes a whole branch of a tree started form node numbered p"""
        left = True
        right = True
        if self.is_leaf(p):
            self.pop(p)
            return
        try:
            self._valid(2 * p + 1, '')
        except Empty:
            left = False
        try:
            self._valid(2 * p + 2, '')
        except Empty:
            right = False
        if left:
            self.remove(2 * p + 1)
        if right:
            self.remove(2 * p + 2)
        self.pop(p)

    def combine(self, other, p, g=0):
        """combines to BinaryTree objects on node numbered p"""
        self.set(p, other[g])
        for i in other._children(g):
            if i % 2 == 1:
                c = 1
            else:
                c = 2
            self.combine(other, 2 * p + c, i)
        return

    def segment(self, p):
        """returns a branch of a BinaryTree object as a new BinaryTree object"""
        self._valid(p, 'node')
        new = BinaryTree(self._tree[p])
        if self.is_leaf(p):
            return new
        for i in self._children(p):
            if i % 2 == 1:
                c = 1
            else:
                c = 2
            new.combine(self.segment(2 * p + c), c)
        return new

    def preorder_list(self, p=0):
        """returns a list of nodes in preorder order"""
        result = []
        result.append(self._tree[p])
        if self.is_leaf(p):
            return result
        for i in self._children(p):
            result += self.preorder_list(i)
        return result

    def preorder(self):
        """returns a string of nodes in preorder order"""
        result = ''
        ar = self.preorder_list()
        for i in ar:
            result += f'{i}, '
        return result[:len(result)-2]

    def inorder_list(self, p=0):
        """returns a list of nodes in inorder order"""
        result = []
        if self.is_leaf(p):
            result.append(self._tree[p])
            return result
        if len(self._children(p)) == 2:
            result += self.inorder_list(self._children(p)[0])
            result.append(self._tree[p])
            result += self.inorder_list(self._children(p)[1])
        elif self._children(p)[0] % 2 == 1:
            result += self.inorder_list(self._children(p)[0])
            result.append(self._tree[p])
        else:
            result.append(self._tree[p])
            result += self.inorder_list(self._children(p)[0])
        return result

    def inorder(self):
        """returns a string of nodes in preorder order"""
        result = ''
        ar = self.inorder_list()
        for i in ar:
            result += f'{i}, '
        return result[:len(result) - 2]

    def _children(self, p):
        self._valid(p, 'node')
        result = []
        left = True
        right = True
        try:
            self._valid(2 * p + 1, '')
        except Empty:
            left = False
        try:
            self._valid(2 * p + 2, '')
        except Empty:
            right = False
        if left:
            result.append(2 * p + 1)
        if right:
            result.append(2 * p + 2)
        return result

    def _valid(self, p, status):
        try:
            self._tree[p]
        except (ValueError, IndexError):
            raise Empty(f"No {status} numbered {p} found")
        if self._tree[p] == None:
            raise Empty(f"No {status} numbered {p} found")

    def _exist(self, p):
        try:
            self._valid(p, '')
        except Empty:
            return False
        return True

    def _resize(self, c):
        A = self._make_array(c)
        for i in range(2 ** (self._h+1) - 1):
            if self._exist(i):
                A[i] = self._tree[i]
        self._tree = A

    def _make_array(self, c):
        return (c * ctypes.py_object)()

if __name__ == '__main__':
    A = BinaryTree()
    print(A,'\n')
    A.set_root(0)
    print(A, '\n')
    A.set_left(1, 0)
    print(A, '\n')
    A.set_right(4, 1)
    print(A, '\n')
    A.set(2, 2)
    print(A, '\n')
    print(A.is_leaf(4), '\n')
    print(A.is_leaf(1), '\n')
    print(A.get_parent(2), '\n')
    print(A.get_children(0), '\n')
    print(A.get_left_child(0), '\n')
    print(A.get_right_child(0), '\n')
    print(A.get_left_child_pos(0), '\n')
    print(A.get_right_child_pos(0), '\n')
    print(A.has_left_child(1), '\n')
    print(A.has_right_child(1), '\n')
    print(A.height(1), '\n')
    print(A.depth(1), '\n')
    print(A.is_empty(), '\n')
    print(A.preorder(), '\n')
    print(A.inorder(), '\n')
    print(A.segment(1), '\n')
    A.remove(1)
    print(A, '\n')
    B = BinaryTree('a')
    B.set_left('b', 0)
    B.set_right('c', 0)
    print(B, '\n')
    A.combine(B, 1)
    print(A, '\n')
    A.remove(0)
    print(A, '\n')
    A.set_root('it')
    A.set_left('is', 0)
    A.set_right('working', 0)
    print(A, '\n')
    print(A.pop(2), '\n')
    print(A, '\n')
    A.add(3, 'bruh')
    print(A)
