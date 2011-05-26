from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext

from datetime import date,datetime,timedelta

from models import Event

def index(request):
    return HttpResponseRedirect(date.today().strftime('%Y/%m/%d/'))


def by_day(request,year,month,day):
    start = datetime(int(year),int(month),int(day))
    end = start+timedelta(days=1)
    events = Event.objects.filter(date__range=(start, end)).order_by('date')
    return render_to_response('event/list_event_by_day.html', {
                'events':events,
                'previous':start-timedelta(days=1),
                'today':start,
                'next':end,
    },context_instance=RequestContext(request))

def view(request,year,month,day,id):
    day = datetime(int(year),int(month),int(day))
    event = get_object_or_404(Event,pk=id)
    return render_to_response('event/event.html', {
                'event':event,
                'day':day,
    },context_instance=RequestContext(request))
