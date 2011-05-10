from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
import pywapi

weather_rss_url= 'http://weather.raychou.com/?/detail/54399/rss'

#@cache_page(60 * 60)
def view(request):
    result = pywapi.get_weather_from_google('beijing',hl='zh_CN')
#    feed = feedparser.parse(weather_rss_url)
    return render_to_response('weather/view.html',{
                'result':result,
                },context_instance=RequestContext(request))