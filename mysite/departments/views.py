from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext
from models import Department, SubDepartment, Building

def department_detail(request,id):
    return render_to_response('department_detail.html',{
                'department':get_object_or_404(Department,id=id),
                'subdepartments':SubDepartment.objects.filter(department=id),
                },context_instance=RequestContext(request))


def department_list(request):
    return render_to_response('department_list.html',{
                'departments':Department.objects.order_by("-name"),
                },context_instance=RequestContext(request))
    