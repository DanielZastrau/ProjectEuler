"""
https://projecteuler.net/problem=56
"""

from Package import cross_sum

def main():
    max_ = 0
    for a in range(1, 100):
        for b in range(1, 100):
            val = cross_sum(a**b)

            if val > max_:
                max_ = val
    return max_

print(main())