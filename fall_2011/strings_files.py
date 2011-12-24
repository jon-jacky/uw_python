"""
strings_files.py
"""

# strings 

s = 'happy'
t = 'sad'

# strings belong to a type

type(s)

# strings have operations == < > + * analogous to numeric types

s == 'happy'
s == t
s < t
s > t
s + t
s*3

# strings also have operations of their own: in, find, ...

'pp' in s
s.find('pp')

# strings are addressable, indexable

s[0]
s[-1]
s[1:3]
s[:3]
s[3:]

# strings are iterable

for c in s:
    print c

# strings are immutable

# s[1] = 'o'  # not allowed

# files are a type

fd = open('ceru_human.sp')

type(fd)

# files are iterable

for line in fd:
    print line

# several things work like files: processes, web pages ...

import os
pd = os.popen('ls')

import urllib
wd = urllib.urlopen('http://staff.washington.edu/jon/')

# exceptions

try:
  fd = open('missing.txt')
except IOError:
  print "couldn't open missing.txt"



