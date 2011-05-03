from django import forms
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext
from departments.models import Department,Building

def bmap(request,id=None):
    """building map on campus"""
    return render_to_response('bmap.html',
                {'building':get_object_or_404(Building,id=id),},
                context_instance=RequestContext(request))
def buildinglist(request):
    """list of building"""
    return render_to_response('building_list.html',
                {'buildings':Building.objects.all()},
                context_instance=RequestContext(request))
def gmap(request,id = None):
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
                'departments':Department.objects.all(),
                },context_instance=RequestContext(request))
