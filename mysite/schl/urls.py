from django.conf.urls.defaults import patterns

import views

urlpatterns = patterns('',
   (r'^$',views.schl_list),
   (r'^(?P<id>\d*)/$',views.schl_detail),
   )