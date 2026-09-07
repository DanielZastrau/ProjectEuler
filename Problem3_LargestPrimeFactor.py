"""https://projecteuler.net/problem=3"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import Commons

if __name__=="__main__":
    t = time.time()

    primes = Commons.eratosthenes(limit=10**6)
    # n = 600_851_475_143
    n = 91
    m = n
    max_ = 0
    sqroot = n ** 0.5

    for prime in primes:
        if prime > sqroot:
            break
        elif n%prime == 0:
            max_ = prime
            n //= prime
            while n%prime == 0:
                n //= prime
            sqroot = n**0.5

    if n != 1:
        print(n)
    else:
        print(max_)

    print(time.time() - t)