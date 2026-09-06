import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def inner_collatz(number: int) -> int:
    if number % 2 == 0: return number // 2
    elif number % 2 == 1: return (number * 3) + 1

def outer_collatz(SL: list[int], number: int) -> int:
    sequence_length = 1
    while not number == 1:
        number = int(inner_collatz(number))
        if number < len(SL):
            return sequence_length + SL[number]
        sequence_length = sequence_length + 1
    return sequence_length

def main():
    max_sl = float('-inf')
    max_int = 0
    SL: list[int] = [0,1]
    for integer in range(2,1000000):
        sl = outer_collatz(SL, integer)
        SL.append(sl)
        if sl > max_sl: 
            max_sl = sl
            max_int = integer

    print(max_int)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)