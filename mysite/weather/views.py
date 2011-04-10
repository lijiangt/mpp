from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
import feedparser

weather_rss_url= 'http://weather.raychou.com/?/detail/54399/rss'

@cache_page(60 * 60)
def view(request):
    feed = feedparser.parse(weather_rss_url)
    return render_to_response('weather/view.html',{
                'feed':feed,
                'entries':feed.entries,
                },context_instance=RequestContext(request))