
import math

def check_for_symmetry(s):
    return s == s[::-1]

def convert_to_numbers(s):
    letter_dict = {
        ' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
        'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26
    }
    ret_arr = []
    for c in s:
        ret_arr.append(letter_dict[c])
    return ret_arr


def convert_to_letters(arr):
    number_dict = {
        0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd',
        5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
        10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n',
        15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
        25: 'y', 26: 'z'
    }
    ret_s = ""
    for elt in arr:
        ret_s += number_dict[elt]
    return ret_s

def is_prime(n):
    for i in range(2, math.floor(n/2)):
        if n % i == 0:
            return False
    return True



def get_intersection( list1, list2 ):
    intersect_dict = {}
    for elt in list1:
        intersect_dict[elt] = 'l1'
    
    for elt in list2:
        if elt in intersect_dict:
            intersect_dict[elt] = 'both'

    ret_arr = []
    for key, value in intersect_dict.items():
        if value == 'both':
            ret_arr.append( key )
    
    return ret_arr

def get_union( list1, list2 ):
    union_dict = {}
    for elt in list1:
       union_dict[elt] = 'either'
    
    for elt in list2:
        union_dict[elt] = 'either'

    ret_arr = []
    for key, value in union_dict.items():
       ret_arr.append( key )

    ret_arr.sort()
    return ret_arr


def count_characters(s):
    ret_dict = {}
    for c in s:
        if c.lower() in ret_dict:
            ret_dict[ c.lower()] += 1
        else:
            ret_dict[ c.lower()] = 1
    
    return ret_dict


def get_first_n_terms_nonrecursive(n):
    ret_arr, current_val = [], 5
    for _ in range(n):
        ret_arr.append(current_val)
        current_val = 3 * current_val - 4
    return ret_arr



def get_first_n_terms_recursive(n):
    ret_arr, current_val = [], 5
    while len(ret_arr) < n:
        ret_arr.append(current_val)
        current_val = 3 * current_val - 4
    return ret_arr


def convert_to_base_10(n):
    ret_val = 0
    for index, c in enumerate(str(n)[::-1]):
        ret_val += int(c) * 2 ** index
    return ret_val


def convert_to_base_2(n):
    exponent, dividend, ret_s  = 0, n, ''
    while dividend > 0:
        remainder = dividend % 2
        ret_s += str(remainder)
        dividend = (dividend - remainder) // 2
    return int(ret_s[::-1])

