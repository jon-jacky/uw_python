"""
print nested data structure with increasing indentation at each level

  [ 'I....', 'II...', [ 'A...', 'B...' ], 'III....' ]

is printed

  I...
  II...
    A...
    B...
  III...
"""

outline = [ 'I....', 'II...', [ 'A...', [ 1, 2 ], 'B...' ], 'III....' ]

def print_nested(spaces, data):
    """
    print nested data with increasing indentation at each level
    data is list of non-lists (strings, numbers...) and/or nested lists
    spaces is indentation, typically '' (empty string) at top level
    """
    if isinstance(data, list):
        for item in data:
            print_nested(spaces + '  ', item) # recursive calls
    else:
        print '%s%s' % (spaces, data)         # base case

if __name__ == '__main__':
    print_nested('', outline)
