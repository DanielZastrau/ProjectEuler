"""https://projecteuler.net/problem=71"""

from time import time, sleep
from math import gcd

def is_less(num1, den1, num2, den2):
    n1 = num1 * den2
    n2 = num2 * den1

    return n1 < n2

def reduce_(numerator, denominator):
    ggT = gcd(numerator, denominator)
    while ggT != 1:
        numerator = numerator // ggT
        denominator = denominator // ggT

        ggT = gcd(numerator, denominator)
    return numerator, denominator

if __name__=="__main__":
    t = time()

    curr = [0, 1]
    for denominator in range(10**6, 2, -1):
        numerator = max(1, ((denominator // 7) * 3))

        while is_less(numerator + 1, denominator, 3, 7):
            numerator += 1
        closest = [numerator, denominator]

        if is_less(curr[0], curr[1], closest[0], closest[1]) and is_less(closest[0], closest[1], 3, 7):
            curr = closest

    curr = reduce_(curr[0], curr[1])

    print(curr)
    print(time() - t)