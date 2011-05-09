from django.conf.urls.defaults import patterns
import views

urlpatterns = patterns('',
    (r'^g/$',views.gmap),
    (r'^c/$',views.cmap),
    (r'^b/$',views.buildinglist),
    (r'^b/(?P<id>\d*)$',views.bmap),
    (r'^d/$',views.department_list),
    (r'^d/(?P<id>\d*)$',views.dmap),
    (r'^s/$',views.schl_list),
    (r'^s/(?P<id>\d*)$',views.smap),
    (r'^search$',views.search),
    (r'^$',views.map),
    )