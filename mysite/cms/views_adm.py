from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.views.generic import list_detail
from django.template import RequestContext
from django.conf import settings

from templatetags import title_field_html

from models import Category,Article

def category_edit(request):
    pass

def category_index(request):
    if request.method == 'GET':
        pageSize = int(request.GET.get('pageSize',settings.DEFAUTL_PAGE_SIZE))
        page = int(request.GET.get('page',1))
        order_str = title_field_html.get_order_str(request)
        if not order_str:
            order_str = '-seqNum'
        queryset = Category.objects.all().order_by(order_str)
        return list_detail.object_list(request, 
                   queryset = queryset,
                   paginate_by=pageSize,
                   page=page)  
    elif request.method == 'POST':
        pass
    else:
        raise Http404

def category_detail(request,id):
    pass

def article_edit(request,category_id):
    pass

def article_index(request,category_id):
    pass

def article_detail(request,category_id,id):
    pass