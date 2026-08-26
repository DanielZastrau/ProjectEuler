"""https://projecteuler.net/problem=120
Aug 26

limit=10**9      7 037     3.943s
limit=10**10    21 035     0.05108s    correct
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

from PrimeSieves import eratosthenes

def remainder(prime: int, n: int) -> int:

    prime_sq = pow(prime, 2)
    return (pow(prime - 1, n, prime_sq) + pow(prime + 1, n, prime_sq)) % prime_sq

def main(limit: int = 10**10):

    primes = eratosthenes(limit=math.isqrt(limit*10))
    print(time.time() - t)    # 0.0098s for limit=10**10

    for index in range(7037, len(primes)):
        if remainder(primes[index], index + 1) > limit:
            print(index + 1)
            break

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**10)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)