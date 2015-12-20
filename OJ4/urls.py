"""OJ4 URL Configuration

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
    url(r'^t/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': 'OJ4app' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'OJ4app.views.oj'),
    url(r'^oj/$', 'OJ4app.views.oj'),
    url(r'^login/$','OJ4app.views.login'),
    url(r'^regist/$', 'OJ4app.views.regist'),
    url(r'^problems/$', 'OJ4app.views.problemss'),
    url(r'^discuss/$', 'OJ4app.views.discuss'),
    url(r'^status/$', 'OJ4app.views.statuss'),
    url(r'^problemshow/$', 'OJ4app.views.problemshow'),
    url(r'^usershow/$', 'OJ4app.views.usershow'),
    url(r'^enter/$', 'OJ4app.views.enter'),
    url(r'^logout/$', 'OJ4app.views.logout'),
    url(r'^myoj/$', 'OJ4app.views.myoj'),
    url(r'^myproblems/$', 'OJ4app.views.myproblemss'),
    url(r'^mystatus/$', 'OJ4app.views.mystatuss'),
    url(r'^myproblemshow/$', 'OJ4app.views.myproblemshow'),
    url(r'^myusershow/$', 'OJ4app.views.myusershow'),
    url(r'^mycodeshow/$', 'OJ4app.views.mycodeshow'),
    url(r'^mysubmitcode/$', 'OJ4app.views.mysubmitcode'),
    url(r'^mydiscuss/$', 'OJ4app.views.mydiscuss'),
]
urlpatterns += staticfiles_urlpatterns()
