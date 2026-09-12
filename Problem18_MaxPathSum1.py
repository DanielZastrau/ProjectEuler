"""https://projecteuler.net/problem=18
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

string = '''75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def make_pyramid(L: list[str]) -> list[list[int]]:
    I: list[list[int]] = []
    list_length = 1

    while L:
        I.append([])
        for _ in range(list_length):
            I[-1].append(int(L[0]))
            del L[0]

        list_length = list_length + 1
    
    return I

def make_max(I: list[list[int]], r_index: int, c_index: int) -> int:
    int1 = I[r_index][c_index] + I[r_index + 1][c_index]
    int2 = I[r_index][c_index] + I[r_index + 1][c_index + 1]
    return max(int1, int2)

def sink_pyramid(I: list[list[int]]):
    for row_index in range(len(I) - 2, -1, -1):
        for column_index in range(len(I[row_index])):
            I[row_index][column_index] = make_max(I, row_index, column_index)

def main():
    L = string.strip().split(' ')
    I = make_pyramid(L)
    sink_pyramid(I)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)