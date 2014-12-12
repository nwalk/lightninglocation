from django.conf.urls import patterns, include, url
from apps.spatial import json_views

urlpatterns = patterns('',
    url('^sensors$', json_views.SensorsCollection.as_view(), name='sensors'),
    )