from Stack import Stack

def permute(n):
    """Technically non-recursive function that returns all permutations of set {1,2,...,n}"""
    nums = []
    for i in range(n):
        nums.append(i+1)
    perm = []
    stack = Stack()
    stack.push(-1)
    permutations = []
    while len(stack):
        i = stack.pop()
        i += 1
        while i < len(nums):
            if nums[i] not in perm:
                break
            i += 1
        else:
            if len(perm):
                perm.pop()
            continue
        stack.push(i)
        stack.push(-1)
        perm.append(nums[i])
        if len(perm) == len(nums):
            permutations.append(list(perm))
    return permutations

if __name__ == '__main__':
    A = permute(4)
    print(A, f'\n{len(A)}')