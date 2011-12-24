"""
Demonstrate three forms of parameter declarations and argument passing 
"""

def f(a,b,c):
    'positional parameters'
    print a,b,c

s = (1,2,3)
d = { 'a':1, 'b':2, 'c':3 }

f(1,2,3) # 1,2,3   arguments matched to parameters by position
f(c=3,b=2,a=1)  # 1,2,3  arguments matched to parameters by keyword
f(*s)    # 1,2,3   * scatters tuple argument to positional parameters
f(**d)   # 1,2,3   ** scatters dictionary argument to positional paramerters

# f(s)   # TypeError: f() takes exactly 3 arguments (1 given)


def g(*args):
    'optional parameters, gather multiple arguments into tuple'
    print args

g()       # ()
g(1)      # (1,)
g(1,2,3)  # (1,2,3) 


def h(**kwargs):
    'keyword parameters, gather multiple keyword args into dictionary'
    print kwargs
   
h(a=1)      # { 'a':1 }
h(a=1, b=2) # { 'a':1, 'b':2 }
h(a=1, b=2, c=3) # { 'a':1, 'c':3, 'b':2 }

