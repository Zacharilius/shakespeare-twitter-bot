from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from .views import *

urlpatterns = [
    url(r'^$', shakespeare_twitter_bot, name='shakespeare_twitter_bot'),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'i18n/', include('django.conf.urls.i18n')),    
    url(r'^admin/', admin.site.urls),
]
