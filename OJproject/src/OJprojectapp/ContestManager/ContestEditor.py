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
from OJprojectapp.ContestManager import TempStore
#from django.templatetags.i18n import language

def get_contest_list(req):
    '''
    username = req.COOKIES.get('username','')
    Flag = True
    if username is "" or username is None:
        Flag = False
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    global problem_pagenumber
    print problemslist.objects.all().count()
    if req.POST:
        if cmp(req.POST["oj"],"all") == 0:
            problems_list=problemslist.objects.all().order_by('SID')
        else:
            problems_list=problemslist.objects.filter(OJ=req.POST["oj"]).order_by('SID')
        find=oj_show.index(req.POST["oj"])
        first=oj_show[0]
        oj_show[0]=req.POST["oj"]
        oj_show[find]=first
        if cmp(req.POST["sid"],"") != 0:
            problems_list=problems_list.filter(SID=req.POST["sid"]).order_by('SID')
        sid_show=req.POST["sid"]
        if cmp(req.POST["title"],"") != 0:
            problems_list=problems_list.filter(title=req.POST["title"]).order_by('SID')
        title_show=req.POST["title"]
        if cmp(req.POST["source"],"") != 0:
            problems_list=problems_list.filter(source=req.POST["source"]).order_by('SID')
        source_show=req.POST["source"]
        if req.POST.has_key("1"):
            problems_list=problems_list[problem_pagenumber+20:problem_pagenumber+40]
        if req.POST.has_key("2"):
            problems_list=problems_list[problem_pagenumber+40:problem_pagenumber+60]
        if req.POST.has_key("3"):
            problems_list=problems_list[problem_pagenumber+60:problem_pagenumber+80]
        if req.POST.has_key("4"):
            problems_list=problems_list[problem_pagenumber+80:problem_pagenumber+100]
        if req.POST.has_key("5"):
            problems_list=problems_list[problem_pagenumber+100:problem_pagenumber+120]
        if req.POST.has_key("nextpage"):
            problems_list=problems_list[problem_pagenumber+120:problem_pagenumber+140]
            problem_pagenumber+=100
        if req.POST.has_key("previouspage"):
            if(problem_pagenumber>=100):
               problem_pagenumber-=100
               problems_list=problems_list[problem_pagenumber:problem_pagenumber+20]
        if req.POST.has_key("filter"):
            problems_list=problems_list[0:20]
            problem_pagenumber=0
        value1=str(problem_pagenumber+1020)
        value2=str(problem_pagenumber+1040)
        value3=str(problem_pagenumber+1060)
        value4=str(problem_pagenumber+1080)
        value5=str(problem_pagenumber+1100)
    else:
        problems_list=problemslist.objects.all().order_by('SID')[0:20]
        sid_show=""
        title_show=""
        source_show=""
        value1="1020"
        value2="1040"
        value3="1060"
        value4="1080"
        value5="1100"
        problem_pagenumber=0
    return render_to_response('problems.html', {'problems_list' : problems_list, 
                                                'oj_show' : oj_show, 
                                                'sid_show' : sid_show, 
                                                'title_show' : title_show, 
                                                'source_show' : source_show, 
                                                'value1' : value1,
                                                'value2' : value2,
                                                'value3' : value3, 
                                                'value4' : value4, 
                                                'value5' : value5, 
                                                'Flag' : Flag, 
                                                'username' : username}, 
                              context_instance=RequestContext(req))
    '''
    username = req.COOKIES.get('username','')
    contest_list = contest.objects.all()
    return render_to_response("mycontest.html", {'username':username, 'contest_list':contest_list},context_instance=RequestContext(req))

def delete_contest_problems(req):
    if req.method == 'GET':
        id = req.GET['id']
        contest_problem.objects.get(id = id).delete()
    return HttpResponseRedirect('/addcontest')

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
    beginTime = Data.begintime.strftime('%Y-%m-%d')
    hour = Data.begintime.hour
    minute = Data.begintime.minute
    d_day = 0
    d_hour = 5
    d_minute = 0
    # 可能需要修改，时间的初始化
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
            print oj, sid, title
            if title == "" or title is None:
                #print 'Try find'
                title = problemslist.objects.get(OJ = oj, SID = sid).title
                T = ProblemForm(titles = title, 
                                pids = sid, 
                                sojs = oj)
            new = contest_problem(titles = T.titles, 
                                  pids = T.pids, 
                                  sojs = T.sojs, )
            new.save()
            Data.list.add(new)
    #return render_to_response('addcontest.html')
    if not show:
        Data.save()
    #print type(beginTime)
    try:
        Data.begintime = datetime.strptime(beginTime,'%Y-%m-%d')
        Data.begintime = Data.begintime.replace(hour = int(hour))
        Data.begintime = Data.begintime.replace(minute = int(minute))
        Data.endtime = Data.begintime + timedelta(days = int(d_day), hours = int(d_hour), minutes = int(d_minute))
        print 'ReadDy =', Data.title
        Data.save()
    except:
        show = True
        warning = "Time's fomat is wrong "
    #print 'Begin : ', Data.begintime
    #print 'long =', long
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
