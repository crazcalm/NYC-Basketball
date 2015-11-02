from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from courts import views

urlpatterns = [
    url(r'^courts/$', views.CourtList.as_view()),
    url(r'^courts/(?P<id>[0-9]+)/$', views.CourtDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
