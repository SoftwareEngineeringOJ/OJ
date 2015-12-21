#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from OJprojectapp.models import *

#用户表单
class UserRegisterForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    signature = forms.CharField(label='Signature',max_length=100)
    school = forms.CharField(label='School ',max_length=100)
    email = forms.EmailField(label='Email ',max_length=50)
class UserLoginForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

def usershow(req):
    choice = req.GET["id"]
    auser = user.objects.get(id=choice)
    return render_to_response('usershow.html',{'auser':auser},context_instance=RequestContext(req))

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
            #添加到数据库
            user.objects.create(username = username, 
                                password = password, 
                                signature = signature, 
                                school = school, 
                                email = email, 
                                register_time = datetime.now(), 
                                answered = 0, 
                                right = 0, 
                                wrong=0, 
                                contest_number = 0, 
                                contest_right = 0, 
                                contest_wrong=0)
            response = HttpResponseRedirect('/enter/')
            response.set_cookie('username',username,3600)
            return response
    else:
        uf = UserRegisterForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

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

def logout(req):
    response = HttpResponseRedirect('/oj/')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def index(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username == None or username is "":
        Flag = False
    return render_to_response('oj.html',{'username' : username, 
                                           'Flag' : Flag})

def enter(req):
    username = req.COOKIES.get('username','')
    if cmp("",username)==0:
        return render_to_response('oj.html')
    else:
        theuser = user.objects.get(username=username)
        problems = theuser.problems.all().order_by('-submit_time')
        ac = theuser.problems.all().filter(result='Accept').order_by('-submit_time')
        if len(problems)>0:
           problems1 = problems[0]
        else:
           problems1 = problemslist()
        if len(ac)>0:
            ac1 = ac[0]
        else:
            ac1 = problemslist()
        if len(problems)>1:
           problems2 = problems[1]
        else:
           problems2 = problemslist()
        if len(ac)>1:
            ac2 = ac[1]
        else:
            ac2 = problemslist()
        if len(problems)>2:
           problems3 = problems[2]
        else:
           problems3 = problemslist()
        if len(ac)>2:
            ac3 = ac[2]
        else:
            ac3 = problemslist()
        if len(problems)>3:
           problems4 = problems[3]
        else:
           problems4 = problemslist()
        if len(ac)>3:
            ac4 = ac[3]
        else:
            ac4 = problemslist()
        if len(problems)>4:
           problems5 = problems[4]
        else:
           problems5 = problemslist()
        if len(ac)>4:
            ac5 = ac[4]
        else:
            ac5 = problemslist()
        if len(problems)>5:
           problems_others = problems[5:]
        else:
            problems_others=[]
        if len(ac)>5:
            ac_others = ac[5:]
        else:
            ac_others=[]
        return render_to_response('enter.html' ,{'username':username,'theuser':theuser,'problems1':problems1,'problems2':problems2,'problems3':problems3,'problems4':problems4,'problems5':problems5,'problems_others':problems_others,'ac1':ac1,'ac2':ac2,'ac3':ac3,'ac4':ac4,'ac5':ac5,'ac_others':ac_others})