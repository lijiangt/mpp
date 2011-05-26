from django.conf.urls.defaults import patterns

from models import Event
import views

event_info_dict = {'month_format':'%m','allow_future':True,'template_name':'event/list_event_by_day.html','queryset':Event.objects.all(),'date_field':'date'}

urlpatterns = patterns('',
   (r'^$',views.index),
   (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',views.by_day), 
   (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)$',views.view),
   )
