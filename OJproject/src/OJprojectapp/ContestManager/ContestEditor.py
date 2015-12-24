#coding=utf-8
'''
Created on 2015年12月22日

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
from OJprojectapp.ContestManager import TempStore, Editor
#from django.templatetags.i18n import language

def get_contest_list(req):
    username, Flag = UserInit.init(req)
    settershow = ""
    if req.method == 'POST':
        setter = req.POST['setter']
        settershow = setter
        print 'Find', settershow
    contest_list = contest.objects.filter(IsReady = True)
    return render_to_response("contestlist.html", {'username' : username, 
                                                   'Flag' : Flag, 
                                                   'settershow' : settershow, 
                                                   'contest_list' : contest_list, }, 
                              context_instance = RequestContext(req))

def delete_contest_problems(req):
    if req.method == 'GET':
        id = req.GET['id']
        contest_problem.objects.get(id = id).delete()
    if 'contest_id' in req.GET:
        return HttpResponseRedirect('/editcontest/?id=%s' %req.GET['contest_id'])
    return HttpResponseRedirect('/addcontest')

def editcontest(req):
    username, Flag = UserInit.init(req)
    if username ==  None or username =="":
        return HttpResponseRedirect('/login')
    #处理没有登录
    if 'id' in req.GET:
        contest_id = req.GET['id']
        Data, find = loadcontest(username, contest_id)
        if not find:
            return HttpResponseRedirect('/contestlist')
    else:
        return HttpResponseRedirect('/contestlist')
    #装载信息
    warning = ""
    show = False #提示信息
    OJList = DataManager.SuportOJList() #OJ列表
    
    start = Data.begintime.strftime('%Y-%m-%d %H:%M:%S %f') <= datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
    
    if not start:
        tmp = Editor.TimeSet(req, Data)
        beginTime = tmp['beginTime']
        hour = tmp['hour']
        minute = tmp['minute']
        if tmp['show']:
            show = True
            warning = tmp['warning']
        #需要选择是否能够修改开始 
    #开始时间设置

    tmp = Editor.LenSet(req, Data)
    d_day = tmp['d_day']
    d_hour = tmp['d_hour']
    d_minute = tmp['d_minute']
    if tmp['show']:
        show = True
        warning = tmp['warning']
    #比赛持续时间
    
    tmp = Editor.InfoSet(req, Data)
    if tmp['show']:
        show = True
        warning = tmp['warning']
    #信息维护
    
    if not start:
        tmp = Editor.ProblemsSet(req, Data)
        if tmp['show']:
            show = True
            warning = tmp['warning']
    #添加题目
    
    if req.method == 'POST':
        if 'submit' in req.POST and not show:
            if Data.title is None or Data.title == "":
                show = True
                warning = "Please input the contest' title !"
            elif (not start) and len(Data.list.all()) == 0:
                show = True
                warning = "Please add the problems !"
            elif (not start) and Data.begintime.strftime('%Y-%m-%d %H:%M:%S %f') < datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'):
                #print 'Set', Data.begintime.strftime('%Y-%m-%d %H:%M:%S %f')
                #print 'Now', datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
                show = True
                warning = "The begin time must be later than now !"
            else:
                Data.save()
                TempStore.edit_contest(contest_id)
    start = not start
    print 'start =', start
    if start:
        return render_to_response('editcontest.html', 
                                  {'username' : username, 
                                   'Flag' : Flag, 
                                   'OJList' : OJList, 
                                   'warning' : warning, 
                                   'show' : show, 
                                   'problems_list' : Data.list.all(), 
                                   'data' : Data, 
                                   'beginTime' : beginTime, 
                                   'hour' : hour, 
                                   'minute' : minute, 
                                   'd_day' : d_day, 
                                   'd_hour' : d_hour, 
                                   'd_minute' : d_minute, 
                                   'start' : start, 
                                   'contestid' : contest_id, 
                                   }, 
                                  context_instance = RequestContext(req))
    print 'start =', start
    return render_to_response('editcontest.html', 
                              {'username' : username, 
                               'Flag' : Flag, 
                               'OJList' : OJList, 
                               'warning' : warning, 
                               'show' : show, 
                               'data' : Data, 
                               'd_day' : d_day, 
                               'd_hour' : d_hour, 
                               'd_minute' : d_minute, 
                               'start' : start, 
                               'contestid' : contest_id, 
                               }, 
                              context_instance = RequestContext(req))


def addcontest(req):
    username, Flag = UserInit.init(req)
    if username ==  None or username =="":
        return HttpResponseRedirect('/login')
    #处理没有登录
    Data = loaddata(username)
    #装载信息
    warning = ""
    show = False #提示信息
    OJList = DataManager.SuportOJList() #OJ列表
    
    tmp = Editor.TimeSet(req, Data)
    beginTime = tmp['beginTime']
    hour = tmp['hour']
    minute = tmp['minute']
    if tmp['show']:
        show = True
        warning = tmp['warning']
    #开始时间设置

    tmp = Editor.LenSet(req, Data)
    d_day = tmp['d_day']
    d_hour = tmp['d_hour']
    d_minute = tmp['d_minute']
    if tmp['show']:
        show = True
        warning = tmp['warning']
    #比赛持续时间
    
    tmp = Editor.InfoSet(req, Data)
    if tmp['show']:
        show = True
        warning = tmp['warning']
    #信息维护
    
    tmp = Editor.ProblemsSet(req, Data)
    if tmp['show']:
        show = True
        warning = tmp['warning']
    #添加题目
    
    if req.method == 'POST':
        if 'submit' in req.POST and not show:
            if Data.title is None or Data.title == "":
                show = True
                warning = "Please input the contest' title !"
            elif len(Data.list.all()) == 0:
                show = True
                warning = "Please add the problems !"
            elif Data.begintime.strftime('%Y-%m-%d %H:%M:%S %f') < datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'):
                #print 'Set', Data.begintime.strftime('%Y-%m-%d %H:%M:%S %f')
                #print 'Now', datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
                show = True
                warning = "The begin time must be later than now !"
            else:
                Data.save()
                TempStore.createcontest(username)
    return render_to_response('addcontest.html', 
                              {'username' : username, 
                               'Flag' : Flag, 
                               'OJList' : OJList, 
                               'warning' : warning, 
                               'show' : show, 
                               'problems_list' : Data.list.all(), 
                               'data' : Data, 
                               'beginTime' : beginTime, 
                               'hour' : hour, 
                               'minute' : minute, 
                               'd_day' : d_day, 
                               'd_hour' : d_hour, 
                               'd_minute' : d_minute, 
                               }, 
                              context_instance = RequestContext(req))
