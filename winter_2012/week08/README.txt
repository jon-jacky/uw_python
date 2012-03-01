
Django example (using sqlite) under django_site/ 

Database defined in SQL (also using sqlite) under sql_samples/

Here the Django site defines a similar database to the one defined
by the SQL script in sql_samples/mailing_list.  However this Django
models.py was written from scratch, it was NOT generated from the
database in sql_samples.

The Django site is configured to include the admin interface and the
databrowse facility.

To build and view the SQL database in sql_samples:

 $ sqlite3 mailing_list.db # this session creates and populates mailing_list.db
 sqlite> .read mailing_list
 sqlite> .read mailing_list_data
 ... error message about constraint failed is expected ...
 sqlite> .dump
 ... shows sql commands that would reconstruct database ...
 sqlite> .read mailing_list_queries
 ... shows formatted database contents ...

To build and view the Django site, including its database, in django_site:

 python manage.py syncdb
 ...
 ... answer prompts to add superuser with password for admin interface ...
 ...

 python manage.py runserver
 ... listening on port 8000 ...

The database is defined but empty -- it contains no data.  To populate
the database, you can use the Django admin interface.  Just point your
browser at 

 http://localhost:8000/admin/
