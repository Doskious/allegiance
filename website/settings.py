import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8#j*o#awh^2)p*v7!ap*=s91^_lycj8x&!jl*6ndajm-)s3)7&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['allegiance.bastion-rising.net', 'allegiance.bastion-rising.local', 'eva.local']


# Application definition





ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/New_York'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/s/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'public')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'website', 'static'),
)
SITE_ID = 1

#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader'
#)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors':
            [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.template.context_processors.csrf',
            'django.template.context_processors.request',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',
            'django.core.context_processors.static',
            'cms.context_processors.cms_settings',
            ],
#        'loaders':
#            [
#            'django.template.loaders.filesystem.Loader',
#            'django.template.loaders.app_directories.Loader',
#            'django.template.loaders.eggs.Loader'
#            ]
    }
},
]

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.contrib.messages.context_processors.messages',
#    'django.template.context_processors.i18n',
#    'django.template.context_processors.debug',
#    'django.template.context_processors.request',
#    'django.template.context_processors.media',
#    'django.template.context_processors.csrf',
#    'django.template.context_processors.tz',
#    'sekizai.context_processors.sekizai',
#    'django.core.context_processors.static',
#    'cms.context_processors.cms_settings'
#)

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'website', 'templates'),
#)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_style',
    'djangocms_column',
#    'djangocms_file',
#    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'stdimage',
#    'reversion',
    'website',
    'shlog',
#    'charsheet',
    'krynncal',
    'ehtest',
    'kthrone',
    'pathpor',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('charsheet.html', 'Character Sheet'),
    ('main.html', 'Frontpage Shlog Display'),
    ('por_list.html', 'Portfolio Listing')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.mysql', 'NAME': u'allegiance', 'HOST': u'localhost', 'USER': u'emma', 'PASSWORD': u'varnaitidewaterweaverrock', 'PORT': ''}
}
