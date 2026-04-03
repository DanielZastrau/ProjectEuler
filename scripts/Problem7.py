#what is the 10 001-st prime
import time
import math

Primes = [2, 3]
integer = 4

while True:
    # time.sleep(1)

    if len(Primes) == 10001: break
    
    Bool = True

    for prime in Primes:

        if prime > math.sqrt(integer):
            Bool = True
            break

        if integer % prime == 0:
            Bool = False
            break
    
    if Bool: 
        Primes.append(integer)
        integer = integer + 1
    elif not Bool: 
        integer = integer + 1

print(Primes[-1])