"""https://projecteuler.net/problem=64"""

from time import sleep, time
from math import gcd

class term:

    def __init__(self, v1, operator, v2):
        self.v1 = v1
        self.operator = operator
        self.v2 = v2

    def __repr__(self):
        return str(self.v1) + self.operator + str(self.v2)

def find_integer_part(numerator, denominator):
    expr = lambda x: denominator.v1**2 * x**2 - 2*denominator.v1*numerator.v2*x + numerator.v2**2

    n = 1
    while expr(n) < num:
        n += 1
    return n-1

def extract_it(numerator, denominator, integer_part):
    numerator_out = term(numerator.v1, '-', abs(numerator.v2 - integer_part*denominator.v1))
    return numerator_out, denominator

def flip_it(numerator, denominator):
    return denominator, numerator

def expand_it(numerator, denominator):
    expansion = term(denominator.v1 , '+', denominator.v2)
    numerator_out = term(numerator, '*', expansion)
    denominator_out = term(denominator, '*', expansion)
    return numerator_out, denominator_out

def reduce_it(numerator, denominator):
    denominator_out = term(denominator.v1.v1 - denominator.v2.v2**2, '+', 0)

    if numerator.v1.v1 == 1:
        numerator_out = numerator.v2
    elif numerator.v1.v1 != 1:
        ggT = gcd(numerator.v1.v1, denominator_out.v1)
        if ggT != 1:
            factor = numerator.v1.v1 // ggT
            denominator_out.v1 = denominator_out.v1 // ggT
            if factor == 1:
                numerator_out = numerator.v2
            else:
                numerator_out = numerator.v2
                numerator_out.v1 = numerator_out.v1 * factor
                numerator_out.v2 = numerator_out.v2 * factor
        else:
            numerator_out = numerator.v2
            numerator_out.v1 = numerator_out.v1 * factor
            numerator_out.v2 = numerator_out.v2 * factor

    return numerator_out, denominator_out

def find_period(A):
    check = A[1:]

    period_length = 1
    while True:
        c = 0

        if period_length > len(check) / 2:
            return -1

        compare_slice = check[:period_length]
        slice_num = 1
        while True:
            curr_slice = check[period_length*slice_num:period_length*(slice_num+1)]

            if compare_slice == curr_slice:
                slice_num += 1

                if (slice_num + 1)*period_length >= len(check):
                    rest_length = len(check) - slice_num*period_length

                    if compare_slice[:rest_length] == check[-rest_length:]:
                        return period_length%2

            else:
                break

        period_length += 1

def odd_period(num):
    if num**0.5 %1 == 0:
        return False

    A = list()
    numerator = term(num, '+', 0)
    denominator = term(1, '+', 0)

    integer_part = find_integer_part(numerator, denominator)
    A.append(integer_part)
    numerator, denominator = extract_it(numerator, denominator, integer_part)

    while True:
        numerator, denominator = flip_it(numerator, denominator)
        numerator, denominator = expand_it(numerator, denominator)
        numerator, denominator = reduce_it(numerator, denominator)
        integer_part = find_integer_part(numerator, denominator)
        A.append(integer_part)
        numerator, denominator = extract_it(numerator, denominator, integer_part)

        if len(A) > 20:
            res = find_period(A)
            if res == -1:
                continue
            elif res == 0:
                return False
            elif res == 1:
                return True
            
if __name__=="__main__":
    t = time()
    c = 0
    for num in range(2, 10**4 + 1):
        if odd_period(num):
            c += 1
    print(c)
    print(time() - t)