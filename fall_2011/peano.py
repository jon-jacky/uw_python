"""
peano.py - infinite generator
"""

def peano(i):
    """
    infinite generator: i, i+1, i+2, i+3, ...
    """
    while True:
        yield i
        i += 1

# print infinite sequence, must interrupt with ^C        
# for i in peano(1): print i

# Generate the first few values
p = peano(1)
print next(p)
print next(p)
print next(p)
print

# Generate finite prefix
p = peano(1) # start over
for i in range(10): print next(p)
print

# print infinite sequence, must interrupt with ^C        
# for i in peano(1): print i

# i in peano(...) is lazy, only generates elements until i is found

print '1000000 in peano(1)', 1000000 in peano(1)  # almost instant
print '10000000 in peano(1)', 10000000 in peano(1) # just perceptible delay
print '100000000 in peano(1)', 100000000 in peano(1) # several seconds
# print '0 in peano(1)', 0 in peano(1) # generates forever, must interrupt with ^C

# generator expression
pg = (i for i in peano(0) if i < 3)

# for i in pg: print i
# prints 0 1 2 then hangs, must interrupt with ^C
# for i in peano(0) keeps generating i but if ... rejects them all

