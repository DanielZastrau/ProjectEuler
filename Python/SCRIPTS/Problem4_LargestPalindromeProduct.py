"""https://projecteuler.net/problem=4"""

if __name__=="__main__":
    from time import time, sleep
    from Package import palindrome

    t = time()

    max_ = 0

    for a in range(999, 99, -1):
        if a%11 == 0:
            for b in range(999, a - 1, -1):
                number = a * b
                if number <= max_:
                    break

                if palindrome(number):
                    max_ = number

        else:
            for b in range(990, 99, -11):
                number = a * b
                if number <= max_:
                    break

                if palindrome(number):
                    max_ = number
    print(max_)

    print(time() - t)