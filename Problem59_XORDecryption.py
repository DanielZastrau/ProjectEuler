"""https://projecteuler.net/problem=59
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def main():

    line_clean: list[int] = []
    with open('./problem_data/p059_cipher.txt', 'r') as file:
        for line in file:
            line_clean.extend([ int(elem) for elem in line.strip().split(',') ])

    for n1 in range(97, 123):
        for n2 in range(97, 123):
            for n3 in range(97, 123):
                values = [n1, n2, n3]
                key_text: list[int] = []
                letter = 0

                for _ in range(len(line_clean)):
                    key_text.append(values[letter])
                    letter = (letter + 1) % 3

                Text = [chr(line_clean[i] ^ key_text[i]) for i in range(len(line_clean))]
                Text = ''.join( Text )
                
                if Text.startswith('An extract taken from'):
                    Text = [ ord(elem) for elem in Text ]
                    print(sum(Text))
                    return
                

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)