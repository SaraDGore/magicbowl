from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('bowls.urls')),
    url(r'^bowls/admin/', include(admin.site.urls)),
)
