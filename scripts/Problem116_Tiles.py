"""https://projecteuler.net/problem=116
Aug 26

         3 253    0.001023s    wrong
20 492 570 929    0.001535s    correct
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

def combinations(tiles: int, length: int, d: dict[int, int] = {}) -> tuple[int, dict[int, int]]:

    if tiles in d:
        return d[tiles], d

    amount0 = tiles - length + 1
    amount1 = 0
    for starting_square in range(amount0):

        rest_length = tiles - starting_square - length
        if rest_length >= length:
            amount, d = combinations(tiles=rest_length, length=length, d=d)
            amount1 += amount

    amount = amount0 + amount1
    d[tiles] = amount

    return amount, d

def main(tiles: int = 50):
    length_red = 2
    length_gre = 3
    length_blu = 4

    amount_red, _ = combinations(tiles=tiles, length=length_red, d={})
    print(amount_red, time.time() - t)

    amount_gre, _ = combinations(tiles=tiles, length=length_gre, d={})
    print(amount_gre, time.time() - t)

    amount_blu, _ = combinations(tiles=tiles, length=length_blu, d={})
    print(amount_blu, time.time() - t)

    print(amount_red + amount_gre + amount_blu)
    
if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--tiles', type=int, default=50)
    args = parser.parse_args()

    t = time.time()
    main(tiles=args.tiles)
    print(time.time() - t)