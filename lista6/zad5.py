from BinaryTree import BinaryTree

values = [30, 40, 24, 58, 48, 26, 11, 13]
A = BinaryTree()
for i in values:
    A.add_regular(i)
    print(A, '\n')