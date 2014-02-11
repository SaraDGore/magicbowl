from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^magicbowl/admin/', include(admin.site.urls)),
    url(r'^magicbowl/$', include('bowls.urls')),
)
