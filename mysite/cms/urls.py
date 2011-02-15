from django.conf.urls.defaults import patterns

import views

urlpatterns = patterns('',
   (r'^(?P<id>\d+)/?$',views.category_view),
   (r'^(?P<category_id>\d+)/(?P<id>\d+)$',views.article_view),
   (r'^(?P<category_id>\d+)/(?P<url_hash>[0-9a-f]{56})$',views.feed_entry_view),
)