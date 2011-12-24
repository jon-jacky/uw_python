"""
atom.py - solution for /Users/jon/uw_python/fall_2011/assign_7.txt
"""

class Atom(object):
    """
    Atom base class for chemistry simulation
    """
    # class attributes shared by all instances
    max_bonds = 0          # placeholder for max_bonds in subclasses
    
    def __init__(self):
        self.bonds = list() # no bonds, initialize with empty list

    def __str__(self):
        # the class name must be the chemical symbol
        s  = '%s %s' % (self.__class__.__name__, id(self)) 
        for a in self.bonds:
            s += ', %s %s' % (a.__class__.__name__, id(a)) # not s.__str__(), infinite recursion!
        return s

    def bond(self, other):
        if (len(self.bonds) < self.max_bonds and
            len(other.bonds) < other.max_bonds):
            self.bonds.append(other)
            other.bonds.append(self)
            return other # success, otherwise returns None for failure
        
class H(Atom):
    """
    Hydrogen atom class for chemistry simulation
    the class name is the chemical symbol
    """
    max_bonds = 1 

    # no methods needed - just use base class

class O(Atom):
    """
    Oxygen atom class for chemistry simulation
    the class name is the chemical symbol
    """
    max_bonds = 2 

# Test
if __name__ == '__main__':
    atoms = [ H(), H(), H(), O(), O()]
    h0, h1, h2, o0, o1 = atoms
    o0.bond(h0)
    o0.bond(h1)
    for a in atoms:
        print a

