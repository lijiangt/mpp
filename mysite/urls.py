from django.conf.urls.defaults import patterns,include
from django.conf import settings
from django.template import RequestContext
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$','views.index'),
    (r'^i18n.js$', direct_to_template, {'template': 'js_i18n.html', 'mimetype':'text/javascript'}),
    (r'^accounts/login$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout$', 'django.contrib.auth.views.logout',{'next_page':settings.LOGOUT_REDIRECT_URL}),
#    (r'^page/','views.page'),
    (r'^admin/', include(admin.site.urls)),
    (r'^content/',include('cms.urls')),
    (r'^cms/',include('cms.urls_adm')),
    (r'^department/',include('departments.urls')),
    (r'^feedback/',include('feedback.urls')),
)


if settings.MEDIA_ROOT and settings.DEBUG:
    urlpatterns += patterns('',
        (r'^s/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    )
    
def _404(request):
    return render_to_response('404.html', context_instance=RequestContext(request))
def _500(request):
    return render_to_response('500.html', context_instance=RequestContext(request))

handler404 = _404
handler500 = _500