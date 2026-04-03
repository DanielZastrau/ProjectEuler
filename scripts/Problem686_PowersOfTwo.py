"""https://projecteuler.net/problem=686"""
"""when dealing with huge numbers and exponents its apparent to use the logarithm"""

from time import time, sleep
from math import log10, floor

if __name__=="__main__":
    t = time()

    limit = 678_910
    # limit = 45

    const1 = log10(1.23)
    const2 = log10(2)
    const3 = log10(1.24)

    j = 0
    c = 0
    while c < limit:
        j += 1
        expr1 = j * const2
        expr2 = floor(expr1)
        if const1 < expr1 - expr2 < const3:
            j += 2
            c += 1
            
    print(j)

    print(time() - t)