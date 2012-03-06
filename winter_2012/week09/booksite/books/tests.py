"""
Demonstrate django.test

For now, trivial: just check that empty path gets 404, valid path gets 200
"""

from django.test import TestCase

class BooksTest(TestCase):
        
    def test_empty(self):
        # there must be a templates/404.html for this test to pass
        response = self.client.get('/')
        #print response.status_code
        self.assertEqual(response.status_code, 404) # no page

    def test_books(self):
        response = self.client.get('/books/')
        #print response.status_code
        self.assertEqual(response.status_code, 200) # index page
