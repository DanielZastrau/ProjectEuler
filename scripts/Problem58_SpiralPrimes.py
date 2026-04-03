"""
https://projecteuler.net/problem=58
"""

from Package import prime
from time import sleep

def main():
    Dia_lo, Dia_lu, Dia_ro, Dia_ru = [1], [1], [1], [1]
    Dias = [Dia_lo, Dia_lu, Dia_ro, Dia_ru]
    
    index, add, primes, total, side_length = 0, 2, 0, 1, 1
    while True:
        for i in range(4):
            Dias[index].append( Dias[index][-1] + add )

            index = (index + 1)%4
            add += 2

        side_length += 2
        total += 4
        primes += len([ elem[-1] for elem in Dias if prime(elem[-1]) ])
        ratio = primes / total
        print(ratio)

        if ratio < 0.1:
            return side_length

print(main())