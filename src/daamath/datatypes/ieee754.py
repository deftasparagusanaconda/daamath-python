import math as _math

from builtins import float as binary64

def binary64_add(a, b): return a + b
def binary64_sub(a, b): return a - b
binary64_bus = binary64_sub

def binary64_mul(a, b): return a * b
def binary64_div(a, b): return a / b
binary64_vid = binary64_div

def binary64_pow(a, b): return a ** b
def binary64_log(a, b): return _math.log(a, b)
def binary64_root(a, b): return _math.root(a, b)

# class Binary32:
#     'IEEE-754 binary32 floating point datatype'
#     significand
#     exponent
    
    
