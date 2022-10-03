

from code import check_for_symmetry
# from unit_test import unit_test

def unit_test(function_name, arg_tuple, value):
    print('testing ', function_name.__name__, ' on input ', arg_tuple, ' to be ', value, sep='')
    if function_name(*arg_tuple) == value:
        print('PASSED')
    else:
        print('FAILED')
    print()

symmetric_test_values = [
    (check_for_symmetry, True, ('racecar', ) )
]

for t in symmetric_test_values:
    f, value, arg_tuple = t
    unit_test(f, arg_tuple, value)


