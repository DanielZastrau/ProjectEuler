"""https://projecteuler.net/problem=42
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import Commons

def main():

    words = []
    with open('./problem_data/p042_words.txt', 'r') as file:
        for line in file:
            words = [elem.strip('"') for elem in line.split(',')]

    mapping: dict[str, int] = {}
    chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    for index, char in enumerate(chars):
        mapping[char] = index + 1

    nums = [int(0.5 * n * (n + 1)) for n in range(1, 100)]

    c = 0
    for word in words:
        num_value = 0
        for letter in word:
            num_value += mapping[letter.lower()]
        
        if num_value in nums:
            print(word)
            c += 1
    print(c)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)