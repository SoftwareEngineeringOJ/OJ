#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from OJprojectapp.models import *

def problemss(req):
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
