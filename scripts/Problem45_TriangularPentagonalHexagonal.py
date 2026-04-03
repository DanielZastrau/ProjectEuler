"""
https://projecteuler.net/problem=45
"""

import math

def next_tr_num(n):
    return n*(n + 1) // 2

def check_pentagonal(num):
    check1 = math.sqrt(24*num + 1)
    check2 = (check1 + 1) / 6
    if (check1%6 == 5) and (check2%1 == 0):
        return True
    
    return False

def check_hexagonal(num):
    """
    every other triangular number is a hexagonal number
    """
    return num%2 == 1

def main():
    n = 286
    while True:
        next_ = next_tr_num(n)
        if check_pentagonal(next_) and check_hexagonal(n):
            return next_
        
        n += 1

print(main())