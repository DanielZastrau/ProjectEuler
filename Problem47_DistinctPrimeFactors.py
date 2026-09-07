"""https://projecteuler.net/problem=47
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def main(amount: int) -> int:

    factors: list[int] = [0 for _ in range(200_000)]
    for n in range(2, 200_000):
        if factors[n] == 0:

            for nn in it.count(start=n, step=n):
                if nn >= 200_000:
                    break
                factors[nn] += 1

    consec = 0
    for n in range(1000, 200_000):
        if factors[n] == amount:
            consec += 1
        else:
            consec = 0

        if consec == amount:
            print(n - 3)
            break

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main(4)
    print(time.time() - t)