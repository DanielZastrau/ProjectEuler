from math import log

def compare_two_exponentials(base_one: int, exp_one: int, base_two: int, exp_two: int) -> int:
    """Returns 0 or 1. 0 indicates the first one was larger, 1 indicates the second one was larger."""

    scalar_betw_bases = log(base_two, base_one)

    relative_first_exponent = exp_one / scalar_betw_bases

    if relative_first_exponent > exp_two:
        return 0
    return 1

def which_is_the_largest_exponential() -> int:
    """Returns the line number of the base, exponential pair with the largest value."""

    with open('./0099_base_exp.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    data = data.split('\n')
    data = map(lambda x: x.split(','), data)

    largest_line = -1
    base_value = -1
    exp_value = -1
    for i, (base, exp) in enumerate(data):

        if i == 0:
            base_value = int(base)
            exp_value = int(exp)

        else:
            if compare_two_exponentials(int(base), int(exp), base_value, exp_value) == 0:
                largest_line = i
                base_value = int(base)
                exp_value = int(exp)

    return largest_line + 1

if __name__=='__main__':
    print(which_is_the_largest_exponential())