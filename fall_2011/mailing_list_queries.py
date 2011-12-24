"""
Based on SQL queries in http://philip.greenspun.com/sql/introduction.html
"""

import sqlite3

conn = sqlite3.connect('mailing_list.db')
c = conn.cursor()

def query(q):
    'Execute query q and print results'
    c.execute(q)
    print '\n%s\n' % q
    for row in c:
        print row
    
q1 = 'select * from mailing_list'
query(q1)

q2 = 'select * from phone_numbers'
query(q2)


q3 = """select * from mailing_list, phone_numbers
  where mailing_list.email = phone_numbers.email"""
query(q3)

# now the iterator c is used up.  Refresh it, save contents

print "\n%s, save results in variable 'rows'\n" % q1
c.execute(q1)
rows = [ row for row in c ]
print rows
