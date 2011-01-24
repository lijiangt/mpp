from django.shortcuts import render_to_response
from django.template import RequestContext

from cms.models import Category 
def index(request):
    categories = Category.objects.order_by('-seqNum');
    return render_to_response('index.html', {
                'categories':categories,
    },context_instance=RequestContext(request))