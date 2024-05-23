import numpy as np

def maxi(l):
    """Function that recursively finds a maximum of array
    Argument: l -- list that will be searched
    Returns: maximal value of l"""
    if len(l) == 1:
        return l[0]
    else:
        x = maxi(l[:-1])
        return x if x > l[-1] else l[-1] #poprawione, żeby były zgodne ze standardem

def mini(l):
    """Function that recursively finds a minimum of array
        Argument: l -- list that will be searched
        Returns: minimal value of l"""
    if len(l) == 1:
        return l[0]
    else:
        x = mini(l[:-1])
        return x if x < l[-1] else l[-1]

def minimaxi(l):
    """Combines the above functions and returns a dict with min and max of l"""
    return {'min': mini(l), 'max': maxi(l)}

if __name__ == '__main__':
    L = np.random.randint(-1000, 1000, size=10)
    print(f'\nMy recursive function:\nminimaxi(L): {minimaxi(L)}\n'
          f'\nStandard Library:\nmin(): {min(L)}, max(L): {max(L)}')