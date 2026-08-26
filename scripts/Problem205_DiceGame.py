"""https://projecteuler.net/problem=205
Aug 26
0.5731440767829787    0.0748s    correct
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

def main(amountfour: int = 9, amountsix: int = 6):

    amount_of_dice_four = amountfour
    amount_of_dice_six = amountsix

    four_sided_dice = [1, 2, 3, 4]
    six_sided_dice = [1, 2, 3, 4, 5, 6]

    outcomes_four = list(map(sum, it.product(four_sided_dice, repeat=amount_of_dice_four)))
    outcomes_six = list(map(sum, it.product(six_sided_dice, repeat=amount_of_dice_six)))

    p_outcome_four = 1 / len(outcomes_four)
    p_outcome_six = 1 / len(outcomes_six)

    print(time.time() - t)

    outcome_counts_four: dict[int, int] = {
        outcome : outcomes_four.count(outcome) for outcome in set(outcomes_four)
    }
    outcome_counts_six: dict[int, int] = {
        outcome: outcomes_six.count(outcome) for outcome in set(outcomes_six)
    }

    print(time.time() - t)

    p_total = 0
    for outcome_six, count_six in outcome_counts_six.items():

        p = 0
        for outcome_four, count_four in outcome_counts_four.items():
            if outcome_four > outcome_six:
                p += count_four * p_outcome_four
        p_total += count_six * p_outcome_six * p
    print(f'Total probability that pyrimidal pete wins: {p_total}')

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--amountfour', type=int, default=9)
    parser.add_argument('--amountsix', type=int, default=6)
    args = parser.parse_args()

    t = time.time()
    main(amountfour=args.amountfour, amountsix=args.amountsix)
    print(time.time() - t)