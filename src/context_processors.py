from ragendja.dbutils import get_object_list
from cms.models import Category
import logging

def menu(request):

    menu_items = get_object_list(Category).order('order').fetch(100)
    menu = []

    for el in (cc for cc in menu_items if cc.code != 'news'):
        menu.append( (el,el.pages_set.order('order').fetch(10),) )

    return {
            'menu':menu
    }
    