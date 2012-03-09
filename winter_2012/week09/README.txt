
Django books site example (using sqlite) under booksite/
This is a solution to the week 8 assignment.

Books database defined in SQL (also using sqlite) under bookdb/

The Django model was generated from the SQL database by

 python manage.py inspectdb > books/models.py

To build and view the Django site on your system, you will first have to
edit settings.py to change the absolute paths in DATABASES NAME and
TEMPLATE_DIRS.

To view the database (when running on localhost), point your browser at

 http://localhost:8000/books/

then follow the links.

The booksite sample also contains a test.py that demonstrates how to
test with django.test.  To run the tests: python manage.py test.  The
files add.py and test_add.py demonstrate testing with doctest and
unittest on a very simple example (that does not involved Django).

The sample under bookshop/ is similar to booksite, but with
authentication (users and logins) added.

The bookshop sample uses the database in bookshopdb, which includes
the database of authorized users.  When this site is running, if you
attempt to access http://localhost:8000/books/ when you have not yet
logged in, a login page appears.  Two users are authorized: jon
(password jacky) and brian (password dorsey).  After you have
successfully logged in, you can view the index and detail pages.  The
logged in user's username and a Logout link appears on index and
detail pages.  There is a Login link on the Logged Out page.

An interesting bookshop demonstration is to log in as two different
users at the same time. (You can do this on one machine, even
localhost, by using two different browsers, for example Firefox and
Safari on a Mac.)

An informative exercise would be to add a shopping cart to the
bookshop.  On each detail page, put an Add to Cart link.  On the index
and detail pages put a Shopping Cart link which goes to a shopping
cart page that is similar to the index page, but only lists the books
in the cart.
