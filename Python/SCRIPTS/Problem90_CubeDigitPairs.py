"""https://projecteuler.net/problem=90"""

from itertools import combinations, product

squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]

dices = list(combinations(range(10), 6))

count = 0

for index_one in range(len(dices)):
    for index_two in range(index_one +1, len(dices)):
        dice_one = dices[index_one]
        dice_two = dices[index_two]

        number_pairs = []

        for digit_one in dice_one:
            for digit_two in dice_two:

                if digit_one == 6:
                    number_pairs.append((9, digit_two))
                    number_pairs.append((digit_two, 9))

                if digit_one == 9:
                    number_pairs.append((6, digit_two))
                    number_pairs.append((digit_two, 6))

                if digit_two == 6:
                    number_pairs.append((digit_one, 9))
                    number_pairs.append((9, digit_one))

                if digit_two == 9:
                    number_pairs.append((digit_one, 6))
                    number_pairs.append((6, digit_one))

                number_pairs.append((digit_one, digit_two))
                number_pairs.append((digit_two, digit_one))

        bool_ = True
        for square in squares:
            if square not in number_pairs:
                bool_ = False
                break
        if bool_:
            count += 1

print(count)