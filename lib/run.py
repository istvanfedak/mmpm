#!/usr/bin/env python3
from ctypes import cdll, POINTER, c_char_p, c_int, pointer, c_char


# https://github.com/dvida/py-ctypes-multidimensional-arrays/blob/master/myfunc.py
def char3ArrayToPointer(arr):
    """ Converts a 3D numpy to ctypes 3D array.

    Arguments:
        arr: [ndarray] 3D numpy float64 array
    Return:
        arr_ptr: [ctypes double pointer]
    """
    CHAR = c_char
    CHAR_PTR = POINTER(CHAR)
    CHAR_PTR_PTR = POINTER(CHAR_PTR)

    # Init needed data types
    ARR_DIMX = CHAR
    ARR_DIMY = CHAR_PTR * len(arr)
    ARR_DIMZ = CHAR_PTR_PTR * len(arr[0])

    # Init pointer
    arr_ptr = ARR_DIMZ()

    for i, row in enumerate(arr):
        arr_ptr[i] = (c_char_p * len(row))

        for j, col in enumerate(row):
            arr_ptr[i][j] = (c_char_p * len(row))()

            #for k, val in enumerate(col):
            #    print(val)
                #arr_ptr[i][j][k] = val.encode('utf-8')

    return arr_ptr


libmmpm = cdll.LoadLibrary('./libmmpm.so')


# SINGLE STRING
test_single_string = libmmpm.test_single_string
test_single_string.argtypes = [c_char_p]
test_single_string.restype = None

string = c_char_p(b'message')
test_single_string(string)

LP_LP_c_char_p = POINTER(POINTER(c_char_p))
LP_c_char_p = POINTER(c_char_p)

# ARRAY OF STRINGS
test_array_of_char_ptrs = libmmpm.test_array_of_char_ptrs
test_array_of_char_ptrs.argtypes = [POINTER(c_char_p), c_int]
test_array_of_char_ptrs.restype = None

two_d_array = [b'0', b'1', b'2', b'3', b'4']
array_of_strings = (c_char_p * 5)(*two_d_array)
test_array_of_char_ptrs(array_of_strings, len(two_d_array))

# ARRAY OF ARRAYS OF STRINGS

display_modules = libmmpm.display_modules
display_modules.argtypes = [POINTER(POINTER(c_char_p)), c_int, c_int]
display_modules.restype = None

modules = [
    ['Category', 'Title', 'Repository', 'Author', 'Description'],
    ['Test', 'Module-Name', 'https://github.com', 'Brandon', 'Stuff']
]


height, width = len(modules), len(modules[0])
multi_d_array = POINTER(POINTER(c_char_p * width) * height)()

ptr = char3ArrayToPointer(modules)
