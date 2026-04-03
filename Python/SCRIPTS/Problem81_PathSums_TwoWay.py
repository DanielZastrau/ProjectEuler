"""https://projecteuler.net/problem=81"""

if __name__=="__main__":
    from time import time, sleep

    class node:

        def __init__(self, value, index):
            self.value = value
            self.index = index
            self.parent1 = None
            self.parent2 = None

        def update_parent(self, node_obj):
            if self.parent1 is None:
                self.parent1 = node_obj
            elif self.parent2 is None:
                self.parent2 = node_obj
            else:
                print(self.index, 'trying to set a third parent...')

        def update_value(self):
            if self.parent1 is None and self.parent2 is None:
                print(self.index, 'that node has no parents')
            elif self.parent2 is None:
                self.value += self.parent1.value
            else:
                self.value += min(self.parent1.value, self.parent2.value)

    t = time()

    Matrix = list()
    with open('p081_matrix.txt', 'r') as file:
        for line in file:
            Matrix.append([])
            for num in [ int(e) for e in line.strip().split(',') ]:
                Matrix[-1].append(num)

    length = len(Matrix)

    Node_matrix = [[0]*length for _ in range(length)]
    for i in range(length):    # 80 * 80 loop iterations = 6 400 * (1 pointer setting + 1 initialization) ~ 12 800 operations 
        for j in range(length):
            Node_matrix[i][j] = node(Matrix[i][j], (i, j))

    for i in range(length):    # 80 * 80 loop iterations = 
        for j in range(length):    # 6 400 * (2 conditionals  + 2 function calls + 2 conditionals + 2 pointer settings)
            if i == 0 == j:            # ~ 51 200 operations
                continue
            else:
                if 0 <= j - 1:
                    Node_matrix[i][j].update_parent(Node_matrix[i][j - 1])
                if 0 <= i - 1:
                    Node_matrix[i][j].update_parent(Node_matrix[i - 1][j])

    for i in range(length):    # 80*(81)/2 loop iterations = 2 * (3 240 * (1 function call + 2 conditionals + 2 additions + 1 minimum))
        if i == 0:                 # ~ 38 880 operations
            continue
        for j in range(i + 1):
            Node_matrix[j][i - j].update_value()
    for i in range(length -2, -1, -1):
        for j in range(i + 1):
            Node_matrix[-(j + 1)][-(i - j + 1)].update_value()

    print(Node_matrix[-1][-1].value)


    print(time() - t)