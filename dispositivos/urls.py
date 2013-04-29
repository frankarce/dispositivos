from django.conf.urls import patterns, include, url
from dispo.views import  index , device, indexlocal
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url (r'^index/(?P<id>\w+)$', index ),
    url (r'^indexlocal/(?P<id>\w+)$', indexlocal ),
    url (r'^device/(?P<id>\w+)$', device ),
    # Examples:
    # url(r'^$', 'dispositivos.views.home', name='home'),
    # url(r'^dispositivos/', include('dispositivos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
