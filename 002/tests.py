import os, sys
ROOT_DIR = os.path.abspath(os.curdir)
UTIL_PATH = os.path.join( ROOT_DIR, 'utils' )
sys.path.append(UTIL_PATH)

import code
from unit_test import unit_test


test_values = [
    (code.encode_string,  [1, 0, 3, 1, 20], ('a cat', 1, 0 ) ), 
    (code.encode_string,  [5, 3, 9, 5, 43], ('a cat', 2, 3 ) ), 
    (code.decode_numbers,  'a cat', ([5, 3, 9, 5, 43], 2, 3) ),
    ( code.calc_minimum, 1, ( [4, 5, 1, 2], ) ), 
    ( code.simple_sort, [ 1, 2, 4, 5 ],  ( [4, 5, 1, 2], ) ) ,
    ( code.swap_sort, [ 1, 2, 4, 5 ],  ( [4, 5, 1, 2], ) ) ,
    ( code.tally_sort, [ 1, 2, 2, 2, 2, 4, 5, 5 ],  ( [4, 2, 2, 5, 2, 5, 1, 2], ) ) ,
    ( code.tally_sort, [ 1, 2, 4, 5 ],  ( [4, 5, 1, 2], ) ) ,
    ( code.card_sort, [ 1, 2, 4, 5 ],  ( [4, 5, 1, 2], ) ) ,
]

print()
for t in test_values:
    f, value, arg_tuple = t
    unit_test(f, arg_tuple, value)



message = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71,
377, 547, 717, 751, 683, 785, 513, 241, 547, 751]

for a in range(1, 100):
    for b in range(100):
        decoded_message =code. decode_numbers( message, a, b )
        if decoded_message:
            print(decoded_message)


print( code.root_2_binary_search() )
print( code.calc_square_root( 2, 10 ** -5 ) )
print( code.calc_nth_root( 2, 2, 10 ** -5 ) )




