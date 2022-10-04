
import os, sys
ROOT_DIR = os.path.abspath(os.curdir)
UTIL_PATH = os.path.join( ROOT_DIR, 'utils' )
sys.path.append(UTIL_PATH)

import code
from const import letter_dict, number_dict

from functools import reduce
from operator import lt


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


def root_2_binary_search():
    lower, upper = 1, 2
    midpoint = lambda a, b: (a+b) / 2
    while upper - lower > 10 ** -5:
        if midpoint( lower, upper ) ** 2 > 2:
            upper = midpoint(lower, upper) 
        else:
            lower = midpoint(lower, upper) 
    return midpoint(lower, upper)

def calc_square_root( x, precision ):
    lower, upper = 0, x 
    midpoint = lambda a, b: (a+b) / 2
    while upper - lower > precision:
        if midpoint( lower, upper ) ** 2 > x:
            upper = midpoint(lower, upper) 
        else:
            lower = midpoint(lower, upper) 
    return midpoint(lower, upper)


def calc_nth_root( x, n, precision ):
    lower, upper = 0, x 
    midpoint = lambda a, b: (a+b) / 2
    while upper - lower > precision:
        if midpoint( lower, upper ) ** n > x:
            upper = midpoint(lower, upper) 
        else:
            lower = midpoint(lower, upper) 
    return midpoint(lower, upper)


def calc_minimum(arr):
    smaller = lambda a, b: a if a < b else b
    return( reduce( smaller, arr ) )

def simple_sort( arr ):
    ret_arr, unsorted = [], arr
    while len( ret_arr ) < len( arr ):
        smallest = calc_minimum(  unsorted )
        index = unsorted.index( smallest )
        unsorted = unsorted[ :index ] + unsorted[ index + 1 : ]
        ret_arr.append(smallest)
    return ret_arr






