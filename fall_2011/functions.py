"""
Functions are objects (can be assigned, passed as arguments, ...)
Objects have attributes (such as docstrings) used by Python or by your code
Functions can have keyword arguments (optional arguments, default arguments)
"""

def f(x):
    'square'    # docstring f.__doc__, used by help(f) or ... 
    return x**2

def g(x):
    'cube'
    return x**3

def integrate(f, dx=0.1, x0=0.0, x1=1.0):
    """
    integrate function f in steps of dx from x0 to x1
    defaults: dx = 0.1, x0 = 0.0, x1 = 1.0
    """
    integral = 0.0
    x = x0
    while x < x1:
        integral += dx * f(x)
        x += dx
    return integral

