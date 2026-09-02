"""https://projecteuler.net/problem=5"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import Commons

def main(n: int):

    primes = Commons.eratosthenes(limit=n)

    #! this is equivalent to computing power such that prime**power = n
    #! log both sides and take the floor
    powers = [math.floor(math.log10(n) / math.log10(prime)) for prime in primes]

    m = 1
    for prime, power in zip(primes, powers):
        m *= prime**power

    print(m)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main(20)
    print(time.time() - t)