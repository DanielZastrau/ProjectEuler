"""https://projecteuler.net/problem=70"""

from time import time, sleep
from math import isclose
from Constants import primes_up_to_10Million
from Package import are_permutations_of_each_other, unique_prime_factors

def phi(prime_factors):
    if len(prime_factors) == 2:
        return (prime_factors[0] - 1) * (prime_factors[1] - 1)

if __name__=="__main__":
    t = time()

    Primes = primes_up_to_10Million()
    print(len(Primes))

    middle_point = int((10**7)**0.5)
    variance = 4*int((10**7)**(1/3))

    Primes_search = list()
    for prime in Primes:
        if middle_point - variance < prime < middle_point + variance:
            Primes_search.append(prime)

    for prime1 in Primes_search:
            for prime2 in Primes_search: 
                    n = prime1 * prime2

                    if n < 10**7:
                        phi_ = phi([prime1, prime2])
                        
                        if are_permutations_of_each_other(n, phi_):
                            print(f'n : {n} | phi : {phi_} | ratio : {n/phi_} ')
        
    print(time() - t)