from django.conf.urls.defaults import patterns

from models import Event
import views

event_info_dict = {'month_format':'%m','allow_future':True,'template_name':'event/list_event_by_day.html','queryset':Event.objects.all(),'date_field':'date'}

urlpatterns = patterns('',
   (r'^$',views.index),
   (r'^date/0/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',views.by_day), 
   (r'^date/0/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)$',views.view),
   (r'^type/$',views.list_type),
   (r'^type/(?P<type>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',views.by_type), 
   (r'^type/(?P<type>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)$',views.view_by_type),
   (r'^dep/$',views.list_dep),
   (r'^dep/(?P<dep_id>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',views.by_dep), 
   (r'^dep/(?P<dep_id>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)$',views.view_by_dep),
   )
