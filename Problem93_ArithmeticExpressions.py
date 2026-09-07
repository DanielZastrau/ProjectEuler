"""https://projecteuler.net/problem=93

    [14.08.26]
        Searchspace=10    ~  18 seconds
        Searchspace=20    ~ 460 seconds
            Calculating all possible combinations of
                    numbers in the searchspace
                    orders of those numbers
                    choices of operators
                    positions of brackets
                    then constructing the term
                    then evaluating it
                    
    [14.08.26]
        Searchspace=10    ~   0.09  seconds    improvement factor=200x
        Searchspace=20    ~   2.16  seconds    improvement factor=212x
        Searchspace=30    ~  13.67  seconds
        Searchspace=40    ~  48.80  seconds
        Searchspace=50    ~ 132.34  seconds
        Searchspace=60    ~ 234.67  seconds
            Calculating all possible combinations of
                    numbers in the searchspace
                    orders of those numbers
                    orders of operators
                    and then just evaluating left to right
            Also cutting out the printing every new n3.
                    
            This acknowledges that it would compute each
            possible combination with the brackets
    

            Different length calculation at the end.
            Now, explicitely going up the numbers and breaking
                    on the first, which breaks.
            Previously,     diffs = [l[i] - l[i - 1] for i in range(1, len(l))]
                            l = list(itertools.filterfalse(lambda x: x != 1, diffs))
                    This was wrong, an unbroken sequence 2 to n would have also counted.
            

            This current left to right solving works for all operations except for divisions.
                    Also it does not work for multiplication (a + b) x (c + d) has no order
                    in which it translates to pure left to right solving.

    [14.08.26]
        Added bracketing in again, doing all cases manually.
        Moved calculation of brackets and operator orders outside of main loops,
                to avoid recalculating the same static entity millions of times.

        Searchspace=10    ~  16.18  seconds    >    1 2 5 8 51
        Searchspace=20    ~ 495.08  seconds    >    1 2 5 8 51

        SOLVED
    """

import argparse
import math
import itertools as it
import time

def disjoint(pair: tuple[tuple[int, int], tuple[int, int]]) -> bool:

    opening_pos_2 = pair[1][0]
    closing_pos_1 = pair[0][1]

    #! disjoint?
    if closing_pos_1 < opening_pos_2:
        return True

    return False


def contained(pair: tuple[tuple[int, int], tuple[int, int]]) -> bool:

    opening_pos_1 = pair[0][0]
    opening_pos_2 = pair[1][0]

    closing_pos_1 = pair[0][1]
    closing_pos_2 = pair[1][1]

    #! not equal
    if opening_pos_1 == opening_pos_2 and closing_pos_1 == closing_pos_2:
        return False

    #! contained?
    if opening_pos_2 >= opening_pos_1 and closing_pos_2 <= closing_pos_1:
        return True

    return False

def evaluate(sequence: list[float], operators: list[str]) -> float:

    count_point_operations = operators.count('*') + operators.count('/')

    for _ in range(count_point_operations):
        for i, op in enumerate(operators):
            if op in ['*', '/']:
                e1 = sequence[i]
                e2 = sequence[i + 1]

                if op == '*':
                    value = e1 * e2

                else:    # op == '/'
                    if e2 == 0:
                        return -10_000
                    value = e1 / e2

                sequence = sequence[: i] + [value] + sequence[i + 2: ]
                operators.remove(op)
                break

    for _ in range(3 - count_point_operations):
        for i, op in enumerate(operators):
            if op in ['+', '-']:
                e1 = sequence[i]
                e2 = sequence[i + 1]

                if op == '+':
                    value = e1 + e2

                else:    # op == '-'
                    value = e1 - e2

                sequence = sequence[: i] + [value] + sequence[i + 2: ]
                operators.remove(op)
                break
        
    return sequence[0]

