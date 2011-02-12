from django.conf.urls.defaults import patterns,include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$','views.index'),
    (r'^i18n.js$', direct_to_template, {'template': 'js_i18n.html', 'mimetype':'text/javascript'}),
#    (r'^page/','views.page'),
    (r'^admin/', include(admin.site.urls)),
    (r'^content/',include('cms.urls')),
    (r'^cms/',include('cms.urls_adm')),
)


if settings.MEDIA_ROOT and settings.DEBUG:
    urlpatterns += patterns('',
        (r'^s/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    )