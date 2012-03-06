from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('books.views',
    url(r'^$', 'index'),
    url(r'^detail/(.*)$', 'detail'),
    url(r'^login/(.*)$', 'login'),
    url(r'^login_user/$', 'login_user'),
)
