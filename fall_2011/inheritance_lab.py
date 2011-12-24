"""
Lab on classes, objects, and inheritance

On this sheet, write down the output from each print statement in this module.

If executing the print statement would raise an exception,
just write ERROR 
"""

class A(object):
    x = 1
    def __init__(self):
        self.y = 2
    def f(self):
        return self.y

class B(A):
    pass

class C(A):
    def g(self):
        return 2*self.y

class D(A):
    def __init__(self):
        self.z = 3
    def f(self):
        return self.z
    
class E(A):
    def __init__(self):
        A.__init__(self)
        self.q = 5


a, b, c, d, e = A(), B(), C(), D(), E()

p = a

print a.x, a.y, a.f()

print b.x, b.y, b.f()

print c.x, c.y, c.f(), c.g()

print d.x, d.z, d.f()

print e.x, e.y, e.f(), e.q

print p.x, p.y, p.f()

a.y = 9

print a.y, b.y, p.y

A.x = 99

print a.x, b.x, p.x

print d.y



 
