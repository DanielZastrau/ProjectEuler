import math
import numpy as np

def is_prime(n):
    if n == 0: return False
    elif n == 1: return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0: return False
    return True

def primes_below(n):
    P = []
    for i in range(n):
        if is_prime(i): P.append(i)
    return P

def rotations_of(n):
    R = []
    s = str(n)
    l = len(s)
    for i in range(l):
        r = s[i:] + s[:i]
        R.append(int(r))
    return R

def rotations(L):
    return [rotations_of(n) for n in L]

def circular_primes_below(n):
    R = rotations(primes_below(n))
    c = 0
    for circle in R:
        c += 1
        for number in circle:
            if not is_prime(number): 
                c -= 1
                break
    return c
        
print(circular_primes_below(10 ** 6))