import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def common_digit(s1: list[int], s2: list[int]) -> int:
    for digit in s1:
        if digit in s2:
            return digit
    return 0

def main():
    numbers: list[tuple[int,int]] = []
    for numerator in range(10,100):
        for denominator in range(numerator + 1, 100):
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue
            numbers1 = [int(char) for char in str(numerator)]
            numbers2 = [int(char) for char in str(denominator)]
            v = common_digit(numbers1, numbers2)
            if v:
                numbers1.remove(v)
                numbers2.remove(v)
                if numbers2[0] != 0 and numerator / denominator == numbers1[0] / numbers2[0]:
                    numbers.append((numerator, denominator))

    print(numbers)
    total_num, total_denom = 1, 1
    for numerator, denominator in numbers:
        total_num *= numerator
        total_denom *= denominator

    x = math.gcd(total_num, total_denom)
    while x > 1:
        total_num //= x
        total_denom //= x
        x = math.gcd(total_num, total_denom)
    print(total_denom)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)