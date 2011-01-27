from django.conf.urls.defaults import patterns

import views_adm

urlpatterns = patterns('',
   (r'^$',views_adm.category_index),
   (r'^!edit$',views_adm.category_edit),
   (r'^(?P<id>\d+)$', views_adm.category_detail),
   (r'^(?P<category_id>\d+)/$',views_adm.article_index),
   (r'^(?P<category_id>\d+)/!edit$',views_adm.article_edit),
   (r'^(?P<category_id>\d+)/(?P<id>\d+)$', views_adm.article_detail),
)