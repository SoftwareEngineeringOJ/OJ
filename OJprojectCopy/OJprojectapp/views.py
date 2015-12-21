#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from models import *

#from spider import PojSpider, HojSpider
from linker import Maneger, SubmitCode, CodeManager
from UserManager import UserManager
from PagesManager import *
from django.templatetags.i18n import language

check = Maneger.Judge()
problem_pagenumber=0
myproblem_pagenumber=0
status_pagenumber=0
mystatus_pagenumber=0

#首页
def oj(req):
    return render_to_response('oj.html')

#注册
def regist(req):
    return UserManager.regist(req)

#登陆
def login(req):
    return UserManager.login(req)

#退出
def logout(req):
    return UserManager.logout()

def problemss(req):
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    global problem_pagenumber
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
            problems_list=problems_list[problem_pagenumber+100:problem_pagenumber+200]
        if req.POST.has_key("2"):
            problems_list=problems_list[problem_pagenumber+200:problem_pagenumber+300]
        if req.POST.has_key("3"):
            problems_list=problems_list[problem_pagenumber+300:problem_pagenumber+400]
        if req.POST.has_key("4"):
            problems_list=problems_list[problem_pagenumber+400:problem_pagenumber+500]
        if req.POST.has_key("5"):
            problems_list=problems_list[problem_pagenumber+500:problem_pagenumber+600]
        if req.POST.has_key("nextpage"):
            problems_list=problems_list[problem_pagenumber+500:problem_pagenumber+600]
            problem_pagenumber+=500
        if req.POST.has_key("previouspage"):
            if(problem_pagenumber>=500):
               problems_list=problems_list[problem_pagenumber:problem_pagenumber+100]
               problem_pagenumber-=500
        if req.POST.has_key("filter"):
            problems_list=problems_list[0:100]
            problem_pagenumber=0
        value1=str(problem_pagenumber+100)
        value2=str(problem_pagenumber+200)
        value3=str(problem_pagenumber+300)
        value4=str(problem_pagenumber+400)
        value5=str(problem_pagenumber+500)
    else:
        problems_list=problemslist.objects.all().order_by('SID')[0:100]
        sid_show=""
        title_show=""
        source_show=""
        value1="100"
        value2="200"
        value3="300"
        value4="400"
        value5="500"
        problem_pagenumber=0
    return render_to_response('problems.html',{'problems_list':problems_list,'oj_show':oj_show,'sid_show':sid_show,'title_show':title_show,'source_show':source_show,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def statuss(req):
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    result_show=["all","Accept","Wrong answer","Compilation Error","Presentation Error","Submit Failed","Memory limit exceeded","Time Limit Exceeded","Output Limit Exceeded"]
    language_show=["all","C","C++","C#","Python","Java"]
    global status_pagenumber
    if req.POST:
        if cmp(req.POST["oj"],"all") == 0:
            status_list=status.objects.all().order_by('-id')
        else:
            status_list=status.objects.filter(OJ=req.POST["oj"]).order_by('-id')
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
            status_list=status_list[status_pagenumber+100:status_pagenumber+200]
        if req.POST.has_key("2"):
            status_list=status_list[status_pagenumber+200:status_pagenumber+300]
        if req.POST.has_key("3"):
            status_list=status_list[status_pagenumber+300:status_pagenumber+400]
        if req.POST.has_key("4"):
            status_list=status_list[status_pagenumber+400:status_pagenumber+500]
        if req.POST.has_key("5"):
            status_list=status_list[status_pagenumber+500:status_pagenumber+600]
        if req.POST.has_key("nextpage"):
            status_list=status_list[status_pagenumber+500:status_pagenumber+600]
            status_pagenumber+=500
        if req.POST.has_key("previouspage"):
            if(status_pagenumber>=500):
               status_list=status_list[status_pagenumber:status_pagenumber+100]
               status_pagenumber-=500
        if req.POST.has_key("filter"):
            status_list=status_list[0:100]
            status_pagenumber=0
        value1=str(status_pagenumber+100)
        value2=str(status_pagenumber+200)
        value3=str(status_pagenumber+300)
        value4=str(status_pagenumber+400)
        value5=str(status_pagenumber+500)
    else:
        status_list=status.objects.all().order_by('-id')[0:100]
        user_show=""
        value1="100"
        value2="200"
        value3="300"
        value4="400"
        value5="500"
        status_pagenumber=0
    return render_to_response('status.html',{'status_list':status_list,'oj_show':oj_show,'result_show':result_show,'language_show':language_show,'usershow':usershow,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def problemshow(req):
    choice = req.GET["id"]
    problem = problems.objects.get(problemID=choice)
    pic_addr = problem.pics.split()
    description = problem.description.split("\r\n")
    inputs = problem.inputs.split("\r\n")
    outputs = problem.output.split("\r\n")
    sample_input = problem.sample_input.split("\r\n")
    sample_output = problem.sample_output.split("\r\n")
    return render_to_response('problemshow.html', {'problem': problem, 'pic_addr': pic_addr,
                                                   "sam_inputs": sample_input,
                                                   "sam_outputs": sample_output,
                                                   "descriptions": description,
                                                   "inputs": inputs,
                                                   "outputs": outputs}
                              , context_instance=RequestContext(req))

def discuss(req):
    username = req.COOKIES.get('username','')
    problemid = req.GET["id"]
    problem = problemslist.objects.get(id=problemid)
    discussion_list = discussion.objects.filter(problemID=problemid)
    return render_to_response('discussion.html',{'username':username,'discussion_list':discussion_list,'problem':problem},context_instance=RequestContext(req))

def usershow(req):
    choice = req.GET["id"]
    auser = user.objects.get(userID=choice)
    return render_to_response('usershow.html', {'auser': auser}, context_instance=RequestContext(req))

def enter(req):
    return PagesManagerOthers.enter(req)
    
def myoj(req):
    username = req.COOKIES.get('username','')
    return render_to_response('myoj.html',{'username':username})


def myproblemss(req):
    username = req.COOKIES.get('username','')
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    global myproblem_pagenumber
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
            problems_list=problems_list[myproblem_pagenumber+100:myproblem_pagenumber+200]
        if req.POST.has_key("2"):
            problems_list=problems_list[myproblem_pagenumber+200:myproblem_pagenumber+300]
        if req.POST.has_key("3"):
            problems_list=problems_list[myproblem_pagenumber+300:myproblem_pagenumber+400]
        if req.POST.has_key("4"):
            problems_list=problems_list[myproblem_pagenumber+400:myproblem_pagenumber+500]
        if req.POST.has_key("5"):
            problems_list=problems_list[myproblem_pagenumber+500:myproblem_pagenumber+600]
        if req.POST.has_key("nextpage"):
            problems_list=problems_list[myproblem_pagenumber+500:myproblem_pagenumber+600]
            myproblem_pagenumber+=500
        if req.POST.has_key("previouspage"):
            if(myproblem_pagenumber>=500):
               problems_list=problems_list[myproblem_pagenumber:myproblem_pagenumber+100]
               myproblem_pagenumber-=500
        if req.POST.has_key("filter"):
            problems_list=problems_list[0:100]
            myproblem_pagenumber=0
        value1=str(myproblem_pagenumber+100)
        value2=str(myproblem_pagenumber+200)
        value3=str(myproblem_pagenumber+300)
        value4=str(myproblem_pagenumber+400)
        value5=str(myproblem_pagenumber+500)
    else:
        problems_list=problemslist.objects.all().order_by('SID')[0:100]
        sid_show=""
        title_show=""
        source_show=""
        value1="100"
        value2="200"
        value3="300"
        value4="400"
        value5="500"
        myproblem_pagenumber=0
    return render_to_response('myproblems.html',{'problems_list':problems_list,'username':username,'oj_show':oj_show,'sid_show':sid_show,'title_show':title_show,'source_show':source_show,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def mystatuss(req):
    username = req.COOKIES.get('username','')
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    result_show=["all","Accept","Wrong answer","Compilation Error","Presentation Error","Submit Failed","Memory limit exceeded","Time Limit Exceeded","Output Limit Exceeded"]
    language_show=["all","C","C++","C#","Python","Java"]
    global mystatus_pagenumber
    if req.POST:
        if cmp(req.POST["oj"],"all") == 0:
            status_list=status.objects.all().order_by('-id')
        else:
            status_list=status.objects.filter(OJ=req.POST["oj"]).order_by('-id')
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
            status_list=status_list[mystatus_pagenumber+100:mystatus_pagenumber+200]
        if req.POST.has_key("2"):
            status_list=status_list[mystatus_pagenumber+200:mystatus_pagenumber+300]
        if req.POST.has_key("3"):
            status_list=status_list[mystatus_pagenumber+300:mystatus_pagenumber+400]
        if req.POST.has_key("4"):
            status_list=status_list[mystatus_pagenumber+400:mystatus_pagenumber+500]
        if req.POST.has_key("5"):
            status_list=status_list[mystatus_pagenumber+500:mystatus_pagenumber+600]
        if req.POST.has_key("nextpage"):
            mystatus_pagenumber+=500
        if req.POST.has_key("previouspage"):
            if(mystatus_pagenumber>=500):
               mystatus_pagenumber-=500
        if req.POST.has_key("filter"):
            mystatus_pagenumber=0
        value1=str(mystatus_pagenumber+100)
        value2=str(mystatus_pagenumber+200)
        value3=str(mystatus_pagenumber+300)
        value4=str(mystatus_pagenumber+400)
        value5=str(mystatus_pagenumber+500)
    else:
        status_list=status.objects.all().order_by('-id')[0:100]
        user_show=""
        value1="100"
        value2="200"
        value3="300"
        value4="400"
        value5="500"
        mystatus_pagenumber=0
    return render_to_response('mystatus.html',{'status_list':status_list,'username':username,'oj_show':oj_show,'result_show':result_show,'language_show':language_show,'usershow':usershow,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def myproblemshow(req):
    username = req.COOKIES.get('username','')
    choice = req.GET["id"]
    problem = problems.objects.get(problemID=choice)
    pic_addr = problem.pics.split()
    description = problem.description.split("\r\n")
    inputs = problem.inputs.split("\r\n")
    outputs = problem.output.split("\r\n")
    sample_input = problem.sample_input.split("\r\n")
    sample_output = problem.sample_output.split("\r\n")
    return render_to_response('myproblemshow.html',
                              {'problem':problem,'username':username,
                               'pic_addr': pic_addr,
                                "sam_inputs": sample_input,
                                "sam_outputs": sample_output,
                                "descriptions": description,
                                "inputs": inputs,
                                "outputs": outputs},context_instance=RequestContext(req))

def myusershow(req):
    username = req.COOKIES.get('username','')
    choice = req.GET["id"]
    auser = user.objects.get(userID=choice)
    return render_to_response('myusershow.html',{'auser':auser,'username':username},context_instance=RequestContext(req))

def mysubmitcode(req):
    return SubmitCode.submit(req, check)

def codeshow(req):
    if req.GET:
        id = req.GET["id"]
        codes = CodeManager.GetFile(id)
        code = codes.split("\n")
    return render_to_response('codeshow.html', {'code':code}, context_instance=RequestContext(req))
