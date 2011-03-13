from django.conf.urls.defaults import patterns

import views

urlpatterns = patterns('',
   (r'^$',views.feedback),
   (r'^result$', views.feedback_result),
   (r'^feature-suggestions/$', views.feature_suggestions),
   (r'^feature-suggestions/result$', views.feature_suggestions_result),
)