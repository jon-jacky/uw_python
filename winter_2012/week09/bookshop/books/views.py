"""
views.py for bookshop sample including authorization (users and logins)

Prepare settings.py per https://docs.djangoproject.com/en/1.3/topics/auth/

To authorize users: python manage.py shell  then
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('jon', 'jon@uw.edu', 'jacky')
>>> user.save()
... etc. ...
"""

from books.models import Books
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Context, loader

@login_required
def index(request):
    # based on first example in Django tutorial03
    books = Books.objects.all()
    t = loader.get_template('index.html')
    c = Context({'books':books, 'username':request.user.username})
    return HttpResponse(t.render(c))

@login_required
def detail(request, isbn):
    book = Books.objects.get(pk=isbn)
    t = loader.get_template('detail.html')
    c = Context({'book':book, 'username':request.user.username})
    return HttpResponse(t.render(c))    
