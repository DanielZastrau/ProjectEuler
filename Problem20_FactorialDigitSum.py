"""https://projecteuler.net/problem=20
"""

import time
import math

import Commons

def main(n: int = 100_000):

    factorial = math.factorial(n)
    digitsum = Commons.digitsum(factorial)
    print(digitsum)

if __name__=='__main__':
    t = time.time()
    main()
    print(time.time() - t)