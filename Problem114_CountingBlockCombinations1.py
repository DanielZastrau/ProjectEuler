"""https://projecteuler.net/problem=114
Sep 26"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import Commons

def combinations(n: int, m: int, d: dict[int, int] = {}) -> tuple[int, dict[int, int]]:
    """m  >  minimum block length
    n  >  total amount of blocks"""

    if n in d:
        return d[n], d

    amount = 0
    for block_length_to_be_placed in range(m, n + 1):
        print(n, m, block_length_to_be_placed)
        amount0 = n - block_length_to_be_placed + 1    # possible starting squares
        amount1 = 0

        for starting_square in range(amount0):
            # additional m1 at the end because each block has to be seperated by an empty square
            rest_m = n - starting_square - block_length_to_be_placed - 1

            if rest_m >= m:
                amount_tmp, d = combinations(n=rest_m, m=m, d=d)
                amount1 += amount_tmp

        amount = amount + amount0 + amount1
    d[n] = amount

    return amount, d

def main(m: int = 3, n: int = 50):
    """m  >  minimum block length
    n  >  total block length"""

    # p1 at the end to also count the empty arrangement
    print(combinations(n=n, m=m, d={})[0] + 1)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=int, default=3)
    parser.add_argument('--n', type=int, default=50)
    args = parser.parse_args()

    t = time.time()
    main(m=args.m, n=args.n)
    print(time.time() - t)