"""https://projecteuler.net/problem=82"""

if __name__=="__main__":
    from time import time, sleep

    def gen_paths(col1, col2, i, length):
        Paths = list()
        for j in range(length):
            if j == i:
                Paths.append([col1[j], col2[j]])
            elif j < i:
                path = [col1[i]]
                for k in range(i -1, j -1, -1):
                    path.append(col1[k])
                path.append(col2[j])
                Paths.append(path)
            elif j > i:
                path = [col1[i]]
                for k in range(i +1, j +1):
                    path.append(col1[k])
                path.append(col2[j])
                Paths.append(path)
        return Paths


    def reduce_(col1, col2):
        length = len(col1)
        new_col = []
        for i in range(length):
            Paths = gen_paths(col1, col2, i, length)
            Path_sums = [sum(path) for path in Paths]
            min_ = min(Path_sums)
            new_col.append(min_)
        return new_col

    t = time()

    # store matrix row by row
    Matrix = list()
    with open('p082_matrix.txt', 'r') as file:
        for line in file:
            Matrix.append([])
            for num in [ int(e) for e in line.strip().split(',') ]:
                Matrix[-1].append(num)
    length = len(Matrix)

    # transpose matrix to store it column by column
    Tmp = [[ 0 for _ in range(length) ] for _ in range(length) ]
    for i in range(length):
        Tmp[i] = [ row[i] for row in Matrix ]
    Matrix = Tmp

    for col in range(length -1, 0, -1):
        col1 = Matrix[col -1]
        col2 = Matrix[col]

        Matrix[col -1] = reduce_(col1, col2)
    print(min(Matrix[0]))

    print(time() - t)