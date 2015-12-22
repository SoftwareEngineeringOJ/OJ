#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
#from django import forms
from OJprojectapp.UserManager import UserInit
from OJprojectapp.models import *
from OJprojectapp.DataManager import DataManager
#from django.templatetags.i18n import language

def contestlist(req):
    return render_to_response('contestlist.html')

class Problem():
    def __init__(self, OJ, SID, title):
        self.OJ = OJ
        self.SID = SID
        self.title = title

class LoadForm():
    def __init__(self):
        self.title = ""
        self.description = ""
        self.announcement = ""
        self.password = ""
        self.owner = ""
        self.count = ""
        self.ptitles = []
        self.pids = []
        self.sojs = []
        self.begintime = ""
        self.endtime = ""

def loaddata(username):
    tmp = contest_tmp.objects.filter(owner = username)
    if len(tmp) == 0:
        tmp = contest_tmp(owner = username, 
                          count = 0, 
                          begintime = datetime.now(), 
                          endtime = datetime.now(),
                          )
        tmp.save()
    tmp = contest_tmp.objects.get(owner = username)
    #print tmp.owner
    Ans = LoadForm()
    print 'title', type(tmp.sojs)
    Ans.title = tmp.title
    Ans.description = tmp.description
    Ans.announcement = tmp.announcement
    Ans.password = tmp.password
    Ans.owner = tmp.owner
    Ans.count = tmp.count
    Ans.ptitles = tmp.ptitles[ : ]
    Ans.pids = tmp.pids[ : ]
    #Ans.sojs = tmp.sojs[ : ]
    Ans.sojs = []
    for i in range(26):
        x = tmp.sojs[i]
        Ans.sojs.append(x)
    Ans.begintime = tmp.begintime
    Ans.endtime = tmp.endtime
    return Ans
    
def savedata(username, Data):
    tmp = contest_tmp.objects.filter(owner = username)
    if len(tmp) == 0:
        tmp = contest_tmp(owner = username, 
                          count = 0, 
                          begintime = datetime.now(), 
                          endtime = datetime.now(),
                          )
        tmp.save()
    tmp = contest_tmp.objects.get(owner = username)
    tmp.title = Data.title
    tmp.description = Data.description
    tmp.announcement = Data.announcement
    tmp.password = Data.password
    tmp.owner = Data.owner
    tmp.count = Data.count
    tmp.ptitles = Data.ptitles[ : ]
    tmp.pids = Data.pids[ : ]
    #tmp.sojs = Data.sojs[ : ]
    #Ans.sojs = []
    for i in range(26):
        tmp.sojs[i] = tmp.sojs[i]
    tmp.begintime = Data.begintime
    tmp.endtime = Data.endtime
    tmp.save()

def check(add):
    tmp = problemslist.objects.filter(OJ = add.OJ, SID = add.SID)
    return len(tmp) > 0

def addcontest(req):
    username, Flag = UserInit.init(req)
    Data = loaddata(username)
    problems_list = []
    warning = ""
    show = False
    print 'Count :', Data.count
    print type(Data.count)
    for i in range(Data.count):
        print type(Data.sojs[0] + '')
        print 'Source :', Data.sojs[0]
        problems_list.append(Problem(Data.sojs[i], Data.pids[i], Data.title[i]))
    OJList = DataManager.SuportOJList()
    if req.method == 'POST' and 'add' in req.POST:
        pages = req.POST
        sid = pages['sid']
        title = pages['problemtitle']
        oj = pages['oj']
        if Problem(oj, sid, title) in problems_list:
            warning = 'Problems existed !'
            show = True
        elif check(Problem(oj, sid, title)):
            warning = 'Input Error'
            show = True
        else:
            print oj, sid, title
            Data.count += 1
            problems_list.append(Problem(oj, sid, title))
    #return render_to_response('addcontest.html')
    savedata(username, Data)
    return render_to_response('addcontest.html', 
                              {'username' : username, 
                               'Flag' : Flag, 
                               'OJList' : OJList, 
                               'warning' : warning, 
                               'show' : show, 
                               }, 
                              context_instance = RequestContext(req))