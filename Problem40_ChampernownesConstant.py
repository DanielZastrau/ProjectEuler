import numpy as np
import math
import time

def first_part(s):
    for digit in range(1, 10):
        s += str(digit)
    return s

def second_part(s):
    for digit1 in range(1, 10):
        for digit2 in range(0, 10):
            s += str(digit1) + str(digit2)
    return s

def third_part(s):
    for digit1 in range(1, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                s += str(digit1) + str(digit2) + str(digit3)
    return s

def fourth_part(s):
    for digit1 in range(1, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                for digit4 in range(0, 10):
                    s += str(digit1) + str(digit2) + str(digit3) + str(digit4)
    return s

def fifth_part(s):
    for digit1 in range(1, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                for digit4 in range(0, 10):
                    for digit5 in range(0,10):
                        s += str(digit1) + str(digit2) + str(digit3) + str(digit4) + str(digit5)
    return s
    
def sixth_part(s):
    for digit1 in range(1, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                for digit4 in range(0, 10):
                    for digit5 in range(0,10):
                        for digit6 in range(0, 10):
                            s += str(digit1) + str(digit2) + str(digit3) + str(digit4) + str(digit5) + str(digit6)
    return s

def number(n):
    s = '0.'
    s = first_part(s)
    s = second_part(s)
    s = third_part(s)
    s = fourth_part(s)
    s = fifth_part(s)
    s = sixth_part(s)
    return s

def product_of_digits(n, Pos):
    n = n[1:]
    i = 0
    j = 0
    p = 1
    while i < len(n) and j < len(Pos):
        if i == Pos[j]:
            print(n[i])
            p *= int(n[i])
            j += 1
        i += 1
    return p


n = 10 ** 6
print(product_of_digits(number(n), [1, 10, 100, 1000, 10000, 100000, 1000000]))