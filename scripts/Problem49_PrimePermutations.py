"""
https://projecteuler.net/problem=49
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def findArithmeticProgression(L: list[int]):

    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            diff = L[j] - L[i]

            if diff > 0 and L[j] + diff in L:
                return L[i], L[j], L[j] + diff

    return None, None, None

def main(limit: int):
    primes = commons.eratosthenes(limit=limit)
    primes = list(filter(lambda x: x >= 1000, primes))
    
    for prime in primes:
        # gets the different permutations of the base number
        l = [ int(''.join(elem)) for elem in it.permutations(str(prime)) ]
        l = list(filter(lambda x: commons.isprime(x), l))

        a, b, c = findArithmeticProgression(l)
        if a and a != 1487:
            print(''.join([str(a), str(b), str(c)]))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10_000)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)