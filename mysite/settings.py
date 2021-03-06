DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mpp',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
import os
PROJECT_ROOT = os.path.dirname(__file__)
MEDIA_ROOT = '%s/s' % PROJECT_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/s'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/s_admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hvb(-s#9p%f-k@xs*hk8_pbglaic#eu#0!6!3#y9qs+ak_o6o+'

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.i18n",
"django.core.context_processors.request",
"django.core.context_processors.media",
"django.core.context_processors.csrf",
'wurfl.context_processors.wurfl_device',
'wurfl.context_processors.device_specific_media',
"django.contrib.messages.context_processors.messages")


if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS += ("django.core.context_processors.debug",)
    TEMPLATE_CONTEXT_PROCESSORS += ("wurfl.context_processors.print_info",)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'wurfl.middleware.WurflMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

if DEBUG:
    MIDDLEWARE_CLASSES += ('common.middleware.SqlPrintingMiddleware',)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
#    'polls',
    'cms',
    'mysite',
    'feedback',
    'departments',
    'schl',
    'bmap',
    'weather',
    'event',
)

CACHES = {
'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'LOCATION': 'unique-snowflake'
    }
}
if not DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
#print CACHES.get('default',None).get('BACKEND',None)

SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
USE_L10N = True
CATEGORY_ICON_PATH='icon/%Y/%j'
CATEGORY_DEFAULT_ICON_PATH=MEDIA_URL+'/default.png'
ARTICLE_PIC_PATH='pic/%Y/%j'
LOGIN_REDIRECT_URL='/cms/'
LOGIN_URL = '/accounts/login'
LOGOUT_REDIRECT_URL=LOGIN_URL

FILE_UPLOAD_IMAGE_MAX_SIZE = 2 #M
FILE_UPLOAD_IMAGE_TYPE=('png','gif','jpg','jpeg')
FILE_UPLOAD_IMAGE_SAVE_PATH=MEDIA_ROOT+'/upload'
FILE_UPLOAD_IMAGE_URL_PATH=MEDIA_URL+'/upload'

gettext_noop = lambda s: s

LANGUAGES=(
           ('zh-cn',gettext_noop('Chinese')),
           ('en',gettext_noop('English')),
)

