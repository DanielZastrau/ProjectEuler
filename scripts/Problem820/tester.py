from main import nth_digit_of_reciprocal, sum_of_nth_digits_of_reciprocals

failed_tests: list[str] = []

if not nth_digit_of_reciprocal(number=1, nth=7) == 0:
    failed_tests.append('1')

if not nth_digit_of_reciprocal(number=2, nth=7) == 0:
    failed_tests.append('2')

if not nth_digit_of_reciprocal(number=3, nth=7) == 3:
    failed_tests.append('3')

if not nth_digit_of_reciprocal(number=4, nth=7) == 0:
    failed_tests.append('4')

if not nth_digit_of_reciprocal(number=5, nth=7) == 0:
    failed_tests.append('5')

if not nth_digit_of_reciprocal(number=6, nth=7) == 6:
    failed_tests.append('6')

if not nth_digit_of_reciprocal(number=7, nth=7) == 1:
    failed_tests.append('7')

if not sum_of_nth_digits_of_reciprocals(n=7) == 10:
    failed_tests.append('8')

if not sum_of_nth_digits_of_reciprocals(n=100) == 418:
    print(sum_of_nth_digits_of_reciprocals(n=100))
    failed_tests.append('9')

if not failed_tests:
    print('Everything passed.')
else:
    print('The following tests failed: ', failed_tests)