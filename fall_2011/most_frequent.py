"""
Solution to Downey's ex 12.3

Write the function most_frequent that takes a string
and prints the letters in decreasing order of frequency ...
"""

from operator import itemgetter # used only for list.sort key= ... option

s = 'supercalifragilisticexpealidocious' # sample text for testing

# use Downey's histogram from 11.1 to get letter frequencies
def histogram(s):
    """
    s is a string
    return dictionary, keys are letters in s, values are their frequencies
    copied from Downey 11.1
    """
    d = dict()
    for c in s:
        if c not in d: # could use solution to Ex 11.2 to eliminate the if
            d[c] = 1
        else:
            d[c] += 1
    return d
    
def reverse_pairs(ts):
    """
    ts: list of pairs (tuples)
    returns new list of pairs, each pair is in reverse order
    """
    # use a loop
    reversed = []
    for first, second in ts:
        reversed += [(second, first)]   
        # reversed.append((second,first))  # this alternative works also
    return reversed

def most_frequent(s):
    """
    s is a string, print letters in s in decreasing order of frequency
    """
    # This calls reverse_pairs to reverse all the tuples before calling sort
    # similar to decorate-sort-undecorate pattern in Downey section 12.7
    freqs = histogram(s)
    freqs_ts = freqs.items()
    freqs_ts_r = reverse_pairs(freqs_ts) # sort by frequency not alph order
    freqs_ts_r.sort(reverse=True)
    for freq, letter in freqs_ts_r: # note reversed order in tuple
        print letter
        
# Alternatives

def reverse_pairs_2(ts):
    """
    ts: list of pairs (tuples)
    returns new list of pairs, each pair is in reverse order
    """
    # use a list comprehension
    return [(second,first) for first,second in ts ]

def most_frequent_2(s):
    """
    s is a string, print letters in s in decreasing order of frequency
    """
    # This version uses keyword arg to sort by second item in each tuple
    # See http://docs.python.org/howto/sorting.html
    freqs = histogram(s)
    freqs_ts = freqs.items()
    freqs_ts.sort(reverse=True, key = lambda pair: pair[1])
    # freqs_ts.sort(reverse=True, key = itemgetter(1)) # this alternative works too
    for letter, freq in freqs_ts:  # same order in tuple
        print letter

# Test

if __name__ == '__main__':
    print histogram(s)  
    most_frequent_2(s)

