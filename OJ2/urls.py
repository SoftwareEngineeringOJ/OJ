"""OJ2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^t/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': 'OJ2app' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'OJ2app.views.oj'),
    url(r'^oj/$', 'OJ2app.views.oj'),
    url(r'^login/$','OJ2app.views.login'),
    url(r'^regist/$', 'OJ2app.views.regist'),
    url(r'^problems/$', 'OJ2app.views.problemss'),
    url(r'^discuss/$', 'OJ2app.views.discuss'),
    url(r'^status/$', 'OJ2app.views.statuss'),
    url(r'^problemshow/$', 'OJ2app.views.problemshow'),
    url(r'^usershow/$', 'OJ2app.views.usershow'),
    url(r'^enter/$', 'OJ2app.views.enter'),
    url(r'^logout/$', 'OJ2app.views.logout'),
    url(r'^myoj/$', 'OJ2app.views.myoj'),
    url(r'^myproblems/$', 'OJ2app.views.myproblemss'),
    url(r'^mystatus/$', 'OJ2app.views.mystatuss'),
    url(r'^myproblemshow/$', 'OJ2app.views.myproblemshow'),
    url(r'^myusershow/$', 'OJ2app.views.myusershow'),
    url(r'^mycodeshow/$', 'OJ2app.views.mycodeshow'),
    url(r'^mysubmitcode/$', 'OJ2app.views.mysubmitcode'),
    url(r'^mydiscuss/$', 'OJ2app.views.mydiscuss'),
]
urlpatterns += staticfiles_urlpatterns()

