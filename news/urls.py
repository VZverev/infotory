from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'news.views.index', name='news'),
    url(r'(?P<id>\d+)/$', 'news.views.details'),
)
