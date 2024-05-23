def palindrome(S):  #nazwa funkcji z małej litery
    """Check if given string S is a palindrome"""
    if len(S) <= 1:  #bardziej zwięzły warunek
        return True
    else:
        if palindrome(S[1:-1]):
            return S[0] == S[-1]
    return False

if __name__ == '__main__':
    print(palindrome('atokanapapanakota'), palindrome('kajak'), palindrome('palindrom'))