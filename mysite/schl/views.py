from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext
from models import School, SubDep

def schl_detail(request,id):
    return render_to_response('schl_detail.html',{
                'schl':get_object_or_404(School,id=id),
                'subdep':SubDep.objects.filter(school=id),
                },context_instance=RequestContext(request))


def schl_list(request):
    return render_to_response('schl_list.html',{
                'schl':School.objects.order_by("-name"),
                },context_instance=RequestContext(request))
