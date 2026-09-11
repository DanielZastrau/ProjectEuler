"""
https://projecteuler.net/problem=55
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def reverse(num: int):
    return int(''.join(str(num)[::-1]))

def palindrome(num: int):
    return str(num) == str(num)[::-1]

def lychrel(num: int):
    for _ in range(50):
        num = num + reverse(num)

        if palindrome(num):
            return False
    return True

def main():
    c = 0
    for num in range(10**4):
        if lychrel(num):
            c += 1
    return c

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)