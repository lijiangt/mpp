from urllib import urlencode

from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.views.generic import list_detail,create_update
from django.template import RequestContext
from django.conf import settings
from django.forms import ModelForm

from templatetags import title_field_html

from models import Category,Article

class CategoryForm(ModelForm):
    class Meta:
        model = Category

def category_edit(request):
    if request.GET and request.GET.has_key('id'):
        id = request.GET['id']
        category = get_object_or_404(Category,pk=id)
        f = CategoryForm(instance=category)
        return render_to_response('cms/category_form.html', {
                'form':           f,
                "submit_times":   -1,
                'display_cancel':'true',
                'ext_query_str': request.GET.get('ext_query_str',''),
                'id':             id,
                },context_instance=RequestContext(request))
    else:
        f = CategoryForm()
        return render_to_response('cms/category_form.html', {
                'form':            f,
                "submit_times":   -1,
                'display_cancel':'true',
        },context_instance=RequestContext(request))

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
        f = CategoryForm(request.POST, request.FILES)
        if f.is_valid():
            category = f.save(commit=False)
            category.save()
            return HttpResponseRedirect(category.id)
        else:
            return render_to_response('cms/category_form.html', {
                    'form':        f,
                    "submit_times":int(request.POST['submit_times']) - 1,
                    'display_cancel':request.POST.get('display_cancel','true'),
                    },context_instance=RequestContext(request))
    raise Http404

def category_detail(request,id):
    if request.method == 'GET':
        category = get_object_or_404(Category,pk=id)
        pageSize = int(request.GET.get('pageSize',settings.DEFAUTL_PAGE_SIZE))
        page = int(request.GET.get('page',1))
        order_str = title_field_html.get_order_str(request)
        if not order_str:
            order_str = '-viewTimes'
        extra_context = {'category':category}
        queryset = Article.objects.filter(category=id).order_by(order_str)
        return list_detail.object_list(request, 
                   queryset = queryset,
                   paginate_by=pageSize,
                   page=page,
                   extra_context=extra_context,
                   template_name='cms/category_detail.html')
#        return list_detail.object_detail(request,
#                                 queryset= Category.objects.all(),
#                                 object_id=id,
#                                 extra_context=extra_context)
    elif request.method == 'POST':
        method = request.POST.get(settings.EXTEND_HTTP_METHOD,None) 
        if method == 'PUT':
            category = get_object_or_404(Category,pk=id)
            f = CategoryForm(request.POST, request.FILES,instance=category)
            if f.is_valid():
                f.save()
                ext_query_str = request.POST.get('ext_query_str','')
                if ext_query_str:
                    ext_query_str = '%s%s'%('?',urlencode({'ext_query_str':ext_query_str}))
                return HttpResponseRedirect('%s%s'%(id,ext_query_str))
            else:
                return render_to_response('cms/category_form.html', {
                                        'form':       f,
                                        "submit_times":int(request.POST['submit_times'])-1,
                                        'id':id,
                                        'display_cancel':request.POST.get('display_cancel','true'),
                                        'ext_query_str':request.POST.get('ext_query_str',''),
                                    },context_instance=RequestContext(request))
        elif method == 'DELETE':
            ext_query_str = request.POST.get('ext_query_str','')
            if ext_query_str:
                ext_query_str = '?'+ext_query_str
            return create_update.delete_object(request,
                               model=Category,
                               object_id=id,
                               post_delete_redirect='./%s'%ext_query_str)
    raise Http404

class ArticleForm(ModelForm):
    class Meta:
        model = Article
#        exclude = ('category','viewTimes',)

def article_edit(request,category_id):
    if request.GET and request.GET.has_key('id'):
        id = request.GET['id']
        article = get_object_or_404(Article,pk=id)
        f = ArticleForm(instance=article)
        return render_to_response('cms/article_form.html', {
                'form':           f,
                "submit_times":   -1,
                'display_cancel':'true',
                'ext_query_str': request.GET.get('ext_query_str',''),
                'id':             id,
                },context_instance=RequestContext(request))
    else:
        f = ArticleForm()
        return render_to_response('cms/article_form.html', {
                'form':            f,
                "submit_times":   -1,
                'display_cancel':'true',
        },context_instance=RequestContext(request))

def article_index(request,category_id):
    if request.method == 'GET':
        return HttpResponseRedirect('../%s'%category_id)
    elif request.method == 'POST':
        f = ArticleForm(request.POST, request.FILES)
        if f.is_valid():
            category = get_object_or_404(Category,pk=category_id)
            article = f.save(commit=False)
            article.category = category
            article.save()
            return HttpResponseRedirect(article.id)
        else:
            return render_to_response('cms/article_form.html', {
                    'form':        f,
                    "submit_times":int(request.POST['submit_times']) - 1,
                    'display_cancel':request.POST.get('display_cancel','true'),
                    },context_instance=RequestContext(request))
    raise Http404

def article_detail(request,category_id,id):
    if request.method == 'GET':
        return list_detail.object_detail(request,
                                 queryset= Article.objects.filter(category=category_id),
                                 object_id=id)
    elif request.method == 'POST':
        method = request.POST.get(settings.EXTEND_HTTP_METHOD,None) 
        if method == 'PUT':
            article = get_object_or_404(Article,pk=id)
            f = CategoryForm(request.POST, request.FILES,instance=article)
            if f.is_valid():
                f.save()
                ext_query_str = request.POST.get('ext_query_str','')
                if ext_query_str:
                    ext_query_str = '%s%s'%('?',urlencode({'ext_query_str':ext_query_str}))
                return HttpResponseRedirect('%s%s'%(id,ext_query_str))
            else:
                return render_to_response('cms/article_form.html', {
                                        'form':       f,
                                        "submit_times":int(request.POST['submit_times'])-1,
                                        'id':id,
                                        'display_cancel':request.POST.get('display_cancel','true'),
                                        'ext_query_str':request.POST.get('ext_query_str',''),
                                    },context_instance=RequestContext(request))
        elif method == 'DELETE':
            ext_query_str = request.POST.get('ext_query_str','')
            if ext_query_str:
                ext_query_str = '?'+ext_query_str
            return create_update.delete_object(request,
                               model=Article,
                               object_id=id,
                               post_delete_redirect='./%s'%ext_query_str)
    raise Http404