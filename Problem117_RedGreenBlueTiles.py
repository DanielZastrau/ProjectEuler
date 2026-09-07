"""https://projecteuler.net/problem=117
Sep 26"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

@ft.cache
def combinations(n: int, m: int, M: int) -> int:
    """m  >  minimum block length
    n  >  total amount of blocks"""

    amount0 = 0
    for block_length in range(m, M + 1):
        if block_length <= n:
            amount1 = n - block_length + 1    # possible starting squares
            amount0 += amount1

            for starting_square in range(amount1):
                rest_n = n - starting_square - block_length

                if rest_n >= m:
                    amount2 = combinations(n=rest_n, m=m, M=M)
                    amount0 += amount2

    return amount0

def main(m: int = 2, n: int = 50, M: int = 4):
    """m  >  minimum block length
    n  >  total block length"""
    print(n)
    print(combinations(m=m, n=n, M=M) + 1)
    print(combinations.cache_info())

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=int, default=2)
    parser.add_argument('--n', type=int, default=50)
    parser.add_argument('--M', type=int, default=4)
    args = parser.parse_args()

    t = time.time()
    main(m=args.m, n=args.n, M=args.M)
    print(time.time() - t)