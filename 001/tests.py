

from code import *
# from unit_test import unit_test

def unit_test(function_name, arg_tuple, value):
    print('testing ', function_name.__name__, ' on input ', arg_tuple, ' to be ', value, sep='')
    if function_name(*arg_tuple) == value:
        print('PASSED')
    else:
        print('FAILED')
    print()

test_values = [
    (check_for_symmetry, True, ('racecar', ) ),
    (convert_to_letters,  'a cat', ([1, 0, 3, 1, 20], ) ), 
    (convert_to_numbers, [ 2, 1, 20, 13, 1, 14 ], ('batman', ) ),
    (is_prime, True,  (59, ) ),
    (is_prime, False, (51, ) )
]

for t in test_values:
    f, value, arg_tuple = t
    unit_test(f, arg_tuple, value)

