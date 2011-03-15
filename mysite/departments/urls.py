from django.conf.urls.defaults import patterns

import views

urlpatterns = patterns('',
   (r'^departments/$',views.department_list),
)