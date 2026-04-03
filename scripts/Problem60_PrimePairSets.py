"""
https://projecteuler.net/problem=60
"""

from Package import binary_search
from Constants import primes_up_to_100Million
from time import sleep, time
from copy import deepcopy

def main(set_size):
    t = time()

    Primes = primes_up_to_100Million()

    Primes1 = []
    Primes2 = []
    for prime_ in Primes:
        if prime_ > 3 * 10**4:
            break
        elif prime_%3 == 1:
            Primes1.append(prime_)
        elif prime_%3 == 2:
            Primes2.append(prime_)
        else:
            Primes1.append(prime_)
            Primes2.append(prime_)

    Cand1 = dict()
    for prime_ in Primes1:
        Cand1[str(prime_)] = set()
    for prime_1 in Primes1:
        for prime_2 in Primes1:
            if prime_1 < prime_2:
                a = str(prime_1)
                b = str(prime_2)

                c = a + b
                d = b + a

                i1 = int(c)
                i2 = int(d)

                if binary_search(i1, Primes) and binary_search(i2, Primes):
                    Cand1[str(prime_1)].add(prime_2)
                    Cand1[str(prime_2)].add(prime_1)
    print(f'length of Candidates1: {len(Cand1)} ')

    size = set_size - 2
    Cands_old = deepcopy(Cand1)
    while size > 0:
        Cands_new = dict()
        for key1, value1 in Cands_old.items():
            for elem in value1:
                key2 = str(elem)
                value2 = Cand1[key2]

                if int(key2) > max([ int(elem) for elem in key1.split(',')]):
                    intersection_ = value1.intersection(value2)
                    if len(intersection_) >= size:
                        Cands_new[key1 + ',' + key2] = intersection_
        size -= 1
        Cands_old = Cands_new
        print(f'length of Candidates_old: {len(Cands_old)} ')

    Out = dict()
    for key, value in Cands_old.items():
        elem = value.pop()
        if elem > max([ int(elem) for elem in key.split(',')]):
            Out[key + ',' + str(elem)] = sum([ int(elem) for elem in key.split(',')]) + elem

    min_ = 10**6
    key_ = ''
    for key, value in Out.items():
        if value < min_:
            key_, min_ = key, value
    if key_ != '':
        return f'key: {key_}, min: {min_}  '

    
    Cand2 = dict()
    for prime_ in Primes2:
        Cand2[str(prime_)] = set()
    for prime_1 in Primes2:
        for prime_2 in Primes2:
            if prime_1 < prime_2:
                a = str(prime_1)
                b = str(prime_2)

                c = a + b
                d = b + a

                i1 = int(c)
                i2 = int(d)

                if binary_search(i1, Primes) and binary_search(i2, Primes):
                    Cand2[str(prime_1)].add(prime_2)
                    Cand2[str(prime_2)].add(prime_1)
    print(f'length of Candidates1: {len(Cand2)} ')

    size = set_size - 2
    Cands_old = deepcopy(Cand2)
    while size > 0:
        Cands_new = dict()
        for key1, value1 in Cands_old.items():
            for elem in value1:
                key2 = str(elem)
                value2 = Cand2[key2]

                if int(key2) > max([ int(elem) for elem in key1.split(',')]):
                    intersection_ = value1.intersection(value2)
                    if len(intersection_) >= size:
                        Cands_new[key1 + ',' + key2] = intersection_
        size -= 1
        Cands_old = Cands_new
        print(f'length of Candidates_old: {len(Cands_old)} ')

    Out = dict()
    for key, value in Cands_old.items():
        elem = value.pop()
        if elem > max([ int(elem) for elem in key.split(',')]):
            Out[key + ',' + str(elem)] = sum([ int(elem) for elem in key.split(',')]) + elem

    min_ = 10**6
    key_ = ''
    for key, value in Out.items():
        if value < min_:
            key_, min_ = key, value
    if key_ != '':
        return f'key: {key_}, min: {min_}  '

if __name__ == "__main__":
    sum_, min_, max_ = 0, 1000, 0
    for i in range(10):
        t1 = time()

        print(main(set_size=5))

        t2 = time()

        diff = t2 - t1
        sum_ += diff
        
        print(diff)

        if diff > max_:
            max_ = diff
        if diff < min_:
            min_ = diff

    print(f'min: {min_} | avg: {sum_/10} | max: {max_}')
    print('\n')