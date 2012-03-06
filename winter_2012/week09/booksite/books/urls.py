from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('books.views',
    url(r'^$', 'index'),
    url(r'^detail/(.*)$', 'detail'),
)
