"""https://projecteuler.net/problem=102
Aug 26

228    0.004s    right
"""

import argparse
import sys
import os
import time
import math 
import itertools as it

class Vector2D():

    def __init__(self, x: int, y: int):

        self.x = x
        self.y = y

    def __sub__(self, other: Vector2D) -> Vector2D:
        """self - other"""

        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector2D) -> int:

        return self.x * other.x + self.y * other.y

    def rotate_clockwise_90(self) -> Vector2D:

        return Vector2D(self.y, -self.x)

    def roatate_counterclockwise_90(self) -> Vector2D:

        return Vector2D(-self.y, self.x)

    def rotate_180(self) -> Vector2D:

        return Vector2D(-self.x, -self.y)

def main():

    with open('../problem_data/p102_triangles.txt', 'r') as file:
        data = file.readlines()

    amount = 0
    for line in data:
        l = list(map(lambda x: int(x), line.strip().split(',')))
        p1, p2, p3 = l[:2], l[2: 4], l[4:]
        v1, v2, v3 = Vector2D(p1[0], p1[1]), Vector2D(p2[0], p2[1]), Vector2D(p3[0], p3[1])

        hyperplane1 = (v1 - v2).rotate_clockwise_90()
        b1 = hyperplane1 * v1
        if hyperplane1 * v3 > b1:
            hyperplane1 = hyperplane1.rotate_180()
            b1 = -b1

        hyperplane2 = (v1 - v3).rotate_clockwise_90()
        b2 = hyperplane2 * v1
        if hyperplane2 * v2 > b2:
            hyperplane2 = hyperplane2.rotate_180()
            b2 = -b2

        hyperplane3 = (v2 - v3).rotate_clockwise_90()
        b3 = hyperplane3 * v2
        if hyperplane3 * v1 > b3:
            hyperplane3 = hyperplane3.rotate_180()
            b3 = -b3

        #! now every valid point should be of the form Ax <= b
        origin = Vector2D(0, 0)
        if hyperplane1 * origin <= b1 and hyperplane2 * origin <= b2 and hyperplane3 * origin <= b3:
            amount += 1

    print(amount)

if __name__=='__main__':

    t = time.time()

    main()

    print(time.time() - t)