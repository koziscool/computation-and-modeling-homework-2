import os, sys
ROOT_DIR = os.path.abspath(os.curdir)
UTIL_PATH = os.path.join( ROOT_DIR, 'utils' )
sys.path.append(UTIL_PATH)

import code
from unit_test import unit_test

test_values = [
]

print()
for t in test_values:
    f, value, arg_tuple = t
    unit_test(f, arg_tuple, value)
