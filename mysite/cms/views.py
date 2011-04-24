import hashlib

from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext

import feedparser

from models import Category,Article,get_category_single_article

def category_view(request,id=None):
    category = get_object_or_404(Category,pk=id)
    c = category
    father_stack = []
    while c.father:
        c = c.father
        father_stack.insert(0, c)
    if category.type == 10:
        categories = Category.objects.filter(father=category.id).order_by('-lastModified')
        return render_to_response('content/category.html', {
                'category':category,
                'father_stack':father_stack,
                'categories':categories,
    },context_instance=RequestContext(request))
    elif category.type == 40:
        article = get_category_single_article(category.id)
        if not article:
            raise Http404
        return render_to_response('content/article.html',{
                'article':article,
                'father_stack':father_stack,
                'category':category,
    },context_instance=RequestContext(request))
    elif category.type == 60:
        return HttpResponseRedirect(category.url)
    elif category.type == 70:
        feed = feedparser.parse(category.url)
        for entry in feed.entries:
            entry.url_hash = hashlib.sha224(entry.link).hexdigest()
        return render_to_response('content/rss.html', {
                'category':category,
                'feed':feed,
                'father_stack':father_stack,
                'entries':feed.entries,
    },context_instance=RequestContext(request))
    articles = Article.objects.filter(category=category.id).order_by('-setTop','-lastModified')
    return render_to_response('content/category.html', {
                'category':category,
                'articles':articles,
                'father_stack':father_stack,
    },context_instance=RequestContext(request))
    
def article_view(request,id=None,category_id=None):
    article = get_object_or_404(Article,pk=id)
    c = article.category
    father_stack = [c,]
    while c.father:
        c = c.father
        father_stack.insert(0, c)
    if article.type == 30:
        return HttpResponseRedirect(article.url);
    return render_to_response('content/article.html',{
                'article':article,
                'category':article.category,
                'father_stack':father_stack,
    },context_instance=RequestContext(request))


def feed_entry_view(request,category_id=None,url_hash=None):
    category = get_object_or_404(Category,pk=category_id)
    feed = feedparser.parse(category.url)
    c = category
    father_stack = [c,]
    while c.father:
        c = c.father
        father_stack.insert(0, c)
    for entry in feed.entries:
        if hashlib.sha224(entry.link).hexdigest() == url_hash:
            return render_to_response('content/feed_entry.html',{
                'entry':entry,
                'category':category,
                'feed':feed,
                'father_stack':father_stack,
                },context_instance=RequestContext(request))
    raise Http404
    