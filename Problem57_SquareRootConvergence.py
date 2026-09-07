"""
https://projecteuler.net/problem=57
"""

from time import sleep

def evaluate_inner(expansion):
    # print(expansion)
    expansion = expansion.strip()

    for index in range(len(expansion)):
        symbol = expansion[index]

        if symbol == '[':
            open_ = index
        elif symbol == ',':
            comma = index
        elif symbol == ']':
            close_ = index

    if '+' in expansion.split(' '):
        num = int(expansion[0])
        numerator = int(expansion[open_ + 1:comma])
        denominator = int(expansion[comma + 1:close_])

        return str( [num*denominator + numerator, denominator] )

    elif '/' in expansion.split(' '):
        numerator = int(expansion[open_ + 1:comma])
        denominator = int(expansion[comma + 1:close_])

        return str( [denominator, numerator] )

def evaluate_outer(expansion):
    expansion = expansion.strip()
    Brackets_open = []
    Brackets_close = []

    for index in range(len(expansion)):
        symbol = expansion[index]

        if symbol == '(':
            Brackets_open.append(index)
        elif symbol == ')':
            Brackets_close.append(index)

    # print(Brackets_open, Brackets_close)

    for index in range(len(Brackets_open) - 1, -1, -1):
        pos_open = Brackets_open[index]
        pos_close = Brackets_close[-(index + 1)]
        # print(f'pos opern: {pos_open}, pos close: {pos_close}')

        res = evaluate_inner(expansion[pos_open + 1: pos_close])
        expansion = expansion[:pos_open] + res + expansion[pos_close + 1:]
        # print(expansion)

        Brackets_close = [ elem - (pos_close - pos_open + 1 - len(res)) for elem in Brackets_close ]
        # print(Brackets_close)

    return expansion

def main():
    c = 0
    last = str([0, 1])
    for depth in range(1, 10**3 + 1):

        expansion = f'( 1 / ( 2 + {last} ) )'
        fraction = evaluate_outer(expansion)
        last = fraction

        res = evaluate_outer(f'( 1 + {fraction} )')

        for index in range(len(res)):
            symbol = res[index]

            if symbol == '[':
                open_ = index
            elif symbol == ',':
                comma = index
            elif symbol == ']':
                close_ = index
        
        numerator = res[open_ + 1: comma].strip()
        denominator = res[comma + 1: close_].strip()

        if len(numerator) > len(denominator):
            c += 1

    return c

print(main())