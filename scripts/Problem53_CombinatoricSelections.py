"""
https://projecteuler.net/problem=53
"""

from math import factorial

c = 0
for n in range(1, 101):
    for k in range(1, n + 1):
        bin_coeff = factorial(n) // (factorial(k) * factorial(n - k))

        if bin_coeff > 10**6:
            c += 1

            if n == 23 and k == 10:
                print(bin_coeff)

print(c)