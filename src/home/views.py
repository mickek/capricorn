# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template
from common.appenginepatch.ragendja.dbutils import get_object
from django.contrib.flatpages.models import FlatPage

def index(request):
    
    content = get_object(FlatPage, 'url =','home-content')
    
    return direct_to_template(request, 'home.html', {'content':content})