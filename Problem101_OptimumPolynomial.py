"""https://projecteuler.net/problem=101
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def polynomial(n: int):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def polynomial_generating_fn(term_count: int) -> list[int]:
    return [polynomial(n) for n in range(1, term_count + 1)]

def test_fn(term_count: int) -> list[int]:
    return [n**3 for n in range(1, term_count + 1)]

def lagrangian_base_polynomials(k: int, xs: list[int], x: int) -> float:
    out = 1
    for i in range(len(xs)):
        if i == k:
            continue
        out *= (x - xs[i]) / (xs[k] - xs[i])
    return out

def lagrangian_polynomial_interpolation(xs: list[int], ys: list[int], x: int) -> float:
    out = 0
    for k in range(len(xs)):
        out += ys[k] * lagrangian_base_polynomials(k, xs, x)
    return out

def main():

    terms = polynomial_generating_fn(1001)
    s = 0
    for degree in range(0, 1000):
        print(degree)
        xs = [n for n in range(1, degree + 2)]
        ys = terms[ : degree + 1]
        broke_out = False

        for x in range(degree + 2, 1000):
            y = lagrangian_polynomial_interpolation(xs, ys, x)

            if y != terms[x - 1]:    #! then we have found the first incorrect term
                broke_out = True
                s += y
                break
        if not broke_out:
            break
    print('Finished')
    print(s)


if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)