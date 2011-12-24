"""
 Exercise 5A - Write a function sorted_string that takes one string
  argument and returns a string with the same characters but sorted in
  lexical (alphabetic) order.  You may use the list sort method, but
  you may NOT use the built-in library function 'sorted' in your
  solution.  Write your function in a module also named sorted_string
  that defines at least two test strings.  In your module, call your
  function on each of these strings and print the results.
"""

s = 'hgfedcba'
t = 'bbbbaaaa'

def sorted_string(s):
    """
    s string, returns new string with same characters as s but sorted
    """
    l = list(s) # sort requires mutable object, convert to list
    l.sort()
    return ''.join(l)  # convert sorted list back to string

if __name__ == '__main__':
    print '%s -> %s' % (s, sorted_string(s))
    print '%s -> %s' % (t, sorted_string(t))
