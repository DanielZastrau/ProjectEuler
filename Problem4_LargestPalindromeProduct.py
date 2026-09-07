"""https://projecteuler.net/problem=4"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def main():
    max_ = (0, 0, 0)

    for n1 in range(999, 99, -1):
        for n2 in range(999, n1 - 1, -1):
            number = n1 * n2
            if number <= max_[0]:
                break

            if str(number) == str(number)[::-1]:
                max_ = (number, n1, n2)

    print(max_)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)