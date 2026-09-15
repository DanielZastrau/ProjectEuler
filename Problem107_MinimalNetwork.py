"""https://projecteuler.net/problem=107
Sep 26
259679  2ms
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

    n = len(matrix)
    total_edge_weight = sum([sum(row) for row in matrix]) // 2

    mst: list[list[int]] =  [[0 for _ in row] for row in matrix]
    tree_nodes = [0]
    visited = [False] * n
    visited[0] = True

    # (weight, source, target)
    heap: list[tuple[int, int, int]] = []
    for target_node, weight in enumerate(matrix[0]):
        if weight > 0:
            heapq.heappush(heap, (weight, 0, target_node))

    while heap and len(tree_nodes) < n:

        weight, source, target = heapq.heappop(heap)
        print(weight, source, target)
        if visited[target]:
            continue

        mst[source][target] = weight
        mst[target][source] = weight
        tree_nodes.append(target)
        visited[target] = True

        for next_target, weight in enumerate(matrix[target]):
            if weight > 0 and not visited[next_target]:
                heapq.heappush(heap, (weight, target, next_target))

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