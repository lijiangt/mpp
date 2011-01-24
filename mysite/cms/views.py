from django.shortcuts import HttpResponseRedirect,Http404,render_to_response,get_object_or_404
from django.template import RequestContext

import feedparser

from models import Category,Article

def category_view(request,id=None):
    category = get_object_or_404(Category,pk=id)
    if category.type == 40:
        pass;
    elif category.type == 60:
        return HttpResponseRedirect(category.url)
    elif category.type == 70:
        feed = feedparser.parse(category.url)
        return render_to_response('content/rss.html', {
                'category':category,
                'feed':feed,
                'entries':feed.entries,
    },context_instance=RequestContext(request))
    articles = Article.objects.filter(category=category.id)
    return render_to_response('content/category.html', {
                'category':category,
                'articles':articles,
    },context_instance=RequestContext(request))
    
def article_view(request,id=None,category_id=None):
    article = get_object_or_404(Article,pk=id)
    if article.type == 30:
        return HttpResponseRedirect(article.url);
    return render_to_response('content/article.html',{
                'article':article,
    },context_instance=RequestContext(request))


def feed_entry_view(request,category_id=None):
    category = get_object_or_404(Category,pk=category_id)
    feed = feedparser.parse(category.url)
    link = request.GET['link']
    for entry in feed.entries:
        if entry.link == link:
            return render_to_response('content/feed_entry.html',{
                'entry':entry,
                },context_instance=RequestContext(request))
    raise Http404
    