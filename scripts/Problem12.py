#value of the first triangle number with over 500 divisiors
#x-th triangle number is the sum of the first x positive integers
import math
import time

TN = [1]

def get_next_number():
    integer = len(TN) + 1
    TN.append(TN[-1] + integer)

def get_number_of_divisors(number):
    integer = 1
    count = 0
    while integer < math.sqrt(number):
        if number % integer == 0:
            count = count + 2
        integer = integer + 1

    if math.sqrt(number) % 1 == 0:
        count = count + 1

    return count

while True:
    get_next_number()
    number = get_number_of_divisors(TN[-1])

    if number > 500:
        print(TN[-1])
        break