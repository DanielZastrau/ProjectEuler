"""https://projecteuler.net/problem=12
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons


def get_number_of_divisors(number: int):
    integer = 1
    count = 0
    while integer < math.sqrt(number):
        if number % integer == 0:
            count = count + 2
        integer = integer + 1

    if math.sqrt(number) % 1 == 0:
        count = count + 1

    return count

def main():

    n = 0    
    for m in range(1, 10**8):
        n += m
        number = get_number_of_divisors(n)

        if number > 500:
            print(n)
            break

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)