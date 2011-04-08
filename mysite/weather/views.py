from django.shortcuts import render_to_response
from django.template import RequestContext

import feedparser

weather_rss_url= 'http://weather.raychou.com/?/detail/54399/rss'

def view(request):
    feed = feedparser.parse(weather_rss_url)
    return render_to_response('weather/view.html',{
                'feed':feed,
                'entries':feed.entries,
                },context_instance=RequestContext(request))