#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from models import *
import urllib

from linker import CodeManager, Maneger, POJ
from django.templatetags.i18n import language

check = Maneger.Judge()
#from spider import PojSpider, HojSpider
'''
poj = PojSpider()
problems.objects.filter(OJ="POJ").delete()
problemslist.objects.filter(OJ="POJ").delete()
poj.save_allpage()

hoj = HojSpider()
problems.objects.filter(OJ="HOJ").delete()
problemslist.objects.filter(OJ="HOJ").delete()
hoj.save_allpage()
'''
#用户表单
class UserRegisterForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    signature = forms.CharField(label='Signature',max_length=100)
    school = forms.CharField(label='School         ',max_length=100)
    email = forms.EmailField(max_length=50)
    register_time = forms.DateTimeField()
class UserLoginForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

#首页
def oj(req):
    return render_to_response('oj.html')

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserRegisterForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            signature = uf.cleaned_data['signature']
            school = uf.cleaned_data['school']
            email = uf.cleaned_data['email']
            register_time = uf.cleaned_data['register_time']
            #添加到数据库
            user.objects.create(username= username,password=password,signature=signature,school=school,email=email,register_time=register_time)
            response = HttpResponseRedirect('/enter/')
            response.set_cookie('username',username,3600)
            return response
    else:
        uf = UserRegisterForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserLoginForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            auser = user.objects.filter(username= username,password= password)
            if auser:
                #比较成功，跳转index
                response = HttpResponseRedirect('/enter/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/')
    else:
        uf = UserLoginForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

def problemss(req):
    if req.GET:
        if cmp(req.GET["oj"],"all") == 0:
            problems_list=problemslist.objects.all()
        else:
            problems_list=problemslist.objects.filter(OJ=req.GET["oj"])
        if cmp(req.GET["sid"],"") != 0:
            problems_list=problems_list.filter(SID=req.GET["sid"])
        if cmp(req.GET["title"],"") != 0:
            problems_list=problems_list.filter(title=req.GET["title"])
        if cmp(req.GET["source"],"") != 0:
            problems_list=problems_list.filter(source=req.GET["source"])
    else:
        problems_list=problemslist.objects.all()
    return render_to_response('problems.html',{'problems_list':problems_list},context_instance=RequestContext(req))

def statuss(req):
    if req.GET:
        oj = req.GET('oj', False)
        print 'oj = ', oj
        return render_to_response('status.html')
        if cmp(oj,"") == 0 or cmp(oj, "all") == 0:
            status_list=status.objects.all()
        else:
            status_list=status.objects.filter(OJ=req.GET["oj"])
        return render_to_response('status.html',{'status_list':status_list},context_instance=RequestContext(req))
        language = req.GET("language", False)
        if cmp(language, "all") != 0:
            status_list=status_list.filter(language=req.GET["language"])
        result = req.GET('result', False)
        if cmp(result,"all") != 0:
            status_list=status_list.filter(result=req.GET["result"])
        user = req.GET('user', False)
        if cmp(user, "") != 0:
            status_list=status_list.filter(username=req.GET["user"])
    else:
        status_list=status.objects.all()
    return render_to_response('status.html',{'status_list':status_list},context_instance=RequestContext(req))

def problemshow(req):
    choice = req.GET["id"]
    problem = problems.objects.get(problemID=choice)
    pic_addr = problem.pics.split()
    return render_to_response('problemshow.html',{'problem':problem, 'pic_addr':pic_addr},context_instance=RequestContext(req))

def usershow(req):
    choice = req.GET["id"]
    auser = user.objects.get(userID=choice)
    return render_to_response('usershow.html',{'auser':auser},context_instance=RequestContext(req))

def logout(req):
    response = HttpResponseRedirect('/oj/')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def enter(req):
    username = req.COOKIES.get('username','')
    if cmp("",username)==0:
        return render_to_response('oj.html')
    else:
       return render_to_response('enter.html' ,{'username':username})

def myoj(req):
    username = req.COOKIES.get('username','')
    return render_to_response('myoj.html',{'username':username})


def myproblemss(req):
    username = req.COOKIES.get('username','')
    if req.GET:
        if cmp(req.GET["oj"],"all") == 0:
            problems_list=problemslist.objects.all()
        else:
            problems_list=problemslist.objects.filter(OJ=req.GET["oj"])
        if cmp(req.GET["sid"],"") != 0:
            problems_list=problems_list.filter(SID=req.GET["sid"])
        if cmp(req.GET["title"],"") != 0:
            problems_list=problems_list.filter(title=req.GET["title"])
        if cmp(req.GET["source"],"") != 0:
            problems_list=problems_list.filter(source=req.GET["source"])
    else:
        problems_list=problemslist.objects.all()
    return render_to_response('myproblems.html',{'problems_list':problems_list,'username':username},context_instance=RequestContext(req))

def mystatuss(req):
    username = req.COOKIES.get('username','')
    if req.GET:
        if cmp(req.GET["oj"],"") == 0 or cmp(req.GET["oj"],"all") == 0:
            status_list=status.objects.all()
        else:
            status_list=status.objects.filter(OJ=req.GET["oj"])
        if cmp(req.GET["language"],"all") != 0:
            status_list=status_list.filter(language=req.GET["language"])
        if cmp(req.GET["result"],"all") != 0:
            status_list=status_list.filter(result=req.GET["result"])
        if cmp(req.GET["user"],"") != 0:
            status_list=status_list.filter(username=req.GET["user"])
    else:
        status_list=status.objects.all()
    return render_to_response('mystatus.html',{'status_list':status_list,'username':username},context_instance=RequestContext(req))

def myproblemshow(req):
    username = req.COOKIES.get('username','')
    choice = req.GET["id"]
    problem = problems.objects.get(problemID=choice)
    return render_to_response('myproblemshow.html',{'problem':problem,'username':username},context_instance=RequestContext(req))

def myusershow(req):
    username = req.COOKIES.get('username','')
    choice = req.GET["id"]
    auser = user.objects.get(userID=choice)
    return render_to_response('myusershow.html',{'auser':auser,'username':username},context_instance=RequestContext(req))

def mysubmitcode(req):
    username = req.COOKIES.get('username', '')
    sid = req.GET["sid"]
    oj = req.GET["oj"]
    title = req.GET["title"]
    lan = POJ.Submit().map()
    
    if req.POST:
        page = req.POST
        new = status(submit_time = datetime.now(), 
                     isprivate = True, 
                     username = username, 
                     language = page['language'], 
                     runID = sid, 
                     result = 'Pending', 
                     OJ = oj, 
                     contestID = 'hello')
        code=req.POST["answer"]
        new.save()
        RunID = new.id
        CodeManager.SaveFile(code, RunID)
        check.push(new)
        postData = {'user': username, 
                    'oj': 'all'} # 构造POST
        postData = urllib.urlencode(postData)
        #return HttpResponseRedirect('/mystatus' + '?' + postData)
    return render_to_response('mysubmitcode.html',{'username':username,'title':title, 'lan':lan},context_instance=RequestContext(req))

