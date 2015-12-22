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

class LoadForm():
    def __init__(self):
        self.title = ""
        self.description = ""
        self.announcement = ""
        self.password = ""
        self.owner = ""
        self.list = []
        self.begintime = ""
        self.endtime = ""

class ProblemForm():
    def __init__(self, titles, pids, sojs):
        self.titles = titles
        self.pids = pids
        self.sojs = sojs

def loaddata(username):
    tmp = contest_tmp.objects.filter(owner = username)
    if len(tmp) == 0:
        tmp = contest_tmp(owner = username, 
                          begintime = datetime.now(), 
                          endtime = datetime.now(), 
                          )
        tmp.save()
    tmp = contest_tmp.objects.get(owner = username)
    #print tmp.owner
    Ans = LoadForm()
    Ans.title = tmp.title
    Ans.description = tmp.description
    Ans.announcement = tmp.announcement
    Ans.password = tmp.password
    Ans.owner = tmp.owner
    for problem in tmp.list.all():
        Ans.list.append(ProblemForm(problem.titles, problem.pids, problem.sojs))
    Ans.begintime = tmp.begintime
    Ans.endtime = tmp.endtime
    return Ans
    
def savedata(username, Data):
    pass

def check(add):
    tmp = problemslist.objects.filter(OJ = add.OJ, SID = add.SID)
    return len(tmp) > 0

def addcontest(req):
    username, Flag = UserInit.init(req)
    Data = loaddata(username)
    problems_list = []
    warning = ""
    show = False
    OJList = DataManager.SuportOJList()
    if req.method == 'POST' and 'add' in req.POST:
        pages = req.POST
        sid = pages['sid']
        title = pages['problemtitle']
        oj = pages['oj']
        if ProblemForm(oj, sid, title) in problems_list:
            warning = 'Problems existed !'
            show = True
        elif check(ProblemForm(oj, sid, title)):
            warning = 'Input Error'
            show = True
        else:
            print oj, sid, title
            problems_list.append(ProblemForm(oj, sid, title))
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
