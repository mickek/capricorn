# -*- coding: utf-8 -*-
from google.appengine.ext import db


class Menu(db.Model):
    
    name    =   db.StringProperty()
    href    =   db.StringProperty()
    num     =   db.IntegerProperty()