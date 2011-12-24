"""
Assignment for week 6
http://staff.washington.edu/jon/uw_python/fall_2011/assign_6.txt

Write a function unlisted_words that takes two string arguments, a
sample string and a reference string, and returns a list of all the
words that appear in the sample string that do not appear in the
reference string.  ...
"""

import re # used by Norvig's words function

sample = 'aaa aaa Aaa AAA "AAA" $aaa \emph{aaa} bbb ccc ddd DDD aaa'
reference = 'aaa bbb ccc'

def words(text):
    """
    return list of cleaned-up unique words in text, copied from
    http://www.norvig.com/spell-correct.html
    """
    return re.findall('[a-z]+', text.lower())

def unlisted_words(sample, reference):
    sample_set = set(words(sample))
    reference_set = set(words(reference))
    return list(sample_set - reference_set)

if __name__ == '__main__':

    # demonstrate words function and set type callable
    print words(sample)
    print words(reference)
    print set(words(sample))
    print set(words(reference))

    # simple test case
    print unlisted_words(sample, reference)

    # spelling checker
    chapter = file('big.txt').read()
    dictionary = file('words').read()
    print
    print unlisted_words(chapter, dictionary)
    

