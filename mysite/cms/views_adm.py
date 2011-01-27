from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext

from models import Category,Article

def category_edit(request):
    pass

def category_index(request):
    pass

def category_detail(request,id):
    pass

def article_edit(request,category_id):
    pass

def article_index(request,category_id):
    pass

def article_detail(request,category_id,id):
    pass