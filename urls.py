from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       (r'^', include('home.urls')),
)