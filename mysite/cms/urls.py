from django.conf.urls.defaults import patterns

import views

urlpatterns = patterns('',
   (r'^(?P<id>\d+)/?$',views.category_view),
   (r'^(?P<category_id>\d+)/(?P<id>\d+)$',views.article_view),
   (r'^(?P<category_id>\d+)/feed_entry$',views.feed_entry_view),
)