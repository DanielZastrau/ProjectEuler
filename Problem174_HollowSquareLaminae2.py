"""https://projecteuler.net/problem=174
Sep 26

387 236    wrong"""

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

def combination_to_tiles(limit: int):
    d: dict[str, int] = {}

    for outer_sq_base in range(1, limit + 1):
        if 2 * outer_sq_base + 2 * (outer_sq_base - 2) > limit:
            break

        parity = outer_sq_base % 2
        square = outer_sq_base**2
        if square <= limit:
            if parity == 0:
                start = 2
            else:
                start = 1

        else:
            diff = square - limit
            start = math.isqrt(diff) - 1

            if not start % 2 == parity:
                start -= 1

        for inner_sq_base in range(start, outer_sq_base, 2):

            val = outer_sq_base**2 - inner_sq_base**2
            if val <= limit:
                key = f'{outer_sq_base} {inner_sq_base}'
                d[key] = val

    return d

def count_tiles(outer_inner_to_tiles: dict[str, int]) -> dict[int, int]:

    d: dict[int, int] = {}
    for _, value in outer_inner_to_tiles.items():
        if value not in d:
            d[value] = 1
        else:
            d[value] += 1
    return d

def count_L(tile_count: dict[int, int]) -> dict[int, int]:

    d: dict[int, int] = {}
    for _, value in tile_count.items():
        if value not in d:
            d[value] = 1
        else:
            d[value] += 1
    return d

def main(limit: int):

    # outer square inner square -> amount of tiles used (t)
    outer_inner_to_tiles = combination_to_tiles(limit)

    # amount of tiles used (t) -> how many combinations of outer sq inner sq can be made with it
    tile_counts = count_tiles(outer_inner_to_tiles)

    # N(n) -> amount of t such that exactly n combinations can be made with it
    N_of_n = count_L(tile_counts)

    # the sum o
    print(sum([N_of_n[n] for n in range(1, 11)]))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**6)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)