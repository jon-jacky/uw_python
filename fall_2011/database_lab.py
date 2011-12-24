
from pprint import pprint

mailing_list = set([('philg@mit.edu','Philip Greenspun'),
                    ('ogrady@fastbuck.com', "Michael O'Grady")])


phone_numbers = set([('ogrady@fastbuck.com','work','(800) 555-1212'),
                    ('ogrady@fastbuck.com','home','(617) 495-6000'),
                    ('philg@mit.edu','work','(617) 253-8574')])

# select * from mailing_list;
pprint(mailing_list)
print # blank line

# select * from phone_numbers;
pprint(phone_numbers)
print

# select * from mailing_list, phone_numbers
#   where mailing_list.email = phone_numbers.email;
pprint([(email1, name1, email2, loc, number)
          for email1,name1 in mailing_list
          for email2, loc, number in phone_numbers
          if email1 == email2 ])



