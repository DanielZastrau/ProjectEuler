import numpy as np
import math

def identities(n):
    A = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            A.append((i, n // i))
        
    return A

def pandigital_inner(n, identities):
    A = np.zeros(10, dtype=int)
    s = str(n)
    for digit in s:
        A[int(digit)] += 1

    for identity in identities:
        B = np.zeros(10, dtype=int)
        for i in range( len(A)):
            B[i] = A[i]

        s1 = str(identity[0])
        s2 = str(identity[1])

        for digit in s1:
            B[int(digit)] += 1
        for digit in s2:
            B[int(digit)] += 1

        if len(B[B != 1]) == 1 and B[0] == 0:
            print(n, identity)
            return True

    return False

def pandigital_outer():
    s = 0
    for n in range(10000):
        if pandigital_inner(n, identities(n)):
            s += n

    return s

print(pandigital_outer())