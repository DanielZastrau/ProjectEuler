"""https://projecteuler.net/problem=98

80 514 729    47.806    wrong
     9 216     6.247    wrong
    18 769     7.803    right
"""

import sys
import os
import time
import argparse
import math 
import itertools as it

def main():

    with open('../problem_data/p098_words.txt', 'r') as file:
        data = file.readlines()[0]

    words = list(map(lambda x: x.strip('"'), data.split(',')))
    M = len(max(words, key=lambda x: len(x)))
    print(M)
    integers = list(range(0, 10))

    combinations_d = {length : list(it.permutations(integers, r=length)) for length in range(M)}

    anagram_pairs: list[tuple[str, str]] = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):

            w1 = words[i]
            w2 = words[j]

            if len(w1) != len(w2):
                continue

            if sorted(w1) == sorted(w2):
                anagram_pairs.append((w1, w2))
    print(len(anagram_pairs))

    anagram_square_pairs: list[tuple[int, int]] = []
    for w1, w2 in anagram_pairs:

        unique_letters_w1 = []
        unique_letters_w1 = [letter for letter in w1 if not letter in unique_letters_w1]
        l = len(unique_letters_w1)

        for combination in combinations_d[l]:

            mapping = {unique_letters_w1[i]: combination[i] for i in range(l)}

            # Digital assignements may not start with zero
            if mapping[w1[0]] == 0 or mapping[w2[0]] == 0:
                continue

            # Square numbers can only end in those
            if mapping[w1[-1]] not in [1, 4, 5, 6, 9] or mapping[w2[-1]] not in [1, 4, 5, 6, 9]:
                continue

            n1 = 0
            for power in range(l):
                n1 += 10**power * mapping[w1[-(power + 1)]]

            n2 = 0
            for power in range(l):
                n2 += 10**power * mapping[w2[-(power + 1)]]

            if math.isqrt(n1)**2 == n1 and math.isqrt(n2)**2 == n2:
                print(w1, n1, w2, n2)
                anagram_square_pairs.append((n1, n2))
    print(len(anagram_square_pairs))

    maximum = 0
    for n1, n2 in anagram_square_pairs:

        if n1 > maximum:
            maximum = n1

        if n2 > maximum:
            maximum = n2
    print(maximum)


if __name__ == '__main__':

    t = time.time()

    main()

    print(time.time() - t)