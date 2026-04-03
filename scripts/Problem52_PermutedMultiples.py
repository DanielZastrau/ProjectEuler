"""
https://projecteuler.net/problem=52
"""

def distinct(L):
    length = len(L)
    for i in range(length):
        for j in range(i + 1, length):
            if L[i] == L[j]:
                return False
    return True

def equal(A, B):
    print(A)
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

def permuted_multiples(x):
    L = [i * x for i in range(1, 7)]
    L = [ sorted([ elem for elem in str(x) ]) for x in L ]

    for i in range(len(L) - 1):
        if not equal(L[i], L[i + 1]):
            return False
    return True

def main():
    for x in range(10**5, int((10**6)/6) + 1):
        if distinct([elem for elem in str(x)]):
            if permuted_multiples(x):
                return x

print(main())