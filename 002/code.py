
import os, sys
ROOT_DIR = os.path.abspath(os.curdir)
UTIL_PATH = os.path.join( ROOT_DIR, 'utils' )
sys.path.append(UTIL_PATH)

import code
from const import letter_dict, number_dict


def encode_string(s, a, b):
    ret_arr = []
    for c in s:
        ret_arr.append( letter_dict[c] * a + b )
    return ret_arr


def decode_numbers(arr, a, b):
    ret_s =  ''
    for elt in arr:
        d = (elt - b ) // a
        if (elt - b) % a !=0 or d not in number_dict:
            return False
        else:
            ret_s += number_dict[d]
    return ret_s