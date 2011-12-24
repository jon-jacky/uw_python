"""
Write a program that takes a single array parameter and
returns the decimal average of the input values
"""
# array elements are command line arguments

import sys
a = [ float(i) for i in sys.argv[1:]]  # first arg is program name
print sum(a)/len(a)

