
def unit_test(function_name, arg_tuple, value):
    print('testing ', function_name.__name__, ' on input ', arg_tuple, ' to be ', value, sep='')
    func_val = function_name(*arg_tuple)
    if func_val == value:
        print('PASSED')
    else:
        print('FAILED')
        print('function returned ', func_val, ' instead')

    print()
