"""https://projecteuler.net/problem=89"""

if __name__=="__main__":
    from time import time, sleep

    def value(numeral):
        Numerals = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }

        length = len(numeral)
        comp = length - 2
        s = i = b = int()
        for i in range(length):
            if b:
                b = 0
                continue
            else:
                if i < comp:
                    if Numerals[numeral[i]] >= Numerals[numeral[i + 1]]:
                        s += Numerals[numeral[i]]
                    else:
                        s += Numerals[numeral[i + 1]] - Numerals[numeral[i]]
                        b = 1
                elif i == comp:
                    if Numerals[numeral[i]] >= Numerals[numeral[i + 1]]:
                        s += Numerals[numeral[i]]
                    else:
                        s += Numerals[numeral[i + 1]] - Numerals[numeral[i]]
                        break
                else:
                        s += Numerals[numeral[i]]
        return s

    def minimal_numeral(value):
        s = str()

        while value >= 1000:
            s += 'M'
            value -= 1000

        if value >= 900:
            s += 'CM'
            value -= 900

        if value >= 500:
            s += 'D'
            value -= 500
        
        if value >= 400:
            s += 'CD'
            value -= 400

        while value >= 100:
            s += 'C'
            value -= 100

        if value >= 90:
            s += 'XC'
            value -= 90

        if value >= 50:
            s += 'L'
            value -= 50

        if value >= 40:
            s += 'XL'
            value -= 40

        while value >= 10:
            s += 'X'
            value -= 10

        if value >= 9:
            s += 'IX'
            value -= 9

        if value >= 5:
            s += 'V'
            value -= 5

        if value >= 4:
            s += 'IV'
            value -= 4

        while value >= 1:
            s += 'I'
            value -= 1

        return s

    t = time()

    L = list()
    with open('p089_roman.txt', 'r') as file:
        for line in file:
            L.append(line.strip())

    i = int()
    for numeral in L:
        x = value(numeral)
        y = minimal_numeral(x)
        i += len(numeral) - len(y)
    print(i)

    print(time() - t)