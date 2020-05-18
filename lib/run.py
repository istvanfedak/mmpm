#!/usr/bin/env python3
from ctypes import cdll, c_char_p, c_int, POINTER


# https://github.com/dvida/py-ctypes-multidimensional-arrays/blob/master/myfunc.py
PTR_TO_CHAR = POINTER(c_char_p)
PTR_TO_PTR_TO_CHAR = POINTER(PTR_TO_CHAR)

libmmpm = cdll.LoadLibrary('./libmmpm.so')

# SINGLE STRING
test_single_string = libmmpm.test_single_string
test_single_string.argtypes = [c_char_p]
test_single_string.restype = None

string = c_char_p(b'message')
test_single_string(string)

# ARRAY OF STRINGS
test_array_of_char_ptrs = libmmpm.test_array_of_char_ptrs
test_array_of_char_ptrs.argtypes = [POINTER(c_char_p), c_int]
test_array_of_char_ptrs.restype = None

array = [b'0', b'1', b'2', b'3', b'4']
array_of_strings = (c_char_p * len(array))(*array)
test_array_of_char_ptrs(array_of_strings, len(array))

# ARRAY OF ARRAYS OF STRINGS
modules = [
    [b'Category', b'Title', b'Repository', b'Author', b'Description'],
    [b'Test', b'Module-Name', b'https://github.com', b'Brandon', b'Stuff']
]

display_modules = libmmpm.display_modules
rows, columns = len(modules), len(modules[0])

display_modules.argtypes = [((c_char_p * columns) * rows), c_int, c_int]
display_modules.restype = None

modules_pointer = ((c_char_p * columns) * rows)()

for i, row in enumerate(modules):
    modules_pointer[i] = (c_char_p * columns)(*row)
    #test_array_of_char_ptrs(modules_pointer[i], width)

display_modules(modules_pointer, rows, columns)
