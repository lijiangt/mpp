from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.utils.translation import ugettext as _

def index(request):
    page = settings.PAGES.get(_('page-home'),None)
    if not page:
        page = settings.PAGES.get('page-home-cn',None)
    apps = page.getApps()
    user_agent = request.META.get('HTTP_USER_AGENT',None) 
    from wurfl import devices
    from pywurfl.algorithms import TwoStepAnalysis
    search_algorithm = TwoStepAnalysis(devices)
    device = devices.select_ua(unicode(user_agent), search=search_algorithm)
    print 'user_agent: %s   device: %s'%(user_agent,device.brand_name)
    print device.model_name
    return render_to_response('index.html', {
                'page':page,
                'apps':apps,
                'appSize':len(apps),
    },context_instance=RequestContext(request))
