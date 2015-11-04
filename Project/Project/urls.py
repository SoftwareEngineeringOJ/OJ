"""Project URL Configuration

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
    url(r'^t/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': 'Projectapp' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Projectapp.views.oj'),
    url(r'^oj/$', 'Projectapp.views.oj'),
    url(r'^login/$','Projectapp.views.login'),
    url(r'^regist/$', 'Projectapp.views.regist'),
    url(r'^logout/$', 'Projectapp.views.logout'),
    url(r'^enter/$', 'Projectapp.views.enter'),
    url(r'^cut/$', 'Projectapp.views.cut'),

]
urlpatterns += staticfiles_urlpatterns()