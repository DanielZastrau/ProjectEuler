"""
https://projecteuler.net/problem=51
"""

from time import sleep, time
from Package import prime

def positions(length):
    if length == 1:
        return []
    
    elif length == 2:
        return []

    elif length == 3:
        return []

    elif length == 4:
        return [
            [0, 1, 2]
        ]
    
    elif length == 5:
        return [
            [0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]
        ]

    elif length == 6:
        return [
            [0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 3], [0, 2, 4], [0, 3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4],
            [0, 1, 2, 3, 4]
        ]

    elif length == 7:
        return [
            [0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 1, 5], [0, 2, 3], [0, 2, 4], [0, 2, 5], [0, 3, 4], [0, 3, 5], [0, 4, 5],
            [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5],
            [0, 1, 2, 3, 4], [0, 1, 2, 3, 5], [0, 1, 2, 4, 5], [0, 1, 3, 4, 5], [0, 2, 3, 4, 5], [1, 2, 3, 4, 5]
        ]

def build_string(list_of_digits, pos, n):
    new_list_of_digits = [elem for elem in list_of_digits]

    for p in pos:
        new_list_of_digits[p] = str(n)
    
    return new_list_of_digits

def check_replacements(num, amount):
    list_of_digits = [ elem for elem in str(num) ]
    length = len(list_of_digits)

    Pos = positions(length)

    for pos in Pos:
        Repl = []
        if 0 in pos:
            for n in range(1, 10):
                Repl.append(build_string(list_of_digits, pos, n))
        else:
            for n in range(0, 10):
                Repl.append(build_string(list_of_digits, pos, n))

        Repl = [ int(''.join(elem)) for elem in Repl ]
        Repl = list(filter(prime, Repl))

        if len(Repl) == amount:
            print(Repl)
            return True, min(Repl)
    return False, False

def main(amount):
    t1 = time()

    num = 3
    while True:

        if int(time() - t1) >= 60:
            return num, 'did not finish'

        if prime(num):
            bool_, n = check_replacements(num, amount)

            if bool_:
                return n
            
        num += 2

t1 = time()
print(main(8))
t2 = time()
print(t2 - t1)