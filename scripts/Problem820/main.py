def nth_digit_of_reciprocal(number: int, nth: int) -> int:

    if number == 1:
        return 0

    numerator = 10
    denominator = number

    seen_numerators: list[int] = []
    seen_decimals = ''

    digits = 0
    while True:

        if numerator in seen_numerators:

            repeating_sequence = seen_decimals[seen_numerators.index(numerator):]
            
            if len(repeating_sequence) == 1:
                return int(repeating_sequence[0])

            else:
                proxy_index = (nth - len(seen_decimals)) % len(repeating_sequence)
                true_index = proxy_index - 1 if proxy_index else len(repeating_sequence) - 1

                return int(repeating_sequence[true_index])
        seen_numerators.append(numerator)

        decimal = numerator // denominator
        seen_decimals += str(decimal)
        
        numerator = numerator % denominator
        numerator *= 10

        if numerator == 0:
            return 0
        
        elif digits == nth:
            return decimal

        digits += 1


def sum_of_nth_digits_of_reciprocals(n: int) -> int:

    s = 0
    for k in range(1, n + 1):

        if k % 1000 == 0:
            answer = input(f'Waiting for approval on continuation. Currently at: {k} -- Enter for continuation / e for end:  ')

            if answer == 'e':
                return -1
            
        s += nth_digit_of_reciprocal(number=k, nth=n)

    return s

if __name__=='__main__':
    
    print(sum_of_nth_digits_of_reciprocals(n=10**7))