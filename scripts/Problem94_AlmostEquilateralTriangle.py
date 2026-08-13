"""https://projecteuler.net/problem=94

The almost equilateral triangle with side-lengths 5-5-6 has an area of 12 square units.
Thus, it has integral side-lengths and integral-area.

An almost equilateral triangle is one, where two side-lengths are equal and the third
differs by no more than 1.

I am supposed to find the sum of all perimeters
    of all almost equilateral triangles
    whose perimeter does not exceed 10**9."""
import math
import time
import itertools

def calculate_perimeter(a: int, c: int) -> int:
    return 2*a + c

def calculate_area(a: int, c: int) -> float:
    """Calculated by Heron's Formula."""

    return math.sqrt(0.5 * a**2 *c - 0.125 * c)

def construct_sidelengths():
    """
    First version:
        Iterating over all base lengths 1 to 10**9 / 3
        Calculating area with a, b, c Heron Formula
        Also I should mention that the first version put out a wrong result.
        ~ Result:    312 532 312 457 237 949    <    Is wrong
        ~ Took around 8 minutes

    Second version:
        By my own derivation only iterating over ood values of a.
        Using the reformulated Heron formula
        Also safeguarding the addition against the explicit condition of the perimeter
                being less than 10**9
        ~ Result:    84 636 964 359 940    <    Is wrong
        ~ Took 200 seconds
    """

    s = 0
    limit = 10**9

    for a in range(1, limit, 2):

        if a % 1_000_000 == 1:
            print(f'--- iteration:    {a}')

        if a == 1:
            c = a + 1

            area_one = calculate_area(a, c)

            if area_one % 1.0 == 0:
                s += calculate_perimeter(a, c)

        else:    # a > 1:
            c1 = a - 1
            c2 = a + 1

            perim_one = calculate_perimeter(a, c1)
            if perim_one < limit:
                area_one = calculate_area(a, c1)

                if area_one % 1.0 == 0:
                    s += perim_one

            perim_two = calculate_perimeter(a, c2)
            if perim_two < limit:
                area_two = calculate_area(a, c2)

                if area_two % 1.0 == 0:
                    s += perim_two

                if a == 5 and c2 == 6:
                    print(f'The provided example:  {area_two}')

        if 2*a > limit:
            break

    print(s)

if __name__=='__main__':
    t = time.time()
    construct_sidelengths()

    print(f'Completion took    {time.time() - t}  seconds.')