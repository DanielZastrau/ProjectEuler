###############################################################################
# variable names: lower_case_with_underscores       (int, str, tuples, bools)
# -- with trailing underscore when using names of built-in functions
# variable names: Upper_first_with_underscores      (list, set, dict)
# variable names: UPPER_CASE_WITH_UNDERSCORES       (constants)
# function names: mixedCase
# class names:    CamelCase
# strings are ''
# comments in english, starting with upper case and ending with '.'

"""
https://projecteuler.net/problem=47
"""

import math
from copy import deepcopy
from time import sleep

def prime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False

    return True

def primeFactorization(num, P_factors):
    if num == 1: return

    if prime(num):
        P_factors.append(num)
        return P_factors

    for i in range(2, int((num + 1) / 2) + 1):
        if prime(i) and num%i == 0:
            P_factors.append(i)

            primeFactorization(num // i, P_factors)

            return P_factors

def clean(L):
    D = dict()
    Out = list()

    for elem in L:
        key = str(elem)
        if key in D.keys():
            D[key] += 1
        else:
            D[key] = 1
    
    for key, value in D.items():
        Out.append(int(key)**value)
    
    return Out, len(D.keys())

def main(amount):
    n = amount
    L = [False for elem in range(amount)]

    while True:
        Tmp, distinct = clean(primeFactorization(num=n, P_factors=[1])[1:])

        if distinct == amount:
            L.append(True)
        else:
            L.append(False)

        bool_ = True
        for i in range(1, amount + 1):
            if L[-i] == False:
                bool_ = False
        if bool_ == True:
            return len(L) - amount

        n += 1

print(main(4))