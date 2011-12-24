"""
Demonstrate generators and lazy computation
"""

# review range

print range(10)

# Print a million elements, type ^C to stop
# Does NOT work in Mac IDLE, ^C doesn't interrupt loop!
# use python -i generator.py  instead
#for i in range(1000000): print i

# Try to print a billion elements, on Windows, fails with MemoryError
# On Mac, DON'T do this!  Hangs python, hangs desktop, must reboot
# for i in range(1000000000): print i

# Use xrange not range for a billion elements, type ^C to stop
# for i in xrange(1000000000): print i

# range is eager - computes all the elements first
# xrange is lazy - computes each element as needed

# Python generators code lazy computation,
# remember values of local variables between calls

def my_xrange(size):
    i = -1
    while True:
        i += 1
        if i < size:
            yield i             # yield not return makes generator
        else:
            raise StopIteration # how to exit from generator

for i in my_xrange(3): print i # what about this?

# generate a billion elements
# for i in my_xrange(1000000000): print i  # ^C to stop

# Generator expressions are like list comprehensions, but lazy

# one hundred million elements
# On Windows, list comprehension fails with MemoryError after 20+ sec
# On Mac, python hangs
# print sum([2*i for i in xrange(100000000)])

# one hundred million elements
# generator expression returns result after 20+ sec
print sum(2*i for i in xrange(100000000))
