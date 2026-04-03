###############################################################################
# variable names: lower_case_with_underscores       (int, str, tuples, bools)
# -- with trailing underscore when using names of built-in functions
# variable names: Upper_first_with_underscores      (list, set, dict)
# variable names: UPPER_CASE_WITH_UNDERSCORES       (constants)
# function names: mixedCase
# class names:    CamelCase
# strings are ''
# comments in english, starting with upper case and ending with '.'

"""
https://projecteuler.net/problem=49
"""

import math
from time import sleep
from Package import prime

def perms(string):
    if len(string) == 1: return string

    if len(string) == 2: return [''.join([string[0], string[1]]), ''.join([string[1], string[0]])]

    else:
        L = []

        for i in range(len(string)):
            L.extend([ ''.join([string[i], elem]) for elem in perms(''.join([string[:i], string[i+1:]])) ])

        return L

def convToInt(L):
    return [ int(elem) for elem in L ]

def removeDuplicates(L):
    Out = []

    for elem in L:
        if elem not in Out:
            Out.append(elem)

    return Out

def sieve(Perms):
    Primes = []

    for num in Perms:
        if prime(num):
            Primes.append(num)

    return Primes

def findArithmeticProgression(L):

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            diff = L[j] - L[i]

            if diff > 0 and L[j] + diff in L:
                return L[i], L[j], L[j] + diff

    return None, None, None

def main():
    n = 1000
    
    while n < 10**4:
        
        if prime(n):
            L = convToInt(perms(str(n)))
            L = removeDuplicates(filter(lambda x: x >= 10**3, L))
            L = list(filter(lambda x: prime(x), sieve(L)))

            a, b, c = findArithmeticProgression(L)
            if a and a != 1487:
                print(''.join([str(a), str(b), str(c)]))
                sleep(0.5)

        n += 1

main()