from appenginepatch.ragendja.dbutils import get_object_list
from home.models import Menu

def menu(request):

    return {
        'menu': get_object_list(Menu).order('num').fetch(1000)
    }
    