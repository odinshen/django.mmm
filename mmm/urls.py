from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import trip_home, trip_detail
from tables.views import table_home, table_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mmm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^table/(?P<id>\d+)/$', table_detail, name='table_detail'),
    url(r'^table/', table_home),
    url(r'^trip/(?P<id>\d+)/$', trip_detail, name='trip_detail'),
    url(r'^trip/', trip_home),
    url(r'^$', trip_home),
)
