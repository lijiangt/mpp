from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext

from datetime import date,datetime,timedelta
from django.utils.translation import ugettext_lazy as _

from models import Event

from departments.models import Department

WEEK_DAY=(_('Sunday'), _('Monday'), _('Tuesday'), _('Wednesday'), _('Thurday'), _('Friday'), _('Saturday'))

def index(request):
    return HttpResponseRedirect(date.today().strftime('date/0/%Y/%m/%d/'))


def by_day(request,year,month,day):
    start = datetime(int(year),int(month),int(day))
    end = start+timedelta(days=1)
    events = Event.objects.filter(date__range=(start, end)).order_by('date')
    return render_to_response('event/list_event_by_day.html', {
                'events':events,
                'previous':start-timedelta(days=1),
                'today':start,
                'next':end,
                'weekday':WEEK_DAY[int(start.strftime('%w'))],
                'previous_weekday':WEEK_DAY[int((start-timedelta(days=1)).strftime('%w'))],
                'next_weekday':WEEK_DAY[int(end.strftime('%w'))],
                'display_type':0,
    },context_instance=RequestContext(request))

def view(request,year,month,day,id):
    day = datetime(int(year),int(month),int(day))
    event = get_object_or_404(Event,pk=id)
    return render_to_response('event/event.html', {
                'event':event,
                'day':day,
                'weekday':WEEK_DAY[int(day.strftime('%w'))],
    },context_instance=RequestContext(request))

def list_type(request):
    return render_to_response('event/list_type.html',{
                'types':Event.CATEGORY_CHOICES,
                'today':date.today(),
                },context_instance=RequestContext(request))

def by_type(request,type,year,month,day):
    start = datetime(int(year),int(month),int(day))
    end = start+timedelta(days=1)
    events = Event.objects.filter(category__exact=type).filter(date__range=(start, end)).order_by('date')
    category_name = None
    for type_id,type_name in Event.CATEGORY_CHOICES:
        if type_id == int(type):
            category_name = type_name
    return render_to_response('event/list_event_by_day.html', {
                'events':events,
                'previous':start-timedelta(days=1),
                'today':start,
                'next':end,
                'weekday':WEEK_DAY[int(start.strftime('%w'))],
                'previous_weekday':WEEK_DAY[int((start-timedelta(days=1)).strftime('%w'))],
                'next_weekday':WEEK_DAY[int(end.strftime('%w'))],
                'category_name':category_name,
                'display_type':1,
    },context_instance=RequestContext(request))

def view_by_type(request,type,year,month,day,id):
    return view(request,year,month,day,id)

def list_dep(request):
    return render_to_response('event/list_dep.html',{
                'deps':Department.objects.order_by("name"),
                'today':date.today(),
                },context_instance=RequestContext(request))

def by_dep(request,dep_id,year,month,day):
    start = datetime(int(year),int(month),int(day))
    end = start+timedelta(days=1)
    dep = get_object_or_404(Department,pk=dep_id)
    events = Event.objects.filter(department=dep_id).filter(date__range=(start, end)).order_by('date')
    return render_to_response('event/list_event_by_day.html', {
                'events':events,
                'previous':start-timedelta(days=1),
                'today':start,
                'next':end,
                'weekday':WEEK_DAY[int(start.strftime('%w'))],
                'previous_weekday':WEEK_DAY[int((start-timedelta(days=1)).strftime('%w'))],
                'next_weekday':WEEK_DAY[int(end.strftime('%w'))],
                'dep':dep,
                'display_type':2,
    },context_instance=RequestContext(request))

def view_by_dep(request,dep_id,year,month,day,id):
    return view(request,year,month,day,id)