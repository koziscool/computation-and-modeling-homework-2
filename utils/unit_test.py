
def unit_test(function_name, arg_tuple, value):
    print('testing ', function_name.__name__, ' on input ', arg_tuple, ' to be ', value, sep='')
    if function_name(*arg_tuple) == value:
        print('PASSED')
    else:
        print('FAILED')
    print()
