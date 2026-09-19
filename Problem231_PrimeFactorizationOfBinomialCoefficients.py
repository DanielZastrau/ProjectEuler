"""https://projecteuler.net/problem=231
Sep 26"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op
import fractions as fr
import heapq

from typing import Iterator

import commons


def main(n: int, k: int):

    primes = commons.eratosthenes(limit=n + 1)
    print(time.time() - t)

    # Legendre's Formula
    total_sum = 0
    for p in primes:
        count = 0
        power = p
        
        # Calculate the net exponent of p in n! / (k! * (n-k)!)
        while power <= n:
            count += n // power    # the amount of numbers which divide by that prime power
            count -= k // power
            count -= (n - k) // power
            power *= p
            
        total_sum += count * p
        
    print(total_sum)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=20 * 10**6)
    parser.add_argument('--k', type=int, default=15 * 10**6)
    args = parser.parse_args()

    t = time.time()
    main(n=args.n, k=args.k)
    print(time.time() - t)