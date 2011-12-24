"""
concordance - week 3 assignment

Write a function named concordance that takes three arguments: a
string, a file object for a file that is open for reading, and a
file object for a file that is open for writing.  The function
writes in the output file the line numbers and contents of all the
lines in the input file where the string occurs.  Write the function
in a module concordance.py that also opens the input and output
files, calls the function, and closes the files.

In my solution, this script gets search string, input and output filenames
from command line. Usage:

 python concordance.py string infile outfile

"""

import sys

def concordance(s, fi, fo):
    """
    s:  string to search for in each line in input file
    fi: input file object, open for reading
    fo: output file object, open for writing
    """
    for i, line in enumerate(fi): # first line is number 0
        if s in line:
            fo.write('%s: %s\n' % (i, line))
    return i  # number of input lines

# search string and file names must appear on command line
#  python concordance.py string infile outfile

if __name__  == '__main__':
    fi = open(sys.argv[2], 'r')
    fo = open(sys.argv[3], 'w')
    concordance(sys.argv[1], fi, fo)
    fi.close()
    fo.close()

