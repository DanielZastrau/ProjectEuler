"""https://projecteuler.net/problem=79"""

from time import time, sleep

def generate_start(S):
    for s in S:
        for elem in s:
            yield elem

def clean(S, passcode):
    Out = set()
    for s in S:
        string = str()
        for elem in list(s):
            if elem not in list(passcode):
                string += elem
        if string != str():
            Out.add(string)
    return Out

if __name__=="__main__":
    S = set()
    with open('p079_keylog.txt', 'r') as file:
        for line in file:
            S.add(line.strip())

    passcode = str()
    while True:
        for start in generate_start(S):
            bool_ = True
            for s in S:
                for i, e in enumerate(list(s)):
                    if e == start and i != 0:
                        bool_ = False
            if bool_:
                passcode += start
                print(passcode)
                break
        
        S = clean(S, passcode)
        if len(S) == 0:
            break
    print(passcode)