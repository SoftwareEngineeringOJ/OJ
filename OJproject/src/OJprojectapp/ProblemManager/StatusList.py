#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from OJprojectapp.UserManager import UserManager
from django import forms
from OJprojectapp.models import *
from OJprojectapp.DataManager import DataManager
from OJprojectapp.PagesManager import PagesManager

def statuss(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username is "" or username is None:
        Flag = False
    oj_show = ['all']
    oj_show += DataManager.SuportOJList()
    result_show = DataManager.ResultList()
    language_show = ['all']
    language_show += DataManager.LanguageList()
    if 'page' in req.GET:
        page = req.GET['page']
    else:
        page = 1
    usershow = "", 
    if req.POST:
        print 'POST'
        if cmp(req.POST["oj"],"all") == 0:
            status_list=user_status.objects.all().order_by('-id')
        else:
            status_list=user_status.objects.filter(OJ=req.POST["oj"]).order_by('-id')
        find=oj_show.index(req.POST["oj"])
        first=oj_show[0]
        oj_show[0]=req.POST["oj"]
        oj_show[find]=first
        if cmp(req.POST["language"],"all") != 0:
            status_list=status_list.filter(language=req.POST["language"]).order_by('-id')
        find=language_show.index(req.POST["language"])
        first=language_show[0]
        language_show[0]=req.POST["language"]
        language_show[find]=first
        if cmp(req.POST["result"],"all") != 0:
            status_list=status_list.filter(result=req.POST["result"]).order_by('-id')
        find=result_show.index(req.POST["result"])
        first=result_show[0]
        result_show[0]=req.POST["result"]
        result_show[find]=first
        if cmp(req.POST["user"],"") != 0:
            status_list=status_list.filter(username=req.POST["user"]).order_by('-id')
        print 'Get =', req.POST['user']
        usershow=req.POST["user"]
    else:
        GET = req.GET
        if ('oj' not in GET) or cmp(GET["oj"],"all") == 0:
            status_list=user_status.objects.all().order_by('-id')
            tmp = 'all'
        else:
            status_list=user_status.objects.filter(OJ=GET["oj"]).order_by('-id')
            tmp = GET['oj']
        find=oj_show.index(tmp)
        first=oj_show[0]
        oj_show[0]=tmp
        oj_show[find]=first
        tmp = 'all'
        if ('language' in GET) and cmp(GET["language"],"all") != 0:
            status_list=status_list.filter(language=GET["language"]).order_by('-id')
            tmp = GET["language"]
        find = language_show.index(tmp)
        first = language_show[0]
        language_show[0] = tmp
        language_show[find] = first
        tmp = 'all'
        if ('result' in GET) and cmp(GET["result"],"all") != 0:
            status_list=status_list.filter(result=GET["result"]).order_by('-id')
            tmp = GET['result']
        find=result_show.index(tmp)
        first=result_show[0]
        result_show[0]=tmp
        result_show[find] = first
        if ('user' in GET) and cmp(GET["user"],"") != 0:
            status_list=status_list.filter(username=GET["user"]).order_by('-id')
            usershow = GET["user"]
    ProID_show = ""
    if req.POST:
        if cmp(req.POST["ProID"],"") != 0:
            ProID_show = req.POST["ProID"]
            status_list = status_list.filter(problemID = ProID_show)
    else:
        if ('ProID' in req.GET):
            ProID_show = req.GET["ProID"]
            status_list = status_list.filter(problemID = ProID_show)
    
    paper = PagesManager(name = 'status', now = int(page), data = status_list, segment = 20)
    return render_to_response('status.html',{'status_list' : paper.show_list, 
                                             'Flag' : Flag, 
                                             'username' : username, 
                                             'oj_show' : oj_show, 
                                             'result_show' : result_show, 
                                             'language_show' : language_show, 
                                             'user_show' : usershow, 
                                             'paper' : paper, 
                                             }, 
                              context_instance=RequestContext(req))
