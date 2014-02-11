from django.conf.urls import patterns, url, include

from bowls import views


urlpatterns = patterns('',
    url(r'^$', views.main, name='mains'), 
)
