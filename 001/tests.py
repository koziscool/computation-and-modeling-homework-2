
import os, sys
ROOT_DIR = os.path.abspath(os.curdir)
UTIL_PATH = os.path.join( ROOT_DIR, 'utils' )
sys.path.append(UTIL_PATH)

import code
from unit_test import unit_test


cat_dict = {
    'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3
}

test_values = [
    (code.check_for_symmetry, True, ('', ) ),
    (code.check_for_symmetry, True, ('racecar', ) ),
    (code.check_for_symmetry, False, ('batman', ) ),
    (code.convert_to_letters,  'a cat', ([1, 0, 3, 1, 20], ) ), 
    (code.convert_to_numbers, [ 2, 1, 20, 13, 1, 14 ], ('batman', ) ),
    (code.is_prime, True,  (59, ) ),
    (code.is_prime, False, (51, ) ),
    (code.get_intersection, [2], ([1, 1, 1, 2, 2, 4], [2, 2, 3, 3])  ),
    (code.get_union, [1, 2, 3, 4], ([1, 1, 1, 2, 2, 4], [2, 2, 3, 3])  ),
    (code.count_characters, cat_dict, ('A cat!!!', )  ),
    (code.get_first_n_terms_nonrecursive, [5, 11, 29, 83 ], (4, )  ),
    (code.get_first_n_terms_recursive, [5, 11, 29, 83 ], (4, )  ),
    ( code.convert_to_base_10, 19, (10011, ) ),
    ( code.convert_to_base_2, 10011, (19, ) ),

]

print()
for t in test_values:
    f, value, arg_tuple = t
    unit_test(f, arg_tuple, value)


