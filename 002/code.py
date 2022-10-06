
import os, sys
ROOT_DIR = os.path.abspath(os.curdir)
UTIL_PATH = os.path.join( ROOT_DIR, 'utils' )
sys.path.append(UTIL_PATH)

import code
from const import letter_dict, number_dict

from functools import reduce
from operator import lt
import math

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

def calc_nth_root_newtons_method( k, n, precision ):
    f = lambda x, k, n: x ** n - k
    derivatve = lambda x, k, n: n * (x ** (n-1))
    approximations = [0, k/2]
    while abs( approximations[-1] -approximations[-2] ) > precision:
        approximations.append( approximations[-1] - 
            (f(approximations[-1], k, n) / derivatve(approximations[-1], k, n) )   )

    return approximations[-1]


def calc_minimum(arr):
    smaller = lambda a, b: a if a < b else b
    return( reduce( smaller, arr ) )

def calc_maximum(arr):
    bigger = lambda a, b: a if a > b else b
    return( reduce( bigger, arr ) )

def simple_sort( arr ):
    ret_arr, unsorted = [], arr.copy()
    while len( ret_arr ) < len( arr ):
        smallest = calc_minimum(  unsorted )
        index = unsorted.index( smallest )
        unsorted = unsorted[ :index ] + unsorted[ index + 1 : ]
        ret_arr.append(smallest)
    return ret_arr

def swap_sort(arr):
    num_swaps = 1
    while num_swaps > 0:
        num_swaps = 0
        for i in range( len(arr) - 1 ):
            if arr[i] > arr[ i+1 ]:
                num_swaps += 1
                arr[i], arr[ i+1 ] = arr[ i+1 ], arr[i]
    return arr

def tally_sort( arr ):
    minimum = calc_minimum(arr)
    maximum = calc_maximum(arr) - minimum

    adj_arr = [ i - minimum for i in arr ]
    tallies = [0] * (maximum + 1)

    for elt in adj_arr:
        tallies[elt] += 1

    ret_arr = []
    for i in range( len(tallies) ):
        for _ in range( tallies[i]):
            ret_arr.append(i)

    ret_arr = [ i + minimum for i in ret_arr ]
    return ret_arr    

def card_sort(arr):
    sorted, unsorted = [], arr.copy()
    while len(sorted) < len(arr):
        elt, elt_index = unsorted.pop(), 0
        while len(sorted) >= elt_index + 1 and elt > sorted[elt_index]:
            elt_index += 1
        sorted = sorted[ :elt_index ] + [ elt ] + sorted[ elt_index : ]
    return sorted

def merge(a,b):
    a_index, b_index, ret_arr = 0, 0, []
    while a_index < len(a) and b_index < len(b):
        if a[a_index] < b[b_index]:
            ret_arr.append( a[a_index] )
            a_index += 1
        else:
            ret_arr.append( b[b_index] )
            b_index += 1

    if a_index == len(a):
        ret_arr += b[ b_index: ]

    if b_index == len(b):
        ret_arr += a[ a_index: ]

    return ret_arr