DEFAUTL_PAGE_SIZE = 20
DEFAULT_THEME = 'default'
EXTEND_HTTP_METHOD='__http_method'
from base import Page,Provider
PAGES = {
    'page-home-cn':Page('Bupt Mobile Portal',providers=[
#           Provider('cms.app.CmsApp',app_label='today_event_cn'),
           Provider('base.GenericApp',local_name='Today Event',url='/event/',iconUrl='/s/event.png'),
           Provider('cms.app.CmsApp',app_label='bupt_news_cn'),
           Provider('base.GenericApp',local_name='Schools List',url='/schl/',iconUrl='/s/schl.png'),
           Provider('base.GenericApp',local_name='Departments List',url='/departments/',iconUrl='/s/department.png'),
           Provider('cms.app.CmsApp',app_label='school_info_cn'),
#           Provider('cms.app.CmsApp',app_label='fast_track_cn'),
           Provider('cms.app.CmsApp',app_label='bus_info_cn'),
           Provider('cms.app.CmsApp',app_label='security_info_cn'),
           Provider('base.GenericApp',local_name='Weather Report',url='/weather/',iconUrl='/s/weather.png'),
           Provider('base.GenericApp',local_name='BUPT Map',url='/bmap/',iconUrl='/s/map.png'),
#           Provider('base.GenericApp',local_name='Mobile Card',url='/s/mcard/index.html',iconUrl='/s/mcard.png'),
#           Provider('base.GenericApp',local_name='Mobile VOD',url='/s/mvod/index.html',iconUrl='/s/mvod.png'),
#           Provider('base.GenericApp',local_name='Mobile Library',url='/s/mlibrary/index.html',iconUrl='/s/mlibrary.png'),
#           Provider('base.GenericApp',local_name='Mobile Dinning',url='/s/mdinner/index.html',iconUrl='/s/mdinner.png'),
#	   Provider('base.GenericApp',local_name='Course Info',url='/s/mcourse/index.html',iconUrl='/s/mcourse.png'),
#	   Provider('base.GenericApp',local_name='Campus Cam',url='/s/mcam/index.html',iconUrl='/s/mcam.png'),
#	   Provider('base.GenericApp',local_name='Talk to President',url='/s/mguestbook/index.html',iconUrl='/s/mgustbook.png'),
#		   Provider('base.GenericApp',local_name='Campus Navi',url='/s/mcampus/index.html',iconUrl='/s/mcampus.png'),
#			   Provider('base.GenericApp',local_name='Mobile OA',url='/s/moa/index.html',iconUrl='/s/moa.png'),
   #           Provider('cms.app.CmsApp',app_label='about_cn'),
                                               ]),
    'page-home':Page('Bupt Mobile Portal',providers=[
            Provider('base.GenericApp',local_name='Today Event',url='/event/',iconUrl='/s/event.png'),
            Provider('cms.app.CmsApp',app_label='bupt_news'),
            Provider('cms.app.CmsApp',app_label='school_info'),
            Provider('cms.app.CmsApp',app_label='fast_track'),
            Provider('cms.app.CmsApp',app_label='bus_info'),
            Provider('cms.app.CmsApp',app_label='security_info'),
            Provider('base.GenericApp',local_name='Weather Report',url='/weather/',iconUrl='/s/weather.png'),
            Provider('base.GenericApp',local_name='Departments List',url='/departments/',iconUrl='/s/department.png'),
            Provider('base.GenericApp',local_name='BUPT Map',url='/bmap/',iconUrl='/s/map.png'),
            Provider('base.GenericApp',local_name='Schools List',url='/schl/',iconUrl='/s/schl.png'),
#           Provider('base.GenericApp',local_name='Mobile Card',url='/s/mcard/index.html',iconUrl='/s/mcard.png'),
#           Provider('base.GenericApp',local_name='Mobile VOD',url='/s/mvod/index.html',iconUrl='/s/mvod.png'),
#           Provider('base.GenericApp',local_name='Mobile Library',url='/s/mlibrary/index.html',iconUrl='/s/mlibrary.png'),
#           Provider('base.GenericApp',local_name='Mobile Dinning',url='/s/mdinner/index.html',iconUrl='/s/mdinner.png'),
#       Provider('base.GenericApp',local_name='Course Info',url='/s/mcourse/index.html',iconUrl='/s/mcourse.png'),
#       Provider('base.GenericApp',local_name='Campus Cam',url='/s/mcam/index.html',iconUrl='/s/mcam.png'),
#       Provider('base.GenericApp',local_name='Talk to President',url='/s/mguestbook/index.html',iconUrl='/s/mgustbook.png'),
#           Provider('base.GenericApp',local_name='Campus Navi',url='/s/mcampus/index.html',iconUrl='/s/mcampus.png'),
#               Provider('base.GenericApp',local_name='Mobile OA',url='/s/moa/index.html',iconUrl='/s/moa.png'),
                                            ]),
}

if False:
    print gettext_noop('Bupt Mobile Portal')
    print gettext_noop('Today Event')
    print gettext_noop('Departments List')
    print gettext_noop('BUPT Map')
    print gettext_noop('Schools List')

    print gettext_noop('About Site')
    
    print gettext_noop('Mobile Card')
    print gettext_noop('Mobile VOD')
    print gettext_noop('Mobile Library')
    print gettext_noop('Mobile Dinning')
    print gettext_noop('Course Info')  
    print gettext_noop('Campus Cam')
    print gettext_noop('Talk to President')
    print gettext_noop('Campus Navi')
    print gettext_noop('Mobile OA')

