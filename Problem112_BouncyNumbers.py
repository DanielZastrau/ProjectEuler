"""https://projecteuler.net/problem=112"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def is_increasing_number(number: int) -> bool:

    string = str(number)

    for i in range(len(string) - 1):
        if int(string[i]) > int(string[i + 1]):
            return False
        
    return True


def is_decreasing_number(number: int) -> bool:

    string = str(number)

    for i in range(len(string) - 1):
        if int(string[i]) < int(string[i + 1]):
            return False
    
    return True


def is_bouncy_number(number: int) -> bool:

    if not is_increasing_number(number=number) and not is_decreasing_number(number=number):
        return True
    return False

def main(level: float):
    """The first integer for which the proportion of bouncy numbers below it, reaches the level.
    50% is specified as 0.5
    """

    count = 0
    number = 100
    while True:

        if is_bouncy_number(number=number):
            count += 1

        if count / number == level:
            print(number)
            break

        number += 1

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main(level=0.99)
    print(time.time() - t)