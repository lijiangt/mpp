from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def index(request):
    page = settings.PAGES['home']
    apps = page.getApps()
    return render_to_response('index.html', {
                'page':page,
                'apps':apps,
                'appSize':len(apps),
    },context_instance=RequestContext(request))