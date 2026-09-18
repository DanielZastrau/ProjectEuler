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

    numbers: list[list[int]] = [[]] * (limit + 1)

    slice_len = (len(numbers) - 4 + 2 - 1) // 2
    numbers[4::2] = [[2]] * slice_len

    for n in range(3, math.isqrt(limit) + 1, 2):
        if not numbers[n]:
            # only checking the odd multiples, because even multiples are already covered by 2
            # starting at the square, because previous multiples are covered by previous primes
            start, step = pow(n, 2), 2*n
            for nn in range(start, limit + 1, step):
                numbers[nn].append(n)
            
    return numbers

def prime_factorization_of_int(n: int) -> list[int]:

    primes = eratosthenes(limit= n// 2 + 1)
    prime_factors: list[int] = []
    for prime in primes:
        if n % prime:
            prime_factors.append(prime)
    return prime_factors