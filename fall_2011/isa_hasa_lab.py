"""
Lab on is-a and has-a relations

On this sheet, write down the output from each print statement in this module.

If executing the print statement would raise an exception,
just write ERROR 
"""

class D(dict):
    'An instance of D is a dictionary'
    # No __init__  needed, inherit from dict
    
    def __repr__(self):
        'Prints as D({...}) not just {...}'
        return 'D(%s)' % dict.__repr__(self)

class X(object):
    'An instance of X has a dictionary'
    def __init__(self, d):
        assert isinstance(d, dict) # d must be a dictionary
        self.d = d
        
    def __repr__(self):
        'Prints as X({...}) not just {...}'
        return 'X(%s)' % dict.__repr__(self.d)

d0 = { 'a':1, 'b':2 }

d, x = D(d0), X(d0)

print type(d), d, isinstance(d, D), isinstance(d, dict)

print type(x), x, isinstance(x, X), isinstance(x, dict)

print type(x.d), x.d, isinstance(x.d, X), isinstance(x.d, dict)

print d['a']

#print x['a']

print x.d['a']

for c in d: print c

#for c in x: print c

for c in x.d: print c

# It is also instructive to print dir(d), dir(x)
#  What is present in dir(d) that is absent from dir(x) ?
#  What is present in dir(x) that is absent from dir(d) ?



        

