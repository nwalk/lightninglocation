from django.conf.urls import patterns, include, url
from apps.locator import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.MainView.as_view()),
    url(r'^map$', views.MapView.as_view()),
)