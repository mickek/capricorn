# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db
from django.db.models import signals
from common.appenginepatch.ragendja.dbutils import cleanup_relations

class Category(db.Model):
    
    name    =   db.StringProperty(required=True)
    code    =   db.StringProperty()
    
    order   =   db.IntegerProperty()
    
    class Meta:
        verbose_name = _('kategoria')
        verbose_name_plural = _('kategorie')
    
class Page(db.Model):
    
    title       =   db.StringProperty(required=True)
    url         =   db.StringProperty(required=True)
    code        =   db.StringProperty(required=False)
    
    stub        =   db.TextProperty()
    content     =   db.TextProperty()
    order       =   db.IntegerProperty(required=False)
    
    date_added  =   db.DateTimeProperty(auto_now=True)
    
    category    =   db.ReferenceProperty(Category, required=True, collection_name="pages_set")
    
    class Meta:
        verbose_name = _('strona')
        verbose_name_plural = _('strony')  
        
class Section(db.Model):
    
    code        =   db.StringProperty()
    content     =   db.TextProperty()
    
    class Meta:
        verbose_name = _('sekcja')
        verbose_name_plural = _('sekcje')  
      
    
signals.pre_delete.connect(cleanup_relations, sender=Page)