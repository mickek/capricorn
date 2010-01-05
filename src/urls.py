# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from google.appengine.api import users
from django.views.generic.simple import redirect_to
from django.utils.html import escape

admin.autodiscover()

handler500 = 'ragendja.views.server_error'


urlpatterns = auth_patterns + patterns('',
    (r'^$', 'home.views.index'),    
    ('^admin/', include(admin.site.urls)),
) + urlpatterns