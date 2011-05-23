from django.conf.urls.defaults import patterns

from django.views.generic import date_based
from models import Event
import views

event_info_dict = {'month_format':'%m','allow_future':True,'template_name':'event/list_event_by_day.html','queryset':Event.objects.all(),'date_field':'date'}

urlpatterns = patterns('',
   (r'^$',views.index),
   (r'^(?P<id>\d+)$',views.view),              
   (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',date_based.archive_day,event_info_dict),
   )
