
Django books site example (using sqlite) under booksite/

Books database defined in SQL (also using sqlite) under bookdb/

The Django model was generated from the SQL database by

 python manage.py inspectdb > books/models.py

To build and view the Django site on your system, you will first have to
edit settings.py to change the absolute paths in DATABASES NAME and
TEMPLATE_DIRS.

To view the database (when running on localhost), point your browser at

 http://localhost:8000/books/

then follow the links.
