from urllib import urlencode

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.views.generic import list_detail,create_update
from django.template import RequestContext
from django.conf import settings
from django import forms
from django.contrib.auth.decorators import login_required,permission_required
from django.core.validators import URLValidator

from templatetags import title_field_html

from models import Category,Article

# TODO check repeated name when save record
class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
#        category = kwargs.get('instance',None)
#        if category:
#            print category.id
        self.base_fields['father'].queryset = Category.objects.filter(type__exact=10)
        super(CategoryForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Category
        widgets = {
            'description': forms.Textarea(attrs={'class':'xhe'}),
        }
    def clean_url(self):
        url = self.cleaned_data.get('url',None)
        type = self.cleaned_data.get('type',None)
        if type in (60,70,):
            URLValidator()(url)
            return url
        else:
            return None
#    def clean_tags(self):
#        tags = self.cleaned_data.get('tags',None)
#        if tags:
#            tags = tags.strip()
#            if tags:
#                if  not tags.endswith(','):
#                    tags = tags + ','
#                tags = tags.replace(',',', ').replace(',  ',', ')
#                return ' '+ tags

@login_required
@permission_required('cms.can_admin')
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

@login_required
@permission_required('cms.can_admin')
def category_index(request):
    if request.method == 'GET':
        pageSize = int(request.GET.get('pageSize',settings.DEFAUTL_PAGE_SIZE))
        page = int(request.GET.get('page',1))
        order_str = title_field_html.get_order_str(request)
        if not order_str:
            order_str = '-lastModified'
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

@login_required
@permission_required('cms.can_admin')
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

class NormalArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('url',)
        widgets = {
            'content': forms.Textarea(attrs={'class':'xhe'}),
        }
class PictureArticleForm(forms.ModelForm):
    pic = forms.ImageField(required=True,label=_('Picture'))
    class Meta:
        model = Article
        exclude = ('url',)
        widgets = {
            'content': forms.Textarea(attrs={'class':'xhe'}),
        }
class LinkArticleForm(forms.ModelForm):
    url=forms.URLField(required=True,label=_('URL'),min_length=4,max_length=255)
    class Meta:
        model = Article
        exclude = ('pic','content',)

@login_required
@permission_required('cms.can_admin')
def article_edit(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    if request.GET and request.GET.has_key('id'):
        id = request.GET['id']
        article = get_object_or_404(Article,pk=id)
        if category.type in (20,40):
            f = NormalArticleForm(instance=article)
        elif category.type == 30:
            f = PictureArticleForm(instance=article)
        elif category.type == 50:
            f = LinkArticleForm(instance=article)
        else:
            raise Http404
        return render_to_response('cms/article_form.html', {
                'form':           f,
                "submit_times":   -1,
                'display_cancel':'true',
                'ext_query_str': request.GET.get('ext_query_str',''),
                'id':             id,
                'category':     category,
                },context_instance=RequestContext(request))
    else:
        if category.type in (20,40):
            f = NormalArticleForm()
        elif category.type == 30:
            f = PictureArticleForm()
        elif category.type == 50:
            f = LinkArticleForm()
        else:
            raise Http404
        return render_to_response('cms/article_form.html', {
                'form':            f,
                "submit_times":   -1,
                'display_cancel':'true',
                'category':     category,
        },context_instance=RequestContext(request))

@login_required
@permission_required('cms.can_admin')
def article_index(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    if request.method == 'GET':
        return HttpResponseRedirect('../%s'%category_id)
    elif request.method == 'POST':
        if category.type in (20,40):
            f = NormalArticleForm(request.POST, request.FILES)
        elif category.type == 30:
            f = PictureArticleForm(request.POST, request.FILES)
        elif category.type == 50:
            f = LinkArticleForm(request.POST, request.FILES)
        else:
            raise Http404
        if f.is_valid():
            article = f.save(commit=False)
            article.category = category
            if category.type == 20:
                article.type = 10
            elif category.type == 30:
                article.type = 20
            elif category.type == 40:
                article.type = 10
            elif category.type == 50:
                article.type = 30
            article.save()
            return HttpResponseRedirect(article.id)
        else:
            return render_to_response('cms/article_form.html', {
                    'form':        f,
                    "submit_times":int(request.POST['submit_times']) - 1,
                    'display_cancel':request.POST.get('display_cancel','true'),
                    },context_instance=RequestContext(request))
    raise Http404

@login_required
@permission_required('cms.can_admin')
def article_detail(request,category_id,id):
    if request.method == 'GET':
        return list_detail.object_detail(request,
                                 queryset= Article.objects.filter(category=category_id),
                                 object_id=id)
    elif request.method == 'POST':
        method = request.POST.get(settings.EXTEND_HTTP_METHOD,None) 
        if method == 'PUT':
            category = get_object_or_404(Category,pk=category_id)
            article = get_object_or_404(Article,pk=id)
            if category.type in (20,40):
                f = NormalArticleForm(request.POST, request.FILES,instance=article)
            elif category.type == 30:
                f = PictureArticleForm(request.POST, request.FILES,instance=article)
            elif category.type == 50:
                f = LinkArticleForm(request.POST, request.FILES,instance=article)
            else:
                raise Http404
            if f.is_valid():
                article = f.save(commit=False)
                article.category = category
                if category.type == 20:
                    article.type = 10
                elif category.type == 30:
                    article.type = 20
                elif category.type == 40:
                    article.type = 10
                elif category.type == 50:
                    article.type = 30
                article.save()
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