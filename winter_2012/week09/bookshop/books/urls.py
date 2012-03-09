from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# login,logout from http://www.djangobook.com/en/2.0/chapter14/
# including import above

urlpatterns = patterns('books.views',
    url(r'^$', 'index'),
    url(r'^detail/(.*)$', 'detail'),
    url(r'^accounts/login/(.*)$',  login),
    url(r'^accounts/logout/(.*)$', logout),
)
