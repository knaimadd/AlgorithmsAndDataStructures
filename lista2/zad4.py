import random

def multiply(m, n):
    """Compute the value m*n for integers m, n"""
    if m == 1:
        return n
    elif m == 0 or n == 0:  #dodatkowe warunki uwzględniające wszystkie liczby całkowite
        return 0
    elif m < 0 and n > 0:
        return multiply(n, m)
    elif m < 0 and n < 0:
        return multiply(-m, -n)
    else:
        return multiply(m-1, n) + n

if __name__ == '__main__':
    m = random.randint(-50, 50)
    n = random.randint(-50, 50)
    print(f'\nmultiply({m},{n}) = {multiply(m, n)}\n'
          f'\n{m}*{n} = {m*n}')