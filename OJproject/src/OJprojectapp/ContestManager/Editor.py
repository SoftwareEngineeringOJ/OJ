#coding=utf-8
'''
Created on 2015年12月23日

@author: Rhapsody
'''

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime, timedelta
#from django import forms
from OJprojectapp.UserManager import UserInit
from OJprojectapp.models import *
from OJprojectapp.DataManager import DataManager
from TempStore import *
from OJprojectapp.ContestManager import TempStore
#from django.templatetags.i18n import language

def TimeSet(req, Data):
    show = False
    warning = ""
    beginTime = Data.begintime.strftime('%Y-%m-%d')
    hour = Data.begintime.hour
    minute = Data.begintime.minute
    if req.method == 'POST':
        pages = req.POST
        if 'beginTime' in pages:
            beginTime = pages['beginTime']
        if 'hour' in pages:
            hour = pages['hour']
        if 'minute' in pages:
            minute = pages['minute']
    try:
        Data.begintime = datetime.strptime(beginTime,'%Y-%m-%d')
        Data.begintime = Data.begintime.replace(hour = int(hour))
        Data.begintime = Data.begintime.replace(minute = int(minute))
        Data.save()
    except:
        show = True
        warning = "Time's fomat is wrong "
    return {'warning' : warning, 
            'show' : show, 
            'data' : Data, 
            'beginTime' : beginTime, 
            'hour' : hour, 
            'minute' : minute, }

def LenSet(req, Data):
    warning = ""
    show = False
    d_day = 0
    d_hour = 5
    d_minute = 0
    if req.method == 'POST':
        pages = req.POST
        if 'd_day' in pages:
            d_day = pages['d_day']
        if 'd_hour' in pages:
            d_hour = pages['d_hour']
        if 'd_minute' in pages:
            d_minute = pages['d_minute']
    try:
        Data.endtime = Data.begintime + timedelta(days = int(d_day), hours = int(d_hour), minutes = int(d_minute))
        Data.save()
    except:
        show = True
        warning = "Time's fomat is wrong "
    return {'warning' : warning, 
            'show' : show, 
            'd_day' : d_day, 
            'd_hour' : d_hour, 
            'd_minute' : d_minute, }

def InfoSet(req, Data):
    warning = ""
    show = False #提示信息
    if req.method == 'POST':
        pages = req.POST
        if 'title' in pages:
            Data.title = pages['title']
        if 'description' in pages:
            Data.description = pages['description']
        if 'announcement' in pages:
            Data.announcement = pages['announcement']
        if 'password' in pages:
            Data.password = pages['password']
        Data.save()
    return {'warning' : warning, 
            'show' : show, }

def ProblemsSet(req, Data):
    show = False
    warning = ""
    if req.method == 'POST' and 'add' in req.POST:
        pages = req.POST
        sid = pages['sid']
        title = pages['problemtitle']
        oj = pages['oj']
        T = ProblemForm(titles = title, 
                        pids = sid, 
                        sojs = oj)
        if len(Data.list.all()) >= 26:
            warning = 'Too many problems'
            show = True
        elif find(Data.list.all(), T):
            warning = 'Problems existed !'
            show = True
        elif check(T):
            warning = 'Input Error'
            show = True
        else:
            if title == "" or title is None:
                title = problemslist.objects.get(OJ = oj, SID = sid).title
                T = ProblemForm(titles = title, 
                                pids = sid, 
                                sojs = oj)
            new = contest_problem(titles = T.titles, 
                                  pids = T.pids, 
                                  sojs = T.sojs, )
            new.save()
            Data.list.add(new)
            Data.save()
    return {'show' : show, 
            'warning' : warning, }
