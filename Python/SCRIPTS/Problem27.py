import numpy as np 
import math


def is_prime(n):
    if n <= 0: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: return False

    return True

def primes_upto(n):
    B = []
    for i in range(2, n):
        if is_prime(i): B.append(i)
        
    return B

def pairs(A, B):
    C = []
    for e in A:
        for p in B:
            C.append((e,p))

    return C

def quadratic(t, x):
    return x**2 + t[0]*x + t[1]

def largest_product(C):
    mn = 0
    mt = None
    for t in C:
        x = 0
        while is_prime(quadratic(t, x)):
            x += 1
        if x > mn:
            mn = x
            mt = t

    return mt[0] * mt[1]

n = 1000
A = [x for x in range (-n + 1,n)]
B = primes_upto(n)
C = pairs(A, B)
print(largest_product(C))