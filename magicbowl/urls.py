from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bowls import views

from django.contrib import admin
admin.autodiscover()

'''Until I get a real landing page for this site.'''

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^magicbowl/admin/', include(admin.site.urls)),
    url(r'^magicbowl/$', include('bowls.urls')),
    
)

urlpatterns += staticfiles_urlpatterns()


