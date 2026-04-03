def help():
    return 'primes_up_to_10to(order)', 'cubes_up_to_1Trillion'

def primes_up_to_10to(order):
    if order == 3:
        file = open('primes_up_to_10to3.txt', 'r')

    elif order == 4:
        file = open('primes_up_to_10to4.txt', 'r')

    elif order == 5:
        file = open('primes_up_to_10to5.txt', 'r')

    elif order == 6:
        file = open('primes_up_to_10to6.txt', 'r')
    
    elif order == 7:
        file = open('primes_up_to_10to7.txt', 'r')
    
    else:
        file = open('primes_up_to_10to8.txt', 'r')

    Primes = list()
    for line in file:
        Primes.append(int(line.strip()))

    file.close()
    return Primes

def cubes_up_to_1Trillion():
    Cubes = list()
    with open('cubes_up_to_1Trillion.txt', 'r') as file:
        for line in file:
            Cubes.append(int(line.strip()))
    return Cubes

def fibs_up_to_10to21():
    Fibs = list()
    with open('fibs_up_to_10to21.txt', 'r') as file:
        for line in file:
            Fibs.append(int(line.strip()))
    return Fibs