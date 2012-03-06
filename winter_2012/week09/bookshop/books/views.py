"""
views.py for bookshop sample including authorization (users and logins)

Prepare settings.py per https://docs.djangoproject.com/en/1.3/topics/auth/

To authorize users: python manage.py shell  then
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('jon', 'jon@uw.edu', 'jacky')
>>> user.save()
... etc. ...

NOT WORKING - LOGIN NEVER SUCCEEDS
"""

from books.models import Books
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import Context, loader
from django.template import RequestContext

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

@csrf_protect
def login(request, x):
    c = { 'form': LoginForm(request.POST) }
    return render_to_response('login.html', c, 
                              context_instance=RequestContext(request))

# copied from sample at https://docs.djangoproject.com/en/1.3/topics/auth/
def login_user(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # DEBUG print - will this appear in dev server progress messages?
        print 'username %s, password %s, user %s' % (username,password,user)
        if user is not None:
            if user.is_active:
                login(request, user)
                print ' authenticated %s' % request.user.is_authenticated()
                return HttpResponseRedirect('/books/')
            else:
                pass # FIXME
                # Return a 'disabled account' error message
        else:
            pass # FIXME 
            # Return an 'invalid login' error message.

# decorator recommended in https://docs.djangoproject.com/en/1.3/topics/auth/
@login_required(login_url='/books/login/')
def index(request):
    # return HttpResponse("books index to come ...") # placeholder
    # based on first example in Django tutorial03
    books = Books.objects.all()
    t = loader.get_template('index.html')
    c = Context({'books':books})
    return HttpResponse(t.render(c))

@login_required(login_url='/books/login/')
def detail(request, isbn):
    # return HttpResponse("books detail for isbn %s to come ..." % isbn) # placeholder
    book = Books.objects.get(pk=isbn)
    t = loader.get_template('detail.html')
    c = Context({'book':book})
    return HttpResponse(t.render(c))    
