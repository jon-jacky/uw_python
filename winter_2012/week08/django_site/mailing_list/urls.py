from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mailing_list.views',
    url(r'^$', 'index'),
    url(r'^name_list/$', 'name_list'), # mailing_list is name of app
    url(r'^phone_numbers/$', 'phone_numbers'),
    url(r'^query/$', 'query'),
    # more to come?
)
