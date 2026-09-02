import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import Commons

def factorial_inner(n: int) -> int:
    if n == 0: return 1
    if n == 1: return 1
    return factorial_inner(n - 1) * n

def factorial_outer() -> dict[int, int]:
    d: dict[int, int] = {}
    for n in range(0, 10):
        d[n] = factorial_inner(n)
    return d

def make_list(n: int):
    return [int(x) for x in str(n)]

def sum_of_digit_fact(n: int, d: dict[int, int]):
    return sum([d[x] for x in make_list(n)])

def main():
    numbers: list[int] = []
    d = factorial_outer()
    for n in range(10, 10**5):
        if n == sum_of_digit_fact(n, d):
            numbers.append(n)

    print(sum(numbers))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)