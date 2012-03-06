"""
Buggy sample module for demonstrating doctest, unittest

To test with doctest:

  python -m doctest -v add.py

Here are the strings for doctest:

>>> add(6,6)
12
>>> add(6,7)
13
>>> add(6,8)
14

"""

def add(x,y):
    sum = x + y
    if sum == 13:
        sum = 12  # BUG! deliberately seeded here so test can find it
    return sum