def calculate_sequence_length(n1: int, n2: int, n3: int, n4: int) -> tuple[int, list[float]]:

    numbers = [n1, n2, n3, n4]
    orders_of_numbers = it.permutations(numbers)

    integer_values: set[float] = set()
    for on in orders_of_numbers:
        for oo in orders_of_operators:

            for bracket in singles:

                if bracket == (0, 1):
                    term1 = evaluate(sequence=[on[0], on[1]], operators=[oo[0]])
                    n = evaluate(sequence=[term1, on[2], on[3]], operators=[oo[1], oo[2]])
                    
                elif bracket == (0, 2):
                    term1 = evaluate(sequence=[on[0], on[1], on[2]], operators=[oo[0], oo[1]])
                    n = evaluate(sequence=[term1, on[3]], operators=[oo[2]])

                elif bracket == (0, 3):
                    n = evaluate(sequence=list(on), operators=list(oo))

                elif bracket == (1, 2):
                    term1 = evaluate(sequence=[on[1], on[2]], operators=[oo[1]])
                    n = evaluate(sequence=[on[0], term1, on[3]], operators=[oo[0], oo[2]])

                elif bracket == (1, 3):
                    term1 = evaluate(sequence=[on[1], on[2], on[3]], operators=[oo[1], oo[2]])
                    n = evaluate(sequence=[on[0], term1], operators=[oo[0]])

                elif bracket == (2, 3):
                    term1 = evaluate(sequence=[on[2], on[3]], operators=[oo[2]])
                    n = evaluate(sequence=[on[0], on[1], term1], operators=[oo[0], oo[1]])

            for pair in doubles_disjoint:
                term1 = evaluate(sequence=[on[0], on[1]], operators=[oo[0]])
                term2 = evaluate(sequence=[on[2], on[3]], operators=[oo[2]])
                n = evaluate(sequence=[term1, term2], operators=[oo[1]])

            for pair in doubles_contained:
                opening_pos_1 = pair[0][0]
                opening_pos_2 = pair[1][0]

                if opening_pos_1 == 0:    # 0,2

                    if opening_pos_2 == 0:    # 0,1
                        term1 = evaluate(sequence=[on[0], on[1]], operators=[oo[0]])
                        term2 = evaluate(sequence=[term1, on[2]], operators=[oo[1]])
                        n = evaluate(sequence=[term2, on[3]], operators=[oo[2]])

                    else:    # 1,2
                        term1 = evaluate(sequence=[on[1], on[2]], operators=[oo[1]])
                        term2 = evaluate(sequence=[on[0], term1], operators=[oo[0]])
                        n = evaluate(sequence=[term2, on[3]], operators=[oo[2]])

                else:    # 1,3

                    if opening_pos_2 == 1:    # 1,2
                        term1 = evaluate(sequence=[on[1], on[2]], operators=[oo[1]])
                        term2 = evaluate(sequence=[term1, on[3]], operators=[oo[2]])
                        n = evaluate(sequence=[on[0], term2], operators=[oo[0]])

                    else:    # 2,3
                        term1 = evaluate(sequence=[on[2], on[3]], operators=[oo[2]])
                        term2 = evaluate(sequence=[on[1], term1], operators=[oo[1]])
                        n = evaluate(sequence=[on[0], term2], operators=[oo[0]])

                #! OPEN
                integer_values.add(n)

    if not 1 in integer_values:
        return 0, [0.0]

    l = sorted(list(it.filterfalse(lambda x: x < 1 or x % 1 != 0, integer_values)))

    index = 0
    while l[index] == index + 1:
        index += 1

    return index, l

def find_longest_sequence(searchspace: int):

    max_sequence_length = 0

    for n1 in range(1, searchspace):
        for n2 in range(n1 + 1, searchspace):
            print(n2)
            for n3 in range(n2 + 1, searchspace):
                for n4 in range(n3 + 1, searchspace):
                    length, l = calculate_sequence_length(n1, n2, n3, n4)

                    if length > max_sequence_length:
                        max_sequence_length = length
                        print(l)

                        print('---------------------', max_sequence_length, n1, n2, n3, n4)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--searchspace', type=int, default=50)
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    #! Calculate bracket pairings once
    singles: list[tuple[int, int]] = [(i, j) for i in range(4) for j in range(i + 1, 4)]

    intermediate = singles.copy()
    intermediate.remove((0,3))

    doubles_disjoint = list(it.filterfalse(lambda x: not disjoint(pair=x), it.product(singles, singles)))
    doubles_contained = list(it.filterfalse(lambda x: not contained(pair=x), it.product(singles, singles)))

    #! Calculate operator list once
    operators = '+,-,*,/'.split(',')
    orders_of_operators = list(it.product(operators, repeat=3))

    if args.test:
        print(calculate_sequence_length(1, 2, 3, 4))

    else:
        t = time.time()

        find_longest_sequence(searchspace = args.searchspace)

        print(f'It took {time.time() - t}  seconds')