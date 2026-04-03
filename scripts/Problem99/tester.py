from main import compare_two_exponentials

failed_tests: list[str] = []

if not compare_two_exponentials(2, 11, 3, 7) == 1:
    failed_tests.append('1')

if not compare_two_exponentials(632382, 518061, 519432, 525806) == 0:
    failed_tests.append('2')


if not failed_tests:
    print('Everything passed.')
else:
    print('The following tests failed: ', failed_tests)