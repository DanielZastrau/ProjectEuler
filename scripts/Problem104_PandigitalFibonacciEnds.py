"""https://projecteuler.net/problem=104
Aug 26

3890    0.15    wrong
329468    76.110    right
329468    1.866    returned the last 9 digits from the generator to reduce the calculation 
                    of the last nine digits from a 50k digit number to a fixed 9 digit number
                    the heavy calculation using the full 50k digit number then only gets executed once.

                    50k is only an example, the number lengths obviously increases and always hovers just
                    above 20% of the index. I.e., 100k index -> 20k+ number length
"""

import argparse
import sys
import os
import time
import math 
import itertools as it

D = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_pandigital(digits: list[int]) -> bool:

    if sorted(digits) == D:
        return True
    return False

def fibonacci_numbers():

    x = 1
    x_latter = 1
    yield x, x_latter

    y = 1
    y_latter = 1
    yield y, y_latter

    while True:

        x, y = y , x + y

        x_latter, y_latter = y_latter, x_latter + y_latter
        y_latter = y_latter % 10**9

        yield y, y_latter

def main():

    for index, (fib_n, fib_n_latter) in enumerate(fibonacci_numbers(), start=1):

        #! smaller number means faster calculation,   only ever 9 digit number compared to above 50k digits
        last_nine_digits = [fib_n_latter // 10**power % 10 for power in range(0, 9)]
        if is_pandigital(last_nine_digits):

            length = int(math.log10(fib_n)) + 1
            first_nine_digits = [fib_n // 10**power % 10 for power in range(length - 1, length - 10, -1)]

            if is_pandigital(first_nine_digits):
                print(index)
                break

if __name__=='__main__':
    t = time.time()

    main()

    print(time.time() - t)