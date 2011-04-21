from django.conf.urls.defaults import patterns

import views

urlpatterns = patterns('',
    (r'^(?P<id>\d*)/$',views.bmap),
    (r'^$',views.bmap_default),
    )