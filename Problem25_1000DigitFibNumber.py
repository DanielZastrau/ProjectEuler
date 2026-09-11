"""https://projecteuler.net/problem=25
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def main():

    index = 2
    a, b = 1, 1
    while b < 10**999:
        a, b = b, a + b
        index += 1
        
    print(index)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)
