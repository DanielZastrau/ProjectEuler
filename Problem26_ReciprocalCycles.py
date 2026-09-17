"""https://projecteuler.net/problem=26
"""

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

def cycle_length(n: int) -> int:
    remainders: list[int] = []
    r = 1
    for _ in range(0, n):
        x = r % n

        for i in range(len(remainders)):
            if remainders[i] == x:
                return len(remainders) - i
            
        remainders.append(x)
        r = x * 10
    return 0

def main():
    m = 0
    for n in range(2, 1000):
        l = cycle_length(n)
        if l > m:
            m = n

    print(m)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)
