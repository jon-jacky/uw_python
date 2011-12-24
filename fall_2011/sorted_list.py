"""
  Exercise 5B - Write a function sorted_list that takes one list
  argument and returns a list with the same elements but sorted.  This
  function must NOT change the list in the caller.  You may use the
  list sort method, but you may NOT use the built-in library function
  'sorted' in your solution.  Write your function in a module also
  named sorted_list that defines at least two test lists.  In your
  module, call your function on each of these lists and print the
  results.  Also, print both lists after calling the function to show
  that they have not changed.
"""

from copy import copy

l1 = list('hgfedcba')
l2 = list('bbbbaaaa')
          
def sorted_list(l):
    """
    l list, returns new list with elements sorted
    """
    lc = copy(l)  # must copy to prevent mutating input l
    lc.sort()     # sorts lc in place, returns None        
    return lc     # return sorted lc

if __name__ == '__main__':
    print '%s -> %s' % (l1, sorted_list(l1))
    print '%s -> %s' % (l2, sorted_list(l2))
    print '%s, %s are unchanged' % (l1, l2)
