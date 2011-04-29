from django.conf.urls.defaults import *

from main.views import main

urlpatterns = patterns('',
    url(r'^$', main, name='main',),
)
