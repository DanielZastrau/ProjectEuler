def make_pyramid():
    I = []
    list_length = 1

    while L:
        I.append([])
        for c in range(list_length):
            I[-1].append(int(L[0]))
            del L[0]

        list_length = list_length + 1
    
    return I

def make_max(r_index, c_index):
    int1 = I[r_index][c_index] + I[r_index + 1][c_index]
    int2 = I[r_index][c_index] + I[r_index + 1][c_index + 1]
    return max(int1, int2)

def sink_pyramid():
    for row_index in range(len(I) - 2, -1, -1):
        for column_index in range(len(I[row_index])):
            I[row_index][column_index] = make_max(row_index, column_index)

        print(I[row_index])

# string = '''1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'''
# string = '''3 7 4 2 4 6 8 5 9 3'''
string = '''75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

L = string.strip().split(' ')
I = make_pyramid()
sink_pyramid()
print(I[0][0])