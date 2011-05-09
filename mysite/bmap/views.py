from django import forms
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext
from departments.models import Department,Building
from schl.models import School

def bmap(request,id=None):
    """building map on campus"""
    return render_to_response('bmap.html',
                {'building':get_object_or_404(Building,id=id),},
                context_instance=RequestContext(request))
def buildinglist(request):
    """list of building"""
    return render_to_response('building_list.html',
                {'buildings':Building.objects.order_by("-name")},
                context_instance=RequestContext(request))
def gmap(request):
    """BUPT on google map """
    return render_to_response('gmap.html',
                {'building':get_object_or_404(Building,id=0),},
                 context_instance=RequestContext(request))
def cmap(request,id = None):
    """city transfer"""
    return render_to_response('cmap.html',
                context_instance=RequestContext(request))
def map(request):
    return render_to_response('map.html',
                context_instance=RequestContext(request))
def dmap(request,id=None):
    return render_to_response('dmap.html',
                {'department':get_object_or_404(Department,id=id),},
                context_instance=RequestContext(request))
def department_list(request):
    return render_to_response('d_list.html',{
                'departments':Department.objects.order_by("-name"),
                },context_instance=RequestContext(request))
def smap(request,id=None):
    return render_to_response('smap.html',
                {'schl':get_object_or_404(School,id=id),},
                context_instance=RequestContext(request))
def schl_list(request):
    return render_to_response('s_list.html',{
                'schl':School.objects.order_by("-name"),
                },context_instance=RequestContext(request))
def search(request):
    if 'filter' in request.GET:
        filter = request.GET['filter']
        if(filter):
            d = Department.objects.filter(name__icontains=filter)
            s = School.objects.filter(name__icontains=filter)
            b = Building.objects.filter(name__icontains=filter)
            
            if d:
                request.META.get('HTTP_REFERER', None) or '/'
                return render_to_response('dd_list.html',{
                    'departments':d,
                    },context_instance=RequestContext(request))            
            elif s :
                return render_to_response('ss_list.html',{
                    'schl':s,
                    },context_instance=RequestContext(request))           
            elif b :
                return render_to_response('bbuilding_list.html',
                    {'buildings':b,
                    },context_instance=RequestContext(request))
            else:
                return render_to_response('map.html',{
                    'error':'True'
                },
                    context_instance=RequestContext(request))
        else:
            return render_to_response('map.html',
                context_instance=RequestContext(request))
            
    else:
            return render_to_response('map.html',
                context_instance=RequestContext(request))
