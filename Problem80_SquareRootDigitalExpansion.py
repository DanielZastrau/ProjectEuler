"""https://projecteuler.net/problem=80"""

if __name__=="__main__":
    from time import time, sleep
    from math import gcd

    t = time()

    def continued_fraction_expansion(square):
        def find_a(square):
            a = 1
            while a**2 < square:
                a += 1
            return a - 1

        def merge_it(num, denominator, numerator):
            numerator = num*denominator + numerator
            return numerator, denominator
        
        def flip_it(r, numerator, denominator):
            return r*denominator, numerator

        def reduce_it(numerator, denominator):
            x = gcd(numerator, denominator)
            if x != 1:
                numerator //= x
                denominator //= x
            return numerator, denominator

        def long_division(numerator, denominator):
            curr = numerator
            divisor = denominator

            Decimal_fraction = list()
            while len(Decimal_fraction) < 101:
                integer_part = curr//divisor
                curr = (curr - integer_part * divisor) * 10

                Decimal_fraction.append(integer_part)
            return Decimal_fraction

        a = find_a(square)
        r = square - a**2

        continued_fraction = list()
        continued_fraction.append(a)
        while len(continued_fraction) < 200:
            continued_fraction.append(2*a)

        numerator = r
        denominator = continued_fraction.pop()

        while len(continued_fraction) > 1:
            num = continued_fraction.pop()
            numerator, denominator = merge_it(num, denominator, numerator)
            numerator, denominator = flip_it(r, numerator, denominator)
            numerator, denominator = reduce_it(numerator, denominator)

        num = continued_fraction.pop()
        numerator, denominator = merge_it(num, denominator, numerator)

        return long_division(numerator, denominator)

    Squares = [i**2 for i in range(1, 10)]
    Nums = [ elem for elem in range(1, 100) if elem not in Squares ]

    s = 0
    for square in Nums:
        decimal_fraction = continued_fraction_expansion(square)
        s += sum(decimal_fraction[0:-1])

    print(s)

    print(time() - t)