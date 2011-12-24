"""
Write a program that takes a single array parameter and
returns the decimal average of the input values

Comments indicate local and global variables
"""

# array is function parameter

def avg1(a):        # a,sum,i: local variables, don't appear in dir()
    'explicit loop' # docstring, appears in help(avg1)
    sum = 0
    for i in a:
        sum += i
    return float(sum)/len(a)

def avg2(a):         # a: local variable, different from a in avg1
    'use built-in sum of sequence'
    return float(sum(a))/len(a)

def avg3(*a):
    'use *args form to collect array elements'
    return float(sum(a))/len(a)

b = [1,2,3] # global variable (module-level variable), visible in dir()

print b

b1 = avg1(b) # global variable variable, visible in dir()

print b1
