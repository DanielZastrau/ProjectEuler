"""https://projecteuler.net/problem=93"""

import itertools

def evaluate(sequence: list[str]) -> float:
    """evaluates a string 4 x (3 + 1 / 2).
    
    Bracket before anything
    division and multiplication before sums and differences."""

    # ! Evaluates any bracketed term
    if '(' in sequence:
        for i, char in enumerate(sequence):
            if char == '(':

                #! Find closing bracket
                last_index: int = i + 1
                for j, charr in enumerate(sequence[i:]):

                    if charr == ')':
                        last_index = i + j
                bracket_value = evaluate(sequence[i + 1: last_index])
                sequence = sequence[: i] + [str(bracket_value)] + sequence[last_index + 1 : ]
                break

    # ! Evaluates multiplications and divisions left to right
    for _ in range(2):
        for i, e in enumerate(sequence):

            if e == 'x' or e == '/':
                if e == 'x':
                    v = float(sequence[i-1]) * float(sequence[i+1])

                else:    # e == '/':

                    if float(sequence[i+1]) == 0:
                        return -10_000
                    
                    v = float(sequence[i-1]) / float(sequence[i+1])

                sequence = sequence[ : i-1] + [str(v)] + sequence[ i+2 : ]
                break

    for _ in range(2):
        for i, e in enumerate(sequence):

            if e == '+' or e == '-':
                if e == '+':
                    v = float(sequence[i-1]) + float(sequence[i+1])

                else:    # e == '-':
                    v = float(sequence[i-1]) - float(sequence[i+1])

                sequence = sequence[ : i-1] + [str(v)] + sequence[ i+2 : ]
                break

    return float(sequence[0])

def calculate_sequence_length(n1: str, n2: str, n3: str, n4: str):

    digits = '0,1,2,3,4,5,6,7,8,9'.split(',')
    numbers = [n1, n2, n3, n4]
    operators = '+,-,x,/'.split(',')
    integer_values: set[int] = set()

    A: list[tuple[int, int]] = []
    for i in range(3):
        for j in range(i, 5):

            if j - i == 1 or j - i == 4:
                continue

            A.append((i,j))
    A = list(itertools.filterfalse(lambda x: x[0] == x[1], A))

    B = itertools.product(A, A)
    B = itertools.filterfalse(lambda x: not (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]), B)
    B = itertools.filterfalse(lambda x: x[0] == x[1], B)
    B = list(B)

    positions_of_brackets = [()] + A + B

    orders_of_numbers = itertools.permutations(numbers)
    orders_of_operators = list(itertools.product(operators, repeat=3))

    for order_n in orders_of_numbers:
        for position_of_brackets in positions_of_brackets:
            for oo in orders_of_operators:
                sequence = list(order_n)

                if position_of_brackets == ():
                    pass

                elif isinstance(position_of_brackets[0], int):

                    position_of_brackets: tuple[int, int]

                    first_bracket_index = position_of_brackets[0]
                    second_bracket_index = position_of_brackets[1]

                    sequence = sequence[:first_bracket_index] + ['('] + sequence[first_bracket_index:]
                    sequence = sequence[:second_bracket_index + 1] + [')'] + sequence[second_bracket_index + 1:]

                elif isinstance(position_of_brackets[0], tuple):

                    position_of_brackets: tuple[tuple[int, int], tuple[int, int]]
                    first_bracket_pair: tuple[int, int]
                    second_bracket_pair: tuple[int, int]
                    first_bracket_pair, second_bracket_pair = position_of_brackets

                    bracket_11: int = first_bracket_pair[0]
                    bracket_12: int = first_bracket_pair[1]
                    bracket_21: int = second_bracket_pair[0]
                    bracket_22: int = second_bracket_pair[1]

                    sequence = sequence[:bracket_11] + ['('] + sequence[bracket_11:]
                    sequence = sequence[:bracket_21 + 1] + ['('] + sequence[bracket_21 + 1:]
                    sequence = sequence[:bracket_22 + 2] + [')'] + sequence[bracket_22 + 2:]
                    sequence = sequence[:bracket_12 + 3] + [')'] + sequence[bracket_12 + 3:]

                s = []
                last_char = ''
                curr_op_i = 0
                for char in sequence:

                    if last_char in digits and char == '(':
                        s += [oo[curr_op_i]]
                        curr_op_i += 1

                    elif last_char == ')' and char in digits:
                        s += [oo[curr_op_i]]
                        curr_op_i += 1

                    elif last_char in digits and char in digits:
                        s += [oo[curr_op_i]]
                        curr_op_i += 1

                    s += [char]

                    last_char = char

                n = evaluate(s)

                if n % 1.0 == 0:
                    integer_values.add(int(n))

    l = sorted(list(itertools.filterfalse(lambda x: x < 1, integer_values)))
    diffs = [l[i] - l[i - 1] for i in range(1, len(l))]
    l = list(itertools.filterfalse(lambda x: x != 1, diffs))

    return len(l) + 1

def find_longest_sequence(searchspace: int):

    max_sequence_length = 0

    for n1 in range(1, searchspace):
        for n2 in range(n1 + 1, searchspace):
            for n3 in range(n2 + 1, searchspace):
                print(n1, n2, n3)
                for n4 in range(n3 + 1, searchspace):
                    length = calculate_sequence_length(str(n1), str(n2), str(n3), str(n4))

                    if length > max_sequence_length:
                        max_sequence_length = length

                        print('---------------------', max_sequence_length, n1, n2, n3, n4)

if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--searchspace', type=int, default=50)
    args = parser.parse_args()

    find_longest_sequence(searchspace = args.searchspace)