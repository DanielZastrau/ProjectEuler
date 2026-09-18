"""https://projecteuler.net/problem=29
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

def main():

    distinct_nums: set[int] = set()
    for a in range(2, 101):
        for b in range(2, 101):
            distinct_nums.add(a ** b)
    print(len(distinct_nums))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)