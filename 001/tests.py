
import os, sys
ROOT_DIR = os.path.abspath(os.curdir)
UTIL_PATH = os.path.join( ROOT_DIR, 'utils' )
sys.path.append(UTIL_PATH)

import code
from unit_test import unit_test

test_values = [
    (code.check_for_symmetry, True, ('racecar', ) ),
    (code.convert_to_letters,  'a cat', ([1, 0, 3, 1, 20], ) ), 
    (code.convert_to_numbers, [ 2, 1, 20, 13, 1, 14 ], ('batman', ) ),
    (code.is_prime, True,  (59, ) ),
    (code.is_prime, False, (51, ) )
]

for t in test_values:
    f, value, arg_tuple = t
    unit_test(f, arg_tuple, value)
