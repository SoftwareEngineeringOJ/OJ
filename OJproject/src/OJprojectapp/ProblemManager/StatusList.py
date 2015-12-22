#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from OJprojectapp.UserManager import UserManager
from django import forms
from OJprojectapp.models import *
from OJprojectapp.UserManager.UserManager import usershow

def mystatuss(req):
    username = req.COOKIES.get('username','')
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","HDU"]
    result_show=["all","Accept","Wrong answer","Compilation Error","Presentation Error","Submit Failed","Memory limit exceeded","Time Limit Exceeded","Output Limit Exceeded"]
    language_show=["all","C","C++","C#","Python","Java"]
    global mystatus_pagenumber
    if req.POST:
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
        user_show=req.POST["user"]
        if req.POST.has_key("1"):
            status_list=status_list[mystatus_pagenumber+20:mystatus_pagenumber+40]
        if req.POST.has_key("2"):
            status_list=status_list[mystatus_pagenumber+40:mystatus_pagenumber+60]
        if req.POST.has_key("3"):
            status_list=status_list[mystatus_pagenumber+60:mystatus_pagenumber+80]
        if req.POST.has_key("4"):
            status_list=status_list[mystatus_pagenumber+80:mystatus_pagenumber+100]
        if req.POST.has_key("5"):
            status_list=status_list[mystatus_pagenumber+100:mystatus_pagenumber+120]
        if req.POST.has_key("nextpage"):
            status_list=status_list[mystatus_pagenumber+120:mystatus_pagenumber+140]
            mystatus_pagenumber+=100
        if req.POST.has_key("previouspage"):
            if(mystatus_pagenumber>=100):
               mystatus_pagenumber-=100
               status_list=status_list[mystatus_pagenumber:mystatus_pagenumber+20]
        if req.POST.has_key("filter"):
            status_list=status_list[0:20]
            mystatus_pagenumber=0
        value1=str(mystatus_pagenumber+1020)
        value2=str(mystatus_pagenumber+1040)
        value3=str(mystatus_pagenumber+1060)
        value4=str(mystatus_pagenumber+1080)
        value5=str(mystatus_pagenumber+1100)
    else:
        status_list=user_status.objects.all().order_by('-id')[0:20]
        user_show=""
        value1="1020"
        value2="1040"
        value3="1060"
        value4="1080"
        value5="1100"
        mystatus_pagenumber=0
    return render_to_response('mystatus.html',{'status_list':status_list,'username':username,'oj_show':oj_show,'result_show':result_show,'language_show':language_show,'usershow':usershow,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def statuss(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username is "" or username is None:
        Flag = False
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    result_show=["all","Accept","Wrong answer","Compilation Error","Presentation Error","Submit Failed","Memory limit exceeded","Time Limit Exceeded","Output Limit Exceeded"]
    language_show=["all","C","C++","C#","Python","Java"]
    global status_pagenumber
    if req.POST:
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
        user_show=req.POST["user"]
        if req.POST.has_key("1"):
            status_list=status_list[status_pagenumber+20:status_pagenumber+40]
        if req.POST.has_key("2"):
            status_list=status_list[status_pagenumber+40:status_pagenumber+60]
        if req.POST.has_key("3"):
            status_list=status_list[status_pagenumber+60:status_pagenumber+80]
        if req.POST.has_key("4"):
            status_list=status_list[status_pagenumber+80:status_pagenumber+100]
        if req.POST.has_key("5"):
            status_list=status_list[status_pagenumber+100:status_pagenumber+120]
        if req.POST.has_key("nextpage"):
            status_list=status_list[status_pagenumber+120:status_pagenumber+140]
            status_pagenumber+=100
        if req.POST.has_key("previouspage"):
            if(status_pagenumber>=100):
               status_pagenumber-=100
               status_list=status_list[status_pagenumber:status_pagenumber+20]
        if req.POST.has_key("filter"):
            status_list=status_list[0:100]
            status_pagenumber=0
        value1=str(status_pagenumber+1020)
        value2=str(status_pagenumber+1040)
        value3=str(status_pagenumber+1060)
        value4=str(status_pagenumber+1080)
        value5=str(status_pagenumber+1100)
    else:
        status_list=user_status.objects.all().order_by('-id')[0:20]
        user_show=""
        value1="1020"
        value2="1040"
        value3="1060"
        value4="1080"
        value5="1100"
        status_pagenumber=0
    return render_to_response('status.html',{'status_list' : status_list, 
                                             'Flag' : Flag, 
                                             'username' : username, 
                                             'oj_show' : oj_show, 
                                             'result_show' : result_show, 
                                             'language_show' : language_show, 
                                             'usershow' : usershow, 
                                             'value1' : value1, 
                                             'value2' : value2, 
                                             'value3' : value3, 
                                             'value4' : value4, 
                                             'value5' : value5}, 
                              context_instance=RequestContext(req))
