"""https://projecteuler.net/problem=107
Sep 26
259679  16ms
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op
import fractions as fr
import heapq

from typing import Iterator

import commons

def test_matrix():
    return [[0, 16, 12, 21, 0, 0, 0],
            [16, 0, 0, 17, 20, 0, 0],
            [12, 0, 0, 28, 0, 31, 0],
            [21, 17, 28, 0, 18, 19, 23],
            [0, 20, 0, 18, 0, 0, 11],
            [0, 0, 31, 19, 0, 0, 27],
            [0, 0, 0, 23, 11, 27, 0]]

def main(test: bool):

    if not test:
        with open('./problem_data/0107_network.txt', 'r', encoding='utf-8') as file:
            data = file.read()

        data = [string.split(',') for string in data.split('\n')][:-1]
        matrix: list[list[int]] = [[int(elem) if elem != '-' else 0 for elem in row] for row in data]

    else:
        matrix = test_matrix()

    total_edge_weight = sum([sum(row) for row in matrix]) // 2
    print(total_edge_weight)

    mst: list[list[int]] =  [[0 for _ in row] for row in matrix]
    tree_nodes = [0]

    while len(tree_nodes) != len(matrix):
        minimum_edge_weight = 10**10
        corresp_source_node = -1
        corresp_target_node = -1

        for source_node in tree_nodes:
            for target_node in range(len(matrix[source_node])):
                if target_node in tree_nodes:
                    continue

                if matrix[source_node][target_node] == 0:
                    continue

                if matrix[source_node][target_node] < minimum_edge_weight:
                    minimum_edge_weight = matrix[source_node][target_node]
                    corresp_source_node = source_node
                    corresp_target_node = target_node

        mst[corresp_source_node][corresp_target_node] = minimum_edge_weight
        mst[corresp_target_node][corresp_source_node] = minimum_edge_weight
        tree_nodes.append(corresp_target_node)

    print('\n'.join([str(row) for row in mst]))
    print(tree_nodes)
    print(total_edge_weight - sum([sum(row) for row in mst]) // 2)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    t = time.time()
    main(test=args.test)
    print(time.time() - t)