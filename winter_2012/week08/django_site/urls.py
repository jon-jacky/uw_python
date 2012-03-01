from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# for databrowse
from django.contrib import databrowse
from mailing_list.models import MailingList, PhoneNumbers

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_site.views.home', name='home'),
    # url(r'^django_site/', include('django_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # quoted include args follow example in tutorial03
    url(r'^mailing_list/', include('mailing_list.urls')),
    url(r'^databrowse/(.*)', databrowse.site.root),
)
