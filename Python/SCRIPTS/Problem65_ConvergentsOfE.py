"""https://projecteuler.net/problem=65"""

from time import sleep, time
from math import gcd, e, floor

class term:

    def __init__(self, v1, operator, v2):
        self.v1 = v1
        self.operator = operator
        self.v2 = v2

    def __repr__(self):
        return str(self.v1) + self.operator + str(self.v2)

class fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

def continued_fraction():
    A = [1]*100
    A[0] = 2

    n = 1
    while n*3 < 100:
        A[n*3 - 1] = n*2
        n += 1
        
    return A

def final_fraction(A):
    numerator = 1
    denominator = A.pop()
    curr_frac = fraction(numerator, denominator)

    while len(A) > 1:
        integer_part = A.pop()

        numerator = curr_frac.denominator
        denominator = integer_part*curr_frac.denominator + curr_frac.numerator

        curr_frac.numerator = numerator
        curr_frac.denominator = denominator

    integer_part = A.pop()

    numerator = integer_part*curr_frac.denominator + curr_frac.numerator
    denominator = curr_frac.denominator

    curr_frac.numerator = numerator
    curr_frac.denominator = denominator

    return curr_frac

    

if __name__=="__main__":
    t = time()
    
    Integer_parts = continued_fraction()
    Fraction = final_fraction(Integer_parts)
    sum_ = sum([ int(elem) for elem in str(Fraction.numerator) ])
    
    print(sum_)
    print(time() - t)