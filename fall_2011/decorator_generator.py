"""
decorator that turns a function into a generator
"""

from functools import wraps

def generator(f):
    #@wraps(f)    # preserves docstring in f etc.
    def gen(s):
        for x in s:
            yield f(x)
        #raise StopIteration # not necessary, doesn't hurt
    return gen


@generator
def odd(x):
    'Returns 1 for odd x, 0 otherwise' 
    return x % 2

for o in odd([1,2,3]): print o

print

@generator
def my_bool(x):
    return bool(x)

for b in my_bool([0,1,'','x',[],[0]]): print b

print

# can also apply the decorator function to an already-defined function

bg = generator(bool)  # Python's built-in bool function

for b in bg([0,1,'','x',[],[0]]): print b


# Try a generator expression

def generator2(f):
    @wraps(f)    # preserves docstring in f etc.
    def gen(s):
        return (f(x) for x in s) # generator expression
    return gen

@generator2
def odd2(x):
    'Returns 1 for odd x, 0 otherwise' 
    return x % 2

for o in odd2([1,2,3]): print o
