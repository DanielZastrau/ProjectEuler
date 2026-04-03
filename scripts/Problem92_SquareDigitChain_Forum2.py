from time import perf_counter

def main():

    def sum_square_digits(n):
        sum_ = 0
        for i in map(int, str(n)):
            sum_ += i * i
        return sum_

    def search(n):
        if eighty_nine[n] is NOT_VISITED:
            eighty_nine[n] = search(sum_square_digits(n))
        return eighty_nine[n]

    LIM = 10_000_000
    NOT_VISITED = -1
    eighty_nine = [NOT_VISITED] * LIM
    eighty_nine[89] = True
    eighty_nine[1] = False
    eighty_nine[0] = False
    for n in range(2, LIM):
        search(n)
    print(sum(eighty_nine))

tick = perf_counter()
main()
tock = perf_counter()
print(f'Execution time: {(tock - tick):.4} s.')