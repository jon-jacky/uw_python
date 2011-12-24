"""
Demonstrate sets to solve this problem:

"Filenames ...may only contain lowercase letters, numbers, the hyphen,
underscore, and period characters."
"""

from string import ascii_letters, digits

def valid_filename(fname):
    return (set(fname).issubset(ascii_letters + digits + '.-_'))

fn1 = 'sets_demo.py'
fn2 = '/src/sets_demo.py'
fn3 = 'C:\python\sets_demo.py'

print fn1, set(fn1), valid_filename(fn1)
print fn2, set(fn2), valid_filename(fn2)
print fn3, set(fn3), valid_filename(fn3)
