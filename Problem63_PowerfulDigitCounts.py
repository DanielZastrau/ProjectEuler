"""
https://projecteuler.net/problem=63
"""

from time import time

if __name__=="__main__":
    t = time()
    
    curr_pow = 1
    c = 0
    n = 1

    while True:
        if 10**(curr_pow - 1) <= n**curr_pow < 10**curr_pow:
            c += 1
            n += 1
        elif n**curr_pow < 10**(curr_pow - 1):
            n += 1
        elif n**curr_pow >= 10**(curr_pow):
            curr_pow += 1
            n = 1
        print(c, curr_pow)

        if time() - t > 60:
            break