# -*- coding: utf-8 -*-
from ragendja.settings_pre import *

MEDIA_VERSION = 9

COMBINE_MEDIA = {
    'home.css':(
        'global/css/main.css',              
        'global/css/menu.css',
    ),
    'content.css':(
        'global/css/content.css',    
        'global/css/menu.css',          
    ),
    'gallery.css':(
        'global/css/content.css',    
        'global/css/menu.css',
        'global/css/gallery.css',
    ),    
    'menu.js':(
        'global/js/menu.js',
        'global/js/jquery.galleriffic.js'
    ),
}

# Change your email settings
if on_production_server: #@UndefinedVariable
    DEFAULT_FROM_EMAIL = 'kontakt@capricorn.pl'
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'capricorn_is_de_best'

USE_I18N = True
LANGUAGE_CODE = 'pl'

# Restrict supported languages (and JS media generation)
LANGUAGES = (
    ('pl', 'Polish'),    
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'ragendja.auth.context_processors.google_user',
    'context_processors.menu'    
)

MIDDLEWARE_CLASSES = (
    'ragendja.middleware.ErrorMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'ragendja.auth.middleware.HybridAuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    'cms.middleware.CmsFallbackMiddleware'
)

INSTALLED_APPS = (
    'blueprintcss',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.sites',
    'appenginepatcher',
    'ragendja',
    'mediautils',
    
    'cms',
    'home',
)

DATABASE_OPTIONS = {
    'remote_id': 'capricorn-med',
}

AUTH_USER_MODULE = 'ragendja.auth.hybrid_models'

from ragendja.settings_post import *