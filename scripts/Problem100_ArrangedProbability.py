"""https://projecteuler.net/problem=100
Aug 26

"""

import os
import sys 
import argparse 
import time
import math
import itertools as it

def generate_solutions(num_solutions: int = 20):
    x, y = 1, 1    # Fundamental solution to the Pell equation
    
    for sol_id in range(num_solutions):

        # Map x, y back to m, n
        m = (y + 1) // 2
        n = (x + 1) // 2

        if sol_id % 2 == 0:
            yield m, n
        
        # Calculate the next (x, y) solution pair, but only every second one is one we need
        x, y = x + 2 * y, x + y

if __name__=='__main__':
    t = time.time()

    # Generate and print the first 10 solutions
    for index, (m, n) in enumerate(generate_solutions(40), start=1):
        print(f"Solution {index}: m = {m:<6} n = {n}")
    
    print(time.time() - t)