from django.conf.urls.defaults import patterns

import views

urlpatterns = patterns('',
   (r'^$',views.department_list),
   (r'^(?P<id>\d*)/$',views.department_detail),
   )