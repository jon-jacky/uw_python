"""
a confection
seen on Stack Overflow, from Active State - but try it first!
"""

a,b,c,d,e,f,g,h,i = 'abcdefghi'   # so we don't have to type a lot of quotes
lists = [[a,b,c],[d,e,f],[g,h,i]] # no quotes needed here

def f(lists):
    if not lists: return[]
    return map(lambda *row: list(row), *lists)

print lists
# print f(lists)     # what does this print?  why?

