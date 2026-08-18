"""https://projecteuler.net/problem=94

The almost equilateral triangle with side-lengths 5-5-6 has an area of 12 square units.
Thus, it has integral side-lengths and integral-area.

An almost equilateral triangle is one, where two side-lengths are equal and the third
differs by no more than 1.

I am supposed to find the sum of all perimeters of all almost equilateral triangles
        whose perimeter does not exceed 10**9.

First version:
    Iterating over all base lengths 1 to 10**9 / 3
    Calculating area with a, b, c Heron Formula
    Also I should mention that the first version put out a wrong result.
    
    ~ Result:    312 532 312 457 237 949    <    Is wrong
    ~ Took around 8 minutes

Second version:
    By my own derivation only iterating over odd values of a.
    Using the reformulated Heron formula
    Also safeguarding the addition against the explicit condition of the perimeter
            being less than 10**9
    
    ~ Result:    84 636 964 359 940    <    Is wrong
    ~ Took 200 seconds

Third version:
    Corrected my calculations I forgot to take the square power ...

    ~ Result:    156 266 819 179 846 792    <    Is wrong
    ~ Took 170 seconds

Third version:
    Took out a=1 and rewrote the area calculation

    ~ Result:    156 265 614 708 331 246    <    Is wrong
    ~ Took 134 seconds

Fourth version:
    Instead of checking perim length in each loop iteration, I add everything for now
            because the condition is true for all but maybe 2 or 3 at the end.
            After everything I filter and sum.

    ~ Result:    156 265 614 708 331 252    <    wrong
    ~ Took 145 seconds

Fifth version:
    Maybe my reformulation of Heron's formula was wrong?

    156 265 895 025 827 800    including 110 and 112    <    wrong
    156 265 895 025 827 794    excluding 110 and 112    <    wrong

Sixth version:
    Throwing out my assumption that a has to be odd and c has to be even.

    312 532 313 457 237 949    including 110 and 112    <    wrong
    312 532 313 457 237 943    excluding 110 and 112    <    wrong

Seventh version:
    Brute forcing even more, instead of trying to hit the limit, I increased
            the search space and just threw out everything too big afterwards.

    312 532 313 457 237 949    including 110 and 112
    312 532 313 457 237 943    excluding 110 and 112

    312 532 314 457 237 949
    312 532 314 457 237 943    No idea why the third block is suddenly 314 instead of 313


    These are actually the same values that I got in the sixth version.

Eight version:
    Reformulated Herons formula with b=a and c=a+1 or a-1. This yields two polynomials of 4th order.
    Then iterating over all possible values of a, calculating the polynomials and checking if their
            squareroot is integral.

    312 532 835 176 830 041     including the values for a=1    wrong
    312 532 835 176 830 035     excluding the values for a=1    wrong

Ninth version:
    now added the check that the int of the square root also needs to yield the squared area

    2 319 414 011    including a=1    wrong
    2 319 414 005    excluding a=1    wrong

    That ran for about 560 seconds

Tenth version:
    Rewrote the polynomial in Herons formula. Pulled out the c so that leaves a polynomial of order 2.
    This reduces the maximum encountered number down from roughly limit**4 to limit**2

    limit=1_000    990    0.0002
        1 1 0
        1 1 2
        5 5 6
        17 17 16
        65 65 66
        241 241 240
    limit=10_000    3694    0.001
    limit=100_000    51 412    0.01
    limit=1_000_000    1 905 582    0.1
    limit=10_000_000    12 405 628 839    1.7
    limit=100_000_000    127 140 974 991 078    18.5
    limit=1_000_000_000    312 530 319 954 683 781    238.09

Eleventh version:
    Now using the decimal package to better handle the precisions.
    --- Added that we only check odd values of a
    --- Added that the distance between correct values of a is less than the previous distance

    These are all inclusive of 112 and 110, apparently the problem excludes these.
    limit=1_000    990    0.002    0.0016    0.0008
    limit=10_000    3694    0.02    0.012    0.0033
    limit=100_000    51 412    0.2    0.112    0.012
    limit=1_000_000    716 038    2.04    1.07    0.157    This is the first difference to previous versions
    limit=10_000_000    9 973 084    20.5    10.77    2.08
    limit=100_000_000    37 220 046    325.89    106.14    27.15
    limit=1_000_000_000    518 408 352    xxx.xxx    ---.---    113.15    <    This is correct (without 112 and 110)
    """

import argparse
import time
import decimal

def main(limit: int = 10**9):

    decimal.getcontext().prec = 32

    perimeters: list[float] = []

    factor_one = decimal.Decimal(0.25)
    factor_two = decimal.Decimal(3)
    factor_three = decimal.Decimal(2)

    a = 1
    while a < (limit // 3) + 2:

        double = False

        a_ = decimal.Decimal(a)
        a_plus_one = decimal.Decimal(a + 1)
        a_minus_one = decimal.Decimal(a - 1)

        A_one = factor_one * a_plus_one * (factor_two * a_ ** 2 - factor_three * a_ - 1).sqrt()
        A_two = factor_one * a_minus_one * (factor_two * a_ ** 2 + factor_three * a_ - 1).sqrt()

        perim_one = 3 * a_ + 1
        if A_one % 1 == 0 and perim_one < limit:
            double = True
            perimeters.append(3 * a + 1)

        perim_two = 3 * a_ - 1
        if A_two % 1 == 0 and perim_two < limit:
            double = True
            perimeters.append(3 * a - 1)

        if double:
            a *= 2 + 1
        else:
            a += 2

    print(sum(perimeters))

if __name__=='__main__': 

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**9)
    args = parser.parse_args()

    t = time.time()

    main(limit=args.limit)

    print(f'Completion took    {time.time() - t}  seconds.')