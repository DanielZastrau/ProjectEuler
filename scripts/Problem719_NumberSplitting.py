"""https://projecteuler.net/problem=719
The answer for 10**4 would be 41_333, works
Currently 10**10 takes ~47seconds +- 5 to finish. And the factor for an additonal power of 10 is between 5 and 6.
Therefore the expected time for 10**12 right now would be between 20 and 30 minutes."""

from time import time

def cross_sum(n):

    integer_array = []

    s = 0
    while n > 0:
        last_digit = n % 10
        s += last_digit

        integer_array.append(last_digit)

        # This simply ensures, that we do not get any decimal points
        n = n - last_digit
        n = n // 10

    # Why do I reverse the array here?
    integer_array.reverse()

    return s, integer_array


def matching_splitting(n, ia_n_sq):

    amount_of_splits = 0
    while True:
        amount_of_splits += 1

        if matching_splitting_inner(n, ia_n_sq, amount_of_splits):
            return True

        if amount_of_splits == 5:
            break

    return False


def matching_splitting_inner(n, ia_n_sq, amount_of_splits):

    # print(f'amount of splits:  {amount_of_splits}')

    # lets say one split
    if amount_of_splits == 1:
        for index in range(1, len(ia_n_sq)):
            n_1_arr = ia_n_sq[: index]
            n_2_arr = ia_n_sq[index:]

            # print(n_1_arr)
            # print(n_2_arr)

            n_1 = int(''.join(map(str, n_1_arr)))
            n_2 = int(''.join(map(str, n_2_arr)))

            # print(n_1)
            # print(n_2)

            if n_1 + n_2 == n:
                return True

    elif amount_of_splits == 2:

        for index_one in range(1, len(ia_n_sq)):
            for index_two in range(index_one + 1, len(ia_n_sq)):
                n_1_arr = ia_n_sq[: index_one]
                n_2_arr = ia_n_sq[index_one: index_two]
                n_3_arr = ia_n_sq[index_two:]

                # print(n_1_arr)
                # print(n_2_arr)
                # print(n_3_arr)

                n_1 = int(''.join(map(str, n_1_arr)))
                n_2 = int(''.join(map(str, n_2_arr)))
                n_3 = int(''.join(map(str, n_3_arr)))

                # print(n_1)
                # print(n_2)
                # print(n_3)

                if n_1 + n_2 + n_3 == n:
                    return True

    elif amount_of_splits == 3:

        for index_one in range(1, len(ia_n_sq)):
            for index_two in range(index_one + 1, len(ia_n_sq)):
                for index_three in range(index_two + 1, len(ia_n_sq)):
                    n_1_arr = ia_n_sq[: index_one]
                    n_2_arr = ia_n_sq[index_one: index_two]
                    n_3_arr = ia_n_sq[index_two: index_three]
                    n_4_arr = ia_n_sq[index_three:]

                    n_1 = int(''.join(map(str, n_1_arr)))
                    n_2 = int(''.join(map(str, n_2_arr)))
                    n_3 = int(''.join(map(str, n_3_arr)))
                    n_4 = int(''.join(map(str, n_4_arr)))

                    if n_1 + n_2 + n_3 == n:
                        return True
                
    return False

def main(limit):

    total = 0

    n = 1
    n_sq = n**2
    while n_sq <= limit:

        cs_n, _ = cross_sum(n)
        cs_n_sq, ia_n_sq = cross_sum(n_sq)

        # print()
        # print(n)
        # print(n_sq)

        if not (cs_n_sq < cs_n):
            # print('checking')
            if matching_splitting(n, ia_n_sq):
                # print('matching')
                total += n_sq

                print(n)
                print(n_sq)

        n += 1
        n_sq = n**2

    return total

if __name__ == '__main__':
    
    limit = 10**4

    t_st = time()
    print(f'The total for the limit {limit} is:  {main(limit)}')
    t_end = time()

    print(f'It took {t_end - t_st} seconds to finish.')