#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime, timedelta
from django.utils import timezone
#from django import forms
from OJprojectapp.UserManager import UserInit
from OJprojectapp.models import *
from OJprojectapp.DataManager import DataManager
from TempStore import *
from django.db.models.lookups import Year
from matplotlib.dates import minutes
from OJprojectapp.ContestManager import TempStore
#from django.templatetags.i18n import language

def addcontest(req):
    username, Flag = UserInit.init(req)
    Data = loaddata(username)
    problems_list = Data.list[ : ]
    print 'Length =', len(Data.list)
    warning = ""
    show = False
    OJList = DataManager.SuportOJList()
    beginTime = timezone.now().strftime('%Y-%m-%d')
    print beginTime
    hour = 0
    minute = 0
    d_day = 0
    d_hour = 5
    d_minute = 0
    if req.method == 'POST':
        pages = req.POST
        if 'title' in pages:
            Data.title = pages['title']
        print 'Title =(', Data.title, ')'
        if 'beginTime' in pages:
            beginTime = pages['beginTime']
        if 'hour' in pages:
            hour = pages['hour']
        if 'minute' in pages:
            minute = pages['minute']
        if 'd_day' in pages:
            d_day = pages['d_day']
        if 'd_hour' in pages:
            d_hour = pages['d_hour']
        if 'd_minute' in pages:
            d_minute = pages['d_minute']
        if 'description' in pages:
            Data.description = pages['description']
        if 'announcement' in pages:
            Data.announcement = pages['announcement']
        if 'password' in pages:
            Data.password = pages['password']
        print 'Update'
    if req.method == 'POST' and 'add' in req.POST:
        pages = req.POST
        sid = pages['sid']
        title = pages['problemtitle']
        oj = pages['oj']
        T = ProblemForm(titles = title, 
                        pids = sid, 
                        sojs = oj)
        if len(problems_list) >= 26:
            warning = 'Too many problems'
            show = True
        elif find(problems_list, T):
            warning = 'Problems existed !'
            show = True
        elif check(T):
            warning = 'Input Error'
            show = True
        else:
            print oj, sid, title
            if title == "" or title is None:
                #print 'Try find'
                title = problemslist.objects.get(OJ = oj, SID = sid).title
                T = ProblemForm(titles = title, 
                                pids = sid, 
                                sojs = oj)
            problems_list.append(T)
    #return render_to_response('addcontest.html')
    if not show:
        Data.list = problems_list[ : ]
        savedata(username, Data)
    show_list = []
    for ele in problems_list:
        show_list.append(ProblemShow(titles = ele.titles, 
                                     pids = ele.pids, 
                                     sojs = ele.sojs, ))
    #print type(beginTime)
    try:
        Data.begintime = datetime.strptime(beginTime,'%Y-%m-%d')
        Data.begintime = Data.begintime.replace(hour = int(hour))
        Data.begintime = Data.begintime.replace(minute = int(minute))
        Data.endtime = Data.begintime + timedelta(days = int(d_day), hours = int(d_hour), minutes = int(d_minute))
        print 'ReadDy =', Data.title
        savedata(username, Data)
    except:
        show = True
        warning = "Time's fomat is wrong "
    #print 'Begin : ', Data.begintime
    #print 'long =', long
    if req.method == 'POST':
        if 'submit' in req.POST:
            TempStore.createcontest(username)
    return render_to_response('addcontest.html', 
                              {'username' : username, 
                               'Flag' : Flag, 
                               'OJList' : OJList, 
                               'warning' : warning, 
                               'show' : show, 
                               'problems_list' : show_list, 
                               'data' : Data, 
                               'beginTime' : beginTime, 
                               'hour' : hour, 
                               'minute' : minute, 
                               'd_day' : d_day, 
                               'd_hour' : d_hour, 
                               'd_minute' : d_minute, 
                               }, 
                              context_instance = RequestContext(req))
