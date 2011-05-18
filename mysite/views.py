from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.utils.translation import ugettext as _

def index(request):
    page = settings.PAGES.get(_('page-home'),None)
    if not page:
        page = settings.PAGES.get('page-home-cn',None)
    apps = page.getApps()
    return render_to_response('index.html', {
                'page':page,
                'apps':apps,
                'appSize':len(apps),
    },context_instance=RequestContext(request))
