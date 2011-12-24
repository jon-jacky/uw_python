"""
Phone number database
"""

# A list of tuples can be a simple database

phones = [('Jon', 4117),
          ('Doug', 6218),
          ('Aki', 6014),
          ('Alan', 4017)]

# blocks of phone numbers are assigned to departments

def physics_dept(phone):
    return 4000 <= phone < 5000

# A list comprehension can be a database query:
#
# [ pattern for item in source if filter ]

# names of people in the physics department

physics_people = [ name for (name, phone) in phones if physics_dept(phone) ]

if __name__ == '__main__':
    print physics_people

    
    

