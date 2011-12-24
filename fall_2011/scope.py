"""
Demonstrate scope: local and global variables and functions
"""

# First, demonstrate distiction between compile-time and run-time errors

def bug1():
    # uncomment erroneous return to see syntax error handling
    return 1+(3) # return 1+(3 syntax error, detected at compile time

def bug2():
    return 1+'3' # type error,  not detected until run time


# demonstrate global and local variables

y = 2  # global variable

def f(x):
    return x + y   # function f uses global variable y

def g(x):
    y = 3;         # local variable y different from global y
    return y + x

def h(x):
    global y;      # declare y is the global variable y
    y = 3;         # update global variable y
    return y + x

# functions can be local, just like variables

def outer1(x):
    def inner1(y):  # local function, local like local variable
        return 2*y
    return 2*inner1(x)

def outer2(x):
    def inner1(y):  # local function, different from inner1 in outer1
        return 3*y
    return 3*inner1(x)


