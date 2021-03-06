# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from google.appengine.api import users
from django.views.generic.simple import redirect_to
from django.utils.html import escape
from django.views.generic.simple import direct_to_template

admin.autodiscover()

handler500 = 'ragendja.views.server_error'


urlpatterns = auth_patterns + patterns('',
    (r'^$', 'home.views.index'),
    (r'^galeria/$', 'home.views.galery'),
    ('^cms/', include('cms.urls')),
    (r'^drukuj_kupon/$',             direct_to_template, {'template': 'coupon_print.html'}, 'coupon_print'),
    (r'^kupon/$',             direct_to_template, {'template': 'coupon.html'}),    
    ('^admin/', include(admin.site.urls)),
) + urlpatterns