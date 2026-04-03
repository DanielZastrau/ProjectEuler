from main import is_increasing_number, is_decreasing_number, is_bouncy_number, amount_of_bouncy_numbers_below, \
    when_does_proportion_of_bouncy_numbers_reach

failed_tests: list[str] = []

if not is_increasing_number(number=134468) == True:
    failed_tests.append('1')

if not is_increasing_number(number=66420) == False:
    failed_tests.append('2')

if not is_decreasing_number(number=134468) == False:
    failed_tests.append('3')

if not is_decreasing_number(number=66420) == True:
    failed_tests.append('4')

if not is_bouncy_number(number=134468) == False:
    failed_tests.append('5')

if not is_bouncy_number(number=66420) is False:
    failed_tests.append('6')

if not is_bouncy_number(number=155349) is True:
    failed_tests.append('7')

if not amount_of_bouncy_numbers_below(number=1000) == 525:
    failed_tests.append('8')

if not when_does_proportion_of_bouncy_numbers_reach(level=0.5) == 538:
    failed_tests.append('9')

if not when_does_proportion_of_bouncy_numbers_reach(level=0.9) == 21780:
    failed_tests.append('10')

if not failed_tests:
    print('Everything passed.')
else:
    print('The following tests failed: ', failed_tests)