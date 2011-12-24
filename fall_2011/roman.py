"""
Roman numeral to integer converter, based on Janos Juhasz in
http://mail.python.org/pipermail/tutor/2007-5March.txt
Turn Juhasz' script into a function, streamline, revise names and comments
"""

# lookup table from single Roman numeral to integer
numerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def roman_to_int(roman):
    """
    Convert string of roman numerals to an integer
    Numerals may be upper or lowercase, other chars raise KeyError
    """
    # convert string of roman numerals to list of integers
    digits = [numerals[ch] for ch in roman.upper()] 
    result = 0
    while digits:
        digit = digits.pop(0) # take leftmost digit
        # if a larger digit remains, subtract this one from result
        if digits and digit < max(digits): digit = -digit 
        result += digit
    return result

# just to demo comprehension, define this function at module level
def digits(roman): return [numerals[ch] for ch in roman.upper()]

if __name__ == '__main__':
    pass
    # In Mac Lion IDLE, F5 on module with raw_input hangs IDLE
##    while True:
##        roman = raw_input('Enter a roman number: ')
##        if not roman: break # loop until empty input
##        print roman, '=', roman_to_int(roman)

