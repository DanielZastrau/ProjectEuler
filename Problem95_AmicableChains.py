"""https://projecteuler.net/problem=95

14 316    4.58s
"""

import argparse
import time
import math
import itertools as it
import decimal

def main(limit: int = 10**6):

    divisors: list[list[int]] = [[] for _ in range(limit)]

    for div in range(1, (limit // 2) + 1):

        value = 2 * div
        while value < limit:
            divisors[value - 1].append(div)
            value += div

    sums_of_divisors: list[int] = list(map(lambda x: sum(x), divisors))

    chain_length = 0
    chain_smallest_elem = 0

    for starting_elem in range(1, (limit // 2) + 1):

        reason = ''

        #! primes
        if sums_of_divisors[starting_elem - 1] == 1:
            continue

        chain = [starting_elem]
        next_elem = sums_of_divisors[starting_elem - 1]

        while True:

            if next_elem == starting_elem:
                reason = 'closed'
                break

            if next_elem in chain:
                reason = 'entered different chain'
                break

            if next_elem == 0:
                reason = 'done'
                break

            if next_elem > limit:
                reason = 'size'
                break

            chain.append(next_elem)
            next_elem = sums_of_divisors[next_elem - 1]

        if reason == 'closed':
            if len(chain) > chain_length:
                chain_length = len(chain)
                chain_smallest_elem = min(chain)

    print(chain_length, chain_smallest_elem)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**6)
    args = parser.parse_args()

    t = time.time()

    main(limit = args.limit)

    print(time.time() - t)