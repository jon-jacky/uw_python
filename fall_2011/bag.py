"""
bag (multiset) class, subclass of dict with + redefined as bag union
"""

class bag(dict):
    """
    Bag (multiset), subclass of dict with + redefined as bag union
    """
    # inherit __init__ from dict

    def __repr__(self):
        """
        String representation, uses dict (superclass) representation
        """
        return 'bag(%s)' % dict.__repr__(self)

        
    def __add__(self, b):
        """
        redefine + as bag union
        """
        u = bag(self) # union, start by copying self
        for k in b:
            if k in u:
                u[k] += b[k]
            else:
                u[k] = b[k]
        return u

d1 = {'a':2, 'b':3}
d2 = {'b':2, 'c':1}

print d1
print d2

# print d1 + d2 # TypeError: unsupported operand type(s)

b1 = bag(d1)  # create bags from dictionaries
b2 = bag(d2)

print b1
print b2

print b1 + b2

b3 = bag({'b':1, 'c':2, 'd':3}) # create bag in one step

print b3
print b2 + b3

    
