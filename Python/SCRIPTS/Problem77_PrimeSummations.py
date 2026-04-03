"""https://projecteuler.net/problem=77"""

if __name__=="__main__":
    from time import time, sleep
    from Constants import primes_up_to_10to

    def recursion(n, Tmp, index):
        if n == 0:
            global ways
            ways += 1
            return 0
        elif n > 0:
            for i in range(index, len(Tmp)):
                prime = Tmp[i]
                res = recursion(n - prime, Tmp, i)
                if res == 0:
                    break

    t = time()

    Primes = primes_up_to_10to(4)

    n = 50
    while True:
        Tmp = [prime for prime in Primes if prime < n]
        ways = 0
        recursion(n, Tmp, 0)

        print(n, ways)

        if ways >= 5000:
            break

        n += 1

    print(time() - t)