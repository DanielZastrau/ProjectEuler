"""https://projecteuler.net/problem=206"""

from time import time, sleep

if __name__=="__main__":
    t = time()

    for i in range(10**9 + 10, 2 * 10**9, 20):
        sq = str(i**2)
        if sq[0] == '1':
            if sq[2] == '2' and sq[4] == '3' and sq[6] == '4' \
                    and sq[8] == '5' and sq[10] == '6' and sq[12] == '7' and sq[14] == '8' \
                    and sq[16] == '9' and sq[18] == '0':
                print(i, sq)
                sleep(1)
        else:
            break

    print(time() - t)