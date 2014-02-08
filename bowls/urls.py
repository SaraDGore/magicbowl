from django.conf.urls import patterns, url

from bowls import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='mains')
)
