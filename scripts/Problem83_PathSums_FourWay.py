"""https://projecteuler.net/problem=83"""

if __name__=="__main__":
    from time import time, sleep

    class node:

        def __init__(self, value):
            self.value = value
            self.path_sum = float('inf')
            self.parent = None
            self.adj = list()

        def __repr__(self):
            return str(self.path_sum)

    def fill_adj(Nodes, length):
        for row in range(1, length -1):
            for col in range(1, length -1):
                Nodes[row][col].adj.append(Nodes[row -1][col])
                Nodes[row][col].adj.append(Nodes[row +1][col])
                Nodes[row][col].adj.append(Nodes[row][col -1])
                Nodes[row][col].adj.append(Nodes[row][col +1])

        for col in range(1, length -1):
            Nodes[0][col].adj.append(Nodes[0][col -1])
            Nodes[0][col].adj.append(Nodes[0][col +1])
            Nodes[0][col].adj.append(Nodes[0 +1][col])

            Nodes[length -1][col].adj.append(Nodes[length -1][col -1])
            Nodes[length -1][col].adj.append(Nodes[length -1][col +1])
            Nodes[length -1][col].adj.append(Nodes[length -1 -1][col])

        for row in range(1, length -1):
            Nodes[row][0].adj.append(Nodes[row -1][0])
            Nodes[row][0].adj.append(Nodes[row +1][0])
            Nodes[row][0].adj.append(Nodes[row][0 +1])

            Nodes[row][length -1].adj.append(Nodes[row -1][length -1])
            Nodes[row][length -1].adj.append(Nodes[row +1][length -1])
            Nodes[row][length -1].adj.append(Nodes[row][length -1 -1])

        Nodes[0][0].adj.append(Nodes[0][1])
        Nodes[0][0].adj.append(Nodes[1][0])

        Nodes[length -1][0].adj.append(Nodes[length -2][0])
        Nodes[length -1][0].adj.append(Nodes[length -1][1])

        Nodes[0][length -1].adj.append(Nodes[0][length -2])
        Nodes[0][length -1].adj.append(Nodes[1][length -1])

        Nodes[length -1][length -1].adj.append(Nodes[length -2][length -1])
        Nodes[length -1][length -1].adj.append(Nodes[length -1][length -2])

    def arg_min(Nodes):
        min_ = float('inf')
        min_obj = None
        for node_obj in Nodes:
            if node_obj.path_sum < min_:
                min_ = node_obj.path_sum
                min_obj = node_obj
        return min_obj

    def print_Nodes():
        global Nodes
        global length
        
        for row in Nodes:
            print(row)

    t = time()

    # store matrix row by row
    Matrix = list()
    with open('p083_matrix.txt', 'r') as file:
        for line in file:
            Matrix.append([int(e) for e in line.strip().split(',')])
    length = len(Matrix)

    # initialize node objects
    Nodes = list()
    for row in range(length):
        Nodes.append(list())
        for col in range(length):
            Nodes[-1].append(node(Matrix[row][col]))

    # initialize adjacency lists
    fill_adj(Nodes, length)
    
    # calc path sum
    Nodes[0][0].path_sum = Nodes[0][0].value
    
    Open = list()
    for row in Nodes:
        Open.extend(row)

    for _ in range(length**2):
        curr = arg_min(Open)
        Open.remove(curr)
        for node_obj in curr.adj:
            if curr.path_sum + node_obj.value < node_obj.path_sum:
                node_obj.path_sum = curr.path_sum + node_obj.value
                node_obj.parent = curr
    print(Nodes[length -1][length -1])

    print(time() - t)