from zad4 import BinaryTree
import numpy as np
import ctypes

class Empty(Exception):
    pass

def valid_node(x):
    """checks if a node is storing valid information for an algebraic expression BinaryTree"""
    if not type(x) in [float, int, str]:
        raise Empty(f'Incorrect value within a tree')
    return

def number_check(x):
    """checks if a node is a number"""
    valid_node(x)
    if type(x) == str:
        return False
    else:
        return True

def diff(Tree, variable):
    """returns a BinaryTree object being a derivative of given expression written in BinaryTree object"""
    derr = BinaryTree()

    if number_check(Tree[0]):
        if not Tree.is_leaf(0):
            raise Empty("Incorrect expression")
        derr.set_root(0)

    elif Tree[0] == variable:
        if not Tree.is_leaf(0):
            raise Empty("Incorrect expression")
        derr.set_root(1)

    elif not Tree[0] in ['sin', 'cos', 'log', '+', '-', '*', '/', '^', '**']:
        if not Tree.is_leaf(0):
            raise Empty("Incorrect expression")
        derr.set_root(0)

    elif Tree[0] == '+':
        if len(Tree._children(0)) != 2:
            raise Empty("Incorrect expression")
        derr.set_root('+')
        derr.combine(diff(Tree.segment(1), variable), 1)
        derr.combine(diff(Tree.segment(2), variable), 2)

    elif Tree[0] == '-':
        if len(Tree._children(0)) != 2:
            raise Empty("Incorrect expression")
        derr.set_root('-')
        derr.combine(diff(Tree.segment(1), variable), 1)
        derr.combine(diff(Tree.segment(2), variable), 2)

    elif Tree[0] == '*':
        if len(Tree._children(0)) != 2:
            raise Empty("Incorrect expression")
        derr.set_root('+')
        derr.set_left('*', 0)
        derr.set_right('*', 0)

        derr.combine(Tree.segment(1), 3)
        derr.combine(diff(Tree.segment(2), variable), 4)

        derr.combine(Tree.segment(2), 5)
        derr.combine(diff(Tree.segment(1), variable), 6)

    elif Tree[0] == '/':
        if len(Tree._children(0)) != 2:
            raise Empty("Incorrect expression")
        if Tree[2] == 0:
            raise ZeroDivisionError
        derr.set_root('/')
        derr.set_left('-', 0)
        derr.set_right('^', 0)

        derr.set_left('*', 1)
        derr.set_right('*', 1)
        derr.combine(Tree.segment(2), 5)
        derr.set_right(2, 2)

        derr.combine(Tree.segment(2), 7)
        derr.combine(diff(Tree.segment(1), variable), 8)
        derr.combine(Tree.segment(1), 9)
        derr.combine(diff(Tree.segment(2), variable), 10)

    elif Tree[0] == '^' or Tree[0] == '**':
        if len(Tree._children(0)) != 2:
            raise Empty("Incorrect expression")
        if Tree[1] == 0 and Tree[2] == 0:
            raise Empty("Incorrect expression")
        derr.set_root('*')
        derr.set_left(Tree[0], 0)
        derr.set_right('+', 0)

        derr.combine(Tree.segment(1), 3)
        derr.set(4, '-')
        derr.set(5, '*')
        derr.set(6, '*')

        derr.combine(Tree.segment(2), 9)
        derr.set(10, 1)
        derr.combine(Tree.segment(2), 11)
        derr.combine(diff(Tree.segment(1), variable), 12)
        derr.set(13, '*')
        derr.set(14, 'log')

        derr.combine(Tree.segment(1), 27)
        derr.combine(diff(Tree.segment(2), variable), 28)
        derr.combine(Tree.segment(1), 30)

    elif Tree[0] == 'sin':
        if len(Tree._children(0)) != 1:
            raise Empty("Incorrect expression")
        p = Tree._children(0)[0]
        derr.set_root('*')
        derr.combine(diff(Tree.segment(p), variable), 1)
        derr.set(2, 'cos')
        derr.combine(Tree.segment(p), 6)

    elif Tree[0] == 'cos':
        if len(Tree._children(0)) != 1:
            raise Empty("Incorrect expression")
        p = Tree._children(0)[0]
        derr.set_root('*')
        derr.combine(diff(Tree.segment(p), variable), 1)
        derr.set(2, '-')
        derr.set_left(0, 2)
        derr.set_right('sin', 2)
        derr.combine(Tree.segment(p), 14)

    elif Tree[0] == 'log':
        if len(Tree._children(0)) != 1:
            raise Empty("Incorrect expression")
        if Tree[2] in [int, float]:
            if Tree[2] <= 0:
                raise Empty("Log takes only positive values")
        p = Tree._children(0)[0]
        derr.set_root('/')
        derr.combine(diff(Tree.segment(p), variable), 1)
        derr.combine(Tree.segment(p), 2)

    return derr

def to_expression(Tree):
    """returns a string of an expression written in BInaryTree object"""
    result = ''

    if number_check(Tree[0]):
        result = str(Tree[0])
        if Tree[0] < 0:
            result = '(' + result + ')'

    elif not Tree[0] in ['sin', 'cos', 'log', '+', '-', '*', '/', '^', '**']:
        result = Tree[0]

    elif Tree[0] in ['+', '-', '*', '/', '^', '**']:
        if type(Tree[1]) in [int, float] and type(Tree[2]) in[int, float]:
            expr = f'{Tree[1]}{Tree[0]}{Tree[2]}'
            expr.replace('^', '**')
            result = str(eval(expr))
            if eval(expr) < 0:
                result = '(' + result + ')'

        elif Tree[1] == 0:
            expr = f'{Tree[1]}{Tree[0]}5'
            expr = expr.replace('^', '**')
            result = str(eval(expr))
            result = result.replace('5', Tree[2])
            if eval(expr) < 0:
                result = '(' + result + ')'

        elif Tree[2] == 0:
            expr = f'5{Tree[0]}{Tree[2]}'
            expr = expr.replace('^', '**')
            result = str(eval(expr))
            result = result.replace('5', Tree[1])
            if eval(expr) < 0:
                result = '(' + result + ')'

        else:
            result = f'({to_expression(Tree.segment(1))}{Tree[0]}{to_expression(Tree.segment(2))})'

    elif Tree[0] in ['sin', 'cos', 'log']:
        result = f'{Tree[0]}({to_expression(Tree.segment(2))})'

    return result

def differentiate(Tree, variable):
    """returns a string being a derivative of an expression written in BinaryTree object"""
    A = diff(Tree, variable)
    return to_expression(A)

if __name__ == '__main__':
    A = BinaryTree('**')
    A.set_left('+', 0)
    A.set_right('*', 0)
    A.set(3, 'x')
    A.set(4, 'y')
    A.set(5, '69')
    A.set(6, 'x')
    print('d/dx',to_expression(A), '=')
    print(differentiate(A, 'x'), '\n')

    print('d/dy', to_expression(A), '=')
    print(differentiate(A, 'y'), '\n')

    B = BinaryTree('/')
    B.set_left('-', 0)
    B.set_right('log', 0)
    B.set(3, 'sin')
    B.set(4, 'cos')
    B.set(6, '*')
    B.set_left(4, 6)
    B.set_right('x', 6)
    B.set_right('+', 3)
    B.set_right('x', 4)
    B.set_left('x', 8)
    B.set_right('y', 8)
    print('d/dx', to_expression(B), '=')
    print(differentiate(B, 'x'))

