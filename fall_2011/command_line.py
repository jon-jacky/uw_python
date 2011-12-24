"""
Demonstrate sys.argv to command line arguments
The program itself if argument 0, other arguments are numbered 1, ...
"""


import sys

for i, arg in enumerate(sys.argv):
    print i, arg
