"""
Demonstrate unit test

The test class inherits unittest.TestCase
The test methods in the test class must begins with 'test'
and must use the assert* methods from the unittest module
(not the plain Python assert statement).

To test the add module with these unit tests:

 python test_add.py

"""

import unittest
from add import add

class TestAdd(unittest.TestCase):

    def test_6_6(self):
        self.assertEqual(6+6, add(6,6))

    def test_6_7(self):
        self.assertEqual(6+7, add(6,7))

    def test_6_8(self):
        self.assertEqual(6+8, add(6,8))

if __name__ == '__main__':
    unittest.main()
