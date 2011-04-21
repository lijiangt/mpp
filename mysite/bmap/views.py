from django import forms
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext
from departments.models import Department,Building

def bmap(request,id = None):
    return render_to_response('bmap.html',
                {'department':get_object_or_404(Department,id=id),
                },context_instance=RequestContext(request))
def bmap_default(request):
    return render_to_response('buptmap.html',
                {'building':get_object_or_404(Building,id=0),
                },context_instance=RequestContext(request))
           
