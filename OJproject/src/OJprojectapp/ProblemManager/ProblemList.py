#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from OJprojectapp.models import *
from OJprojectapp.PagesManager import PagesManager

def problemss(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username is "" or username is None:
        Flag = False
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    if 'page' in req.GET:
        page = req.GET['page']
    else:
        page = 1
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
        page = 1
    else:
        GET = req.GET
        if ('oj' not in GET) or cmp(GET["oj"],"all") == 0:
            problems_list=problemslist.objects.all().order_by('SID')
            tmp = 'all'
        else:
            problems_list=problemslist.objects.filter(OJ = GET["oj"]).order_by('SID')
            tmp = GET('oj')
        find=oj_show.index(tmp)
        first=oj_show[0]
        oj_show[0] = tmp
        oj_show[find]=first
        tmp = ""
        if ('sid' in GET) and cmp(GET["sid"],"") != 0:
            problems_list=problems_list.filter(SID=GET["sid"]).order_by('SID')
            tmp = GET['sid']
        sid_show=tmp
        title_show = ""
        if ('title' in GET) and cmp(GET["title"],"") != 0:
            problems_list=problems_list.filter(title=GET["title"]).order_by('SID')
            title_show = GET["title"]
    paper = PagesManager(name = 'problem', now = int(page), data = problems_list, segment = 20)
    page = int(page)
    return render_to_response('problems.html', {'problems_list' : paper.show_list, 
                                                'oj_show' : oj_show, 
                                                'sid_show' : sid_show, 
                                                'title_show' : title_show, 
                                                'Flag' : Flag, 
                                                'username' : username, 
                                                'paper' : paper, }, 
                              context_instance=RequestContext(req))
