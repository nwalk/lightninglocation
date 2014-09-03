from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.locator.views import MainView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lightninglocation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main', MainView.as_view(), name='main'),
    ##url(r'^main/', include('apps.locator.urls', namespace='locator')),
)
