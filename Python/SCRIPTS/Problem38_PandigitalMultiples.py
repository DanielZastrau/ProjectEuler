import numpy as np
import math
import time

def is_pandigital(s):
    B = np.zeros(10)
    for digit in s:
        B[int(digit)] += 1
    if len(B[B != 1]) == 1 and B[0] == 0: return True
    else: return False

def is_pandigital_multiple(i):
    s = ''
    p = 1
    while len(s) < 9:
        s += str(i * p)
        p += 1
    if is_pandigital(s):
        return True, int(s)
    else: return False, None

maximum = 0
for integer in range(10000):
    b, v = is_pandigital_multiple(integer)
    if b:
        if v > maximum:
            maximum = v

print(maximum)