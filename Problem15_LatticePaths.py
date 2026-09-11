"""https://projecteuler.net/problem=15
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def main(k, n):
    number1 = 1
    for integer in range(n, 0, -1):
        number1 = number1 * integer
    #print(number1)

    number2 = 1
    for integer in range(k, 0, -1):
        number2 = number2 * integer
    #print(number2)

    number3 = 1
    for integer in range(n - k, 0, -1):
        number3 = number3 * integer
    #print(number3)

    return int(number1 / (number2 * number3))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    print(main(1, 2))
    print(main(2, 4))
    print(main(3, 6))
    print(main(4, 8))
    print(main(5, 10))
    print(main(6, 12))
    print(main(7, 14))
    print(main(8, 16))
    print(main(9, 18))
    print(main(10, 20))
    print(main(11, 22))
    print(main(12, 24))
    print(main(13, 26))
    print(main(14, 28))
    print(main(15, 30))
    print(main(16, 32))
    print(main(17, 34))
    print(main(18, 36))
    print(main(19, 38))
    print(main(20, 40))
    print(time.time() - t)
