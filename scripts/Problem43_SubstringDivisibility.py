"""
https://projecteuler.net/problem=43
"""
import time

def pd_num(string=''):
    global sum_

    if len(string) == 0:
        for i in range(1, 10):
            pd_num(''.join(['', str(i)]))

    elif len(string) == 4:
        check = string[1:]

        if int(check)%2 == 0:
            for i in range(1, 10):

                if str(i) not in string:
                    pd_num(''.join([string, str(i)]))

    elif len(string) == 5:
        check = string[2:]

        if int(check)%3 == 0:
            for i in range(1, 10):

                if str(i) not in string:
                    pd_num(''.join([string, str(i)]))

    elif len(string) == 6:
        check = string[3:]

        if int(check)%5 == 0:
            for i in range(1, 10):

                if str(i) not in string:
                    pd_num(''.join([string, str(i)]))

    elif len(string) == 7:
        check = string[4:]

        if int(check)%7 == 0:
            for i in range(1, 10):

                if str(i) not in string:
                    pd_num(''.join([string, str(i)]))

    elif len(string) == 8:
        check = string[5:]

        if int(check)%11 == 0:
            for i in range(1, 10):

                if str(i) not in string:
                    pd_num(''.join([string, str(i)]))

    elif len(string) == 9:
        check = string[6:]

        if int(check)%13 == 0:
            for i in range(1, 10):

                if str(i) not in string:
                    pd_num(''.join([string, str(i)]))
    
    elif len(string) == 10:
        check = string[7:]

        if int(check)%17 == 0:
            sum_ += int(string)

    else:
        for i in range(10):
            if str(i) not in string:
                pd_num(''.join([string, str(i)]))

sum_ = 0
pd_num()
print(sum_)