"""https://projecteuler.net/problem=96

24702    1.8s
"""

import sys
import os
import argparse
import math
import copy
import itertools as it
import time

characters = '1,2,3,4,5,6,7,8,9,0'.split(',')
integers = set(range(1, 10))
triples = [(0, 3), (3, 6), (6, 9)]
ranges = list(it.product(triples, repeat=2))

def print_sudoku(sudoku: list[list[int]]):

    for row_id in range(9):
        if row_id % 3 == 0:
            print()
        row = sudoku[row_id]
        print(str(row[:3]) + '        ' + str(row[3: 6]) + '        ' + str(row[6:]) )
    print()

def print_searchspace(searchspace: list[list[list[int]]]):

    for row_id in range(9):
        if row_id % 3 == 0:
            print()
        row = searchspace[row_id]
        print(str(row[:3]) + '        ' + str(row[3: 6]) + '        ' + str(row[6:]) )
    print()

def duplicate_elem(l: list[int]) -> bool:

    for i, char in enumerate(l):

        if char == 0:
            continue

        if char in l[i + 1:]:
            return True

    return False

def update_row_and_col(row: int, col: int) -> tuple[int, int]:
    r_id = row + 1
    c_id = col

    if r_id == 9:
        r_id = 0
        c_id += 1

    return r_id, c_id

def get_searchspace(sudoku: list[list[int]]) -> list[list[list[int]]]:

    searchspace: list[list[list[int]]] = []
    for row_id in range(9):
        searchspace.append([])
        for col_id in range(9):
            searchspace[-1].append([])

            if sudoku[row_id][col_id] == 0:
                chars = integers - set(sudoku[row_id])
                chars = chars - set([row[col_id] for row in sudoku])

                l: list[int] = []
                for row_range, col_range in ranges:
                    if row_range[0] <= row_id < row_range[1] \
                            and col_range[0] <= col_id < col_range[1]:
                        
                        for r_id in range(row_range[0], row_range[1]):
                            l.extend(sudoku[r_id][col_range[0] : col_range[1]])
                        break
                
                chars = chars - set(l)

                searchspace[-1][-1].extend(list(chars))

    return searchspace

def update_searchspace(
        searchspace: list[list[list[int]]], rid: int, cid: int, v: int
    ) -> list[list[list[int]]]:

    new_searchspace = copy.deepcopy(searchspace)

    for col_id in range(9):
        if v in new_searchspace[rid][col_id]:
            new_searchspace[rid][col_id].remove(v)

    for row_id in range(9):
        if v in new_searchspace[row_id][cid]:
            new_searchspace[row_id][cid].remove(v)

    for row_range, col_range in ranges:

        if row_range[0] <= rid < row_range[1] \
                and col_range[0] <= cid < col_range[1]:

            for row_id in range(row_range[0], row_range[1]):
                for col_id in range(col_range[0], col_range[1]):

                    if v in new_searchspace[row_id][col_id]:
                        new_searchspace[row_id][col_id].remove(v)

    return new_searchspace

def any_searchspace_left(searchspace: list[list[list[int]]]) -> bool:

    out = False

    for row in searchspace:
        for col in row:

            if col:
                out = True

    return out

def insert_singleton_cells(
        sudoku: list[list[int]], searchspace: list[list[list[int]]]
    ) -> tuple[list[list[int]] ,list[list[list[int]]], bool]:

    change = False
    while True:

        changed_sth = False
        for row_id in range(9):
            for col_id in range(9):

                if len(searchspace[row_id][col_id]) == 1:
                    sudoku[row_id][col_id] = searchspace[row_id][col_id][0]

                    changed_sth = True
                    change = True

        if not changed_sth:
            break

        searchspace = get_searchspace(sudoku)

    return sudoku, searchspace, change

def insert_singleton_value_in_row(
        sudoku: list[list[int]], searchspace: list[list[list[int]]]
) -> tuple[list[list[int]], list[list[list[int]]], bool]:

    change = False

    while True:

        changed_sth = False
        for row_id in range(9):

            for integer in integers:
                indeces: list[int] = []

                for col_id in range(9):
                    if integer in searchspace[row_id][col_id]:
                        indeces.append(col_id)

                if len(indeces) == 1:
                    sudoku[row_id][indeces[0]] = integer

                    changed_sth = True
                    change = True

        if not changed_sth:
            break

        searchspace = get_searchspace(sudoku)

    return sudoku, searchspace, change


def insert_singleton_value_in_col(
        sudoku: list[list[int]], searchspace: list[list[list[int]]]
) -> tuple[list[list[int]], list[list[list[int]]], bool]:

    change = False

    while True:

        changed_sth = False
        for col_id in range(9):

            for integer in integers:
                indeces: list[int] = []

                for row_id in range(9):
                    if integer in searchspace[row_id][col_id]:
                        indeces.append(row_id)

                if len(indeces) == 1:
                    sudoku[indeces[0]][col_id] = integer

                    changed_sth = True
                    change = True

        if not changed_sth:
            break

        searchspace = get_searchspace(sudoku)

    return sudoku, searchspace, change

def recursively_solve(
        sudoku: list[list[int]], searchspace: list[list[list[int]]],
        row_id: int = 0, col_id: int = 0
    ) -> tuple[str, int]:

    # print_sudoku(sudoku)
    # time.sleep(1)

    if row_id == 8 and col_id == 8:
        num = 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]
        return 'solved', num

    if sudoku[row_id][col_id] == 0:
        new_sudoku = copy.deepcopy(sudoku)

        for char in searchspace[row_id][col_id]:
            new_sudoku[row_id][col_id] = char
            new_searchspace = update_searchspace(searchspace, row_id, col_id, char)
            row, col = update_row_and_col(row_id, col_id)
            outcome, num = recursively_solve(new_sudoku, new_searchspace, row, col)

            if outcome == 'solved':
                return 'solved', num

        return 'failed', -1

    else:
        r_id, c_id = update_row_and_col(row_id, col_id)
        return recursively_solve(sudoku, searchspace, r_id, c_id)

def main():

    with open('../problem_data/p096_sudoku.txt', 'r') as file:
        data = file.readlines()

    sudokus: list[list[list[int]]] = []
    for line in data:

        if line[0] in characters:
            sudokus[-1].append([int(char) for char in line.strip()])

        else:
            sudokus.append([])

    s = 0
    for i, sudoku in enumerate(sudokus):
        print(i)

        searchspace = get_searchspace(sudoku)
        # print_searchspace(searchspace)

        change = True
        while change:
            sudoku, searchspace, change_one = insert_singleton_cells(sudoku, searchspace)
            sudoku, searchspace, change_two = insert_singleton_value_in_row(sudoku ,searchspace)
            sudoku, searchspace, change_thr = insert_singleton_value_in_col(sudoku, searchspace)

            change = change_one or change_two or change_thr

        if any_searchspace_left(searchspace):
            _, num = recursively_solve(sudoku, searchspace)

        else:
            num = 100 * sudoku[0][0] + 10 * sudoku[0][1] + 1 * sudoku[0][2]

        s += num

    print(s)

if __name__=='__main__':

    t = time.time()

    main()

    print(time.time() -t )