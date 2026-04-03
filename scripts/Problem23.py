import time
import numpy as np
import math

def proper_divisor(n):
    sq = math.sqrt(n)
    sq1 = int(sq)

    L = np.zeros(2 * sq1 + 1, dtype = int)
    L[0] = 1
    a = 1

    for i in range( 2, sq1 + 1):
        if n % i == 0:
            L[a] = i
            L[a + 1] = n // i
            a = a + 2

    if sq == sq1: L[a - 1] = 0

    return L[L != 0]

def abundant_numbers_less_than(n):
    L = np.zeros( n, dtype=np.bool)

    c = 0
    for i in range(n):
        if np.sum(proper_divisor(i)) > i:
            L[i] = True
            c = c + 1

    L2 = np.zeros( c, dtype=int)
    c = 0
    for i in range(n):
        if L[i]:
            L2[c] = i
            c = c + 1

    return L2

def non_abundant_sum_less_than(n, arr_in):
    L = np.ones(n, dtype=np.bool)
    L2 = np.arange(n)
    i1 = len(arr_in)

    for i in range(i1):
        x = arr_in[i]
        for j in range(i, i1):
            y = arr_in[j]
            z = x + y
            if z >= n:
                continue
            L[z] = False

    return np.sum(L2[L])

n = 28124
print(non_abundant_sum_less_than(n, abundant_numbers_less_than(n)))