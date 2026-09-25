import math
import time

def digitsum(n: int):
    return sum([int(char) for char in str(n)])

def isprime(n: int):
    if n <= 1:
        return False
    for m in range(2, math.isqrt(n) + 1):
        if n % m == 0:
            return False
    return True

def eratosthenes(limit: int) -> list[int]:
    """Calculates all primes up to limit=10**9 in under 45 seconds."""

    numbers: list[bool] = [True] * (limit + 1)

    slice_len = (len(numbers) - 4 + 2 - 1) // 2
    numbers[4::2] = [False] * slice_len

    for n in range(3, math.isqrt(limit) + 1, 2):
        if numbers[n]:
            # only checking the odd multiples, because even multiples are already covered by 2
            # starting at the square, because previous multiples are covered by previous primes
            start, step = pow(n, 2), 2*n
            slice_len = (len(numbers) - start + step - 1) // step
            numbers[start::step] = [False] * slice_len
            
    return [index for index in range(2, len(numbers)) if numbers[index]]

def prime_factorization_sieve(limit: int) -> list[list[int]]:

    numbers: list[list[int]] = [[] for _ in range(limit + 1)]
    numbers[1] = [1]
    for n in range(2, limit + 1):
        if not numbers[n]:
            for nn in range(n, limit + 1, n):

                power = 0
                while nn % pow(n, power + 1) == 0:
                    power += 1
                numbers[nn].extend([n] * power)
            
    return numbers

def prime_factorization_of_int(n: int) -> list[int]:

    primes = eratosthenes(limit= n// 2 + 1)
    prime_factors: list[int] = []
    for prime in primes:
        if n % prime:
            prime_factors.append(prime)
    return prime_factors

def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int, int, int, int]:
    """computes the bezout coefficients for integers a and b:    ax + by = gcd(a, b)
    args:    a    integer
             b    integer
    returns: tuple
                bezout coefficients x and y in places 0 and 1
                gcd d in place 2
                quotients by the gcd of a and b in places 3 and 4
    """

    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r

        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_s, old_t, old_r, t, s