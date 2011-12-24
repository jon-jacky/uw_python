"""
Demonstrate decorators
"""

# define a function *in a function* and return that function

def addn(n):
    def adder(i):
        return i + n
    return adder

add2 = addn(2)
print add2(1)
add3 = addn(3)
print add3(1)

# pass a function as an argument, use that to define the function you return

def odd(i): return i % 2

def even(i): return not odd(i)

def sieve(f):
    def siever(s):
        return [ x for x in s if f(x)]
    return siever

s = [1,2,3,4]
oddsieve = sieve(odd)
print oddsieve(s)
evensieve  = sieve(even)
print evensieve(s)

# The decorator operator @ abbreviates the preceding pattern
# @f; def g  means g = f(g)

@sieve
def osieve(i): return i % 2

print osieve(s)

# You can also use a class as a decorator
# because classes and objects are callable (via __init__ and __call__)

class memoize:
    """
    memoize decorator from avinash.vora
    http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    """
    def __init__(self, function): # runs when memoize class is called
        self.function = function
        self.memoized = {}

    def __call__(self, *args): # runs when memoize instance is called
        try:
          return self.memoized[args]
        except KeyError:
          self.memoized[args] = self.function(*args)
          return self.memoized[args]

@memoize        # same effect as sum2x = memoize(sum2x)
def sum2x(n):
    return sum(2*i for i in xrange(n)) #takes time when n > 10 million

# sum2x(100000000) # first time takes > 20 sec, second time very fast
