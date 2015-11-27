"""OJproject URL Configuration

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
    url(r'^t/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': 'OJprojectapp' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'OJprojectapp.views.oj'),
    url(r'^oj/$', 'OJprojectapp.views.oj'),
    url(r'^login/$','OJprojectapp.views.login'),
    url(r'^regist/$', 'OJprojectapp.views.regist'),
    url(r'^problems/$', 'OJprojectapp.views.problemss'),
    url(r'^status/$', 'OJprojectapp.views.statuss'),
    url(r'^problemshow/$', 'OJprojectapp.views.problemshow'),
    url(r'^usershow/$', 'OJprojectapp.views.usershow'),
    url(r'^enter/$', 'OJprojectapp.views.enter'),
    url(r'^logout/$', 'OJprojectapp.views.logout'),
    url(r'^myoj/$', 'OJprojectapp.views.myoj'),
    url(r'^myproblems/$', 'OJprojectapp.views.myproblemss'),
    url(r'^mystatus/$', 'OJprojectapp.views.mystatuss'),
    url(r'^myproblemshow/$', 'OJprojectapp.views.myproblemshow'),
    url(r'^myusershow/$', 'OJprojectapp.views.myusershow'),
    url(r'^mysubmitcode/$', 'OJprojectapp.views.mysubmitcode'),
    url(r'^codeshow/$','OJprojectapp.views.codeshow')
]
urlpatterns += staticfiles_urlpatterns()
