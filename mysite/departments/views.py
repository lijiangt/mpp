# Create your views here.
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext

from models import Department,SmallDepartment,Building,Staff

def department_detail(request,id=None):
    department = get_object_or_404(Department,pk=id)
    return render_to_response('department_detail.html',{
                'department':department,
                },context_instance=RequestContext(request))

def department_list(request):
    departments = Department.objects.all()
    return render_to_response('department_list.html',{
                'department':departments,
                },context_instance=RequestContext(request))
    