"""
Demonstrate reductions, several techniques
Compute product of a sequence, analogous to built in sum function
"""

import operator

# test cases
s0 = tuple() # empty
s1 = (1,)
s4 = (1,2,3,4)
b4 = (1, 'a', [ 'x '], {})  # three true and a false (empty dictionary)

# A reduction computes a single value from a collection

print sum(s4)
print max(s4)
print min(s4)
print all(b4)
print any(b4)

# There is built in sum but not product

def product_loop(s):
    result = s[0]   # fails on empty s
    for x in s[1:]:
        result = result * x
    return result

def product2(x,y):
    return x*y

def product_named(s):
    return reduce(product2, s) # fails on empty s

# def product_times(s):
#    return reduce(*, s) # syntax error

def product_timeschar(s):
    return reduce('*', s) # TypeError: 'str' object is not callable

def product_operator(s):
    return reduce(operator.mul, s)

def product_lambda(s):
    return reduce(lambda x,y: x*y, s)

if __name__ == '__main__':
    print product_loop(s4)
    print product_named(s4)
    # print product_timeschar(s4) # runtime error, see above
    print product_operator(s4)
    print product_lambda(s4)





        
