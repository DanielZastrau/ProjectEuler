#sum of all primes below 2 million
import time
import math

Primes = [2, 3]
integer = 4

while True:
    # time.sleep(1)
    
    Bool = True

    for prime in Primes:

        if prime > math.sqrt(integer):
            Bool = True
            break

        if integer % prime == 0:
            Bool = False
            break
    
    if Bool: 
        if integer >= 2000000:
            break
        else:
            Primes.append(integer)
            integer = integer + 1
    elif not Bool: 
        integer = integer + 1

sum1 = sum(Primes)
print(sum1)