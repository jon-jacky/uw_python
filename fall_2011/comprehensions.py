"""
More list comprehension explanations and examples
"""

from route import puget
from phones import phones, physics_dept

print phones

# use a loop to build up a list from a source, filter, and pattern:
def physics_people():
    names = []
    for (name, phone) in phones: # phones is the source
        if physics_dept(phone):  # physics_deptn(phone) is the filter
            names.append(name)   # name is the pattern
    return names

print physics_people()

# a list comprehension expresses the same thing in one expression
#     [ pattern for     item      in source if filter ]
print [ name    for (name, phone) in phones if physics_dept(phone) ]

# the pattern can be elaborate
print [ "%s's phone is %s" % (name,phone)
        for (name, phone) in phones if physics_dept(phone) ]


# note the difference between filter and conditional expr. in pattern

def odd(i): return i%2 # 1 (true) when i is odd, 0 (false) when even

print [ (i, 'odd') for i in range(5) if odd(i) ] # filter

print [ (i, 'odd' if odd(i) else 'even') for i in range(5) ] # pattern


# map pattern: apply a function to each element in the source

print [ odd(i) for i in range(5) ]

# built-in map function is an alternative

print map(odd, range(5)) # 

# filter pattern: use a filter (Boolean function) to select elements from source

print [ i for i in range(5) if odd(i) ]

# built-in filter function is an alternative

print filter(odd, range(5)) 


