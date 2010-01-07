# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template
from common.appenginepatch.ragendja.dbutils import get_object
from cms.models import Page, Category

def index(request):
    
    welcome     = get_object(Page, 'code =','home-welcome')
    services    = get_object(Page, 'code =','home-services')
    promotions  = get_object(Page, 'code =','home-promotions')
    
    news = get_object(Category, 'code =', 'news')
    current_news = news.pages_set.order('date_added').fetch(1)
    current_news = current_news[0] if current_news else None
    
    return direct_to_template(request, 'home.html', locals())