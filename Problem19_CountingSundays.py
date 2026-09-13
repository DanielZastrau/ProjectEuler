# 1st january 1901 - 31st december 2000
# 1st january 1900 - Monday

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

Week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Y365 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Y366 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def main():
    # weekday of 1st januare 1901
    day_count = 1
    w_index = 0
    while day_count <= 365:
        day_count += 1
        w_index += 1

        if w_index % 7 == 0: w_index = 0


    # daycount off all years 1901 - 2000
    Years = []
    for year in range(1901, 2001):
        if year % 4 == 0: Years.append(Y366)
        else: Years.append(Y365)

    # count sundays per year 
    sunday_count = 0
    for year in Years:
        for month in year:
            count = 0
            while count < month:

                if w_index == 6 and count == 0:
                    sunday_count += 1

                count += 1
                w_index += 1

                if w_index % 7 == 0:
                    w_index = 0
    print(sunday_count)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)