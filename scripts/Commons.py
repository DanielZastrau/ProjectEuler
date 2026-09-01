import math
import time

def digitsum(n: int):
    return sum([int(char) for char in str(n)])

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

def atkin(limit: int) -> list[int]:
    """That thing is painfully slow. Need to optimize it in the future to run on more low-level
    CPython-native operations."""

    primes: list[int] = [2, 3]
    sieve = [False] * (limit + 1)

    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):

            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]


    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit + 1, x**2):
                sieve[y] = False

    for p in range(5, limit):
        if sieve[p]:
            primes.append(p)

    return primes