def is_increasing_number(number: int) -> bool:

    string = str(number)

    for i in range(len(string) - 1):
        if int(string[i]) > int(string[i + 1]):
            return False
        
    return True


def is_decreasing_number(number: int) -> bool:

    string = str(number)

    for i in range(len(string) - 1):
        if int(string[i]) < int(string[i + 1]):
            return False
    
    return True


def is_bouncy_number(number: int) -> bool:

    if not is_increasing_number(number=number) and not is_decreasing_number(number=number):
        return True
    return False


def amount_of_bouncy_numbers_below(number: int) -> int:

    count = 0
    for n in range(1, number):

        if is_bouncy_number(number=n):
            count += 1
    return count


def when_does_proportion_of_bouncy_numbers_reach(level: float) -> int:
    """The first integer for which the proportion of bouncy numbers below it, reaches the level.
    50% is specified as 0.5
    """

    count = 0
    number = 100
    while True:

        if is_bouncy_number(number=number):
            count += 1

        if count / number == level:
            return number

        if number % 10000 == 0:
            answer = input(f'Waiting for approval on continuation. Currently at: {number} -- Enter for continuation / e for end:  ')

            if answer == 'e':
                return -1

        number += 1

if __name__=='__main__':

    print(when_does_proportion_of_bouncy_numbers_reach(level=0.99))