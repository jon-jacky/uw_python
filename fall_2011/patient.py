"""
Contrast equality, identity
Instances whose attributes all have the same values are not equal
"""

# strings

s1 = 'Smith, John'
s2 = 'Smith, John'

print 'strings s1 == s2', s1 == s2  # True

# tuples

t1 = ('Smith', 'John')
t2 = ('Smith', 'John')

print 'tuples t1 == t2', t1 == t2  # True

# dictionaries

d1 = { 'last': 'Smith', 'first': 'John' }
d2 = { 'last': 'Smith', 'first': 'John' }

print 'dictionaries d1 == d2', d1 == d2  # True

# instances

class Patient(object):
    def __init__(self, last, first):
        self.last = last
        self.first = first

p1 = Patient(last='Smith', first='John')
p2 = Patient(last='Smith', first='John')

print 'instances p1 == p2', p1 == p2  # False
