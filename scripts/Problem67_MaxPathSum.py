"""https://projecteuler.net/problem=67"""

from time import time

def make_pyramid():

    for r_index in range(len(I)):
        for c_index in range(len(I[r_index])):
            I[r_index][c_index] = int(I[r_index][c_index])

def make_max(r_index, c_index):
    int1 = I[r_index][c_index] + I[r_index + 1][c_index]
    int2 = I[r_index][c_index] + I[r_index + 1][c_index + 1]
    return max(int1, int2)


def sink_pyramid():
    for row_index in range(len(I) - 2, -1, -1):
        for column_index in range(len(I[row_index])):
            I[row_index][column_index] = make_max(row_index, column_index)

        print(I[row_index])

with open('p067_triangle.txt', 'r') as file:
    I = []
    for line in file:
        I.append(line.strip().split(' '))

if __name__=="__main__":
    t = time()

    make_pyramid()
    sink_pyramid()

    print(I[0][0])
    print(time() - t)