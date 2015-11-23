#-*- coding:utf8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import Problems, Status, User, ProblemsList
from PojSpider import PojSpider


class UserForm(forms.Form):
    #用户表单
    username = forms.CharField(label='用户',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/enter/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#登陆成功，进行操作
def enter(req):
    username = req.COOKIES.get('username','')
    if cmp("",username)==0:
        return render_to_response('oj.html')
    else:
       return render_to_response('enter.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#首页
def oj(req):
    return render_to_response('oj.html')

#用户切换
def cut(req):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    return response

def pojproblems_spider():
    max_page_num = 30
    poj_spider = PojSpider(max_page_num)
    poj_spider.save_allpage()

def problems(req):
    choice=req.GET["id"]
    if cmp(choice,"1") == 0:
        pojproblems_spider()
        problems_list = ProblemsList.objects.all()
    if cmp(choice,"2") == 0:
        problems_list = ProblemsList.objects.filter(OJ="HOJ")
    if cmp(choice,"3") == 0:
        problems_list = ProblemsList.objects.filter(OJ="ZOJ")
    if cmp(choice,"4") == 0:
        problems_list = ProblemsList.objects.filter(OJ="NOJ")
    if cmp(choice,"5") == 0:
        problems_list = ProblemsList.objects.filter(OJ="TYVJ")
    return render_to_response('problems.html',{'problems_list':problems_list},context_instance=RequestContext(req))

def status(req):
    status_list = Status.objects.all()
    return render_to_response('status.html',{'status_list':status_list},context_instance=RequestContext(req))
'''
def rank(req):
    choice = req.GET["id"]
    userdetail_list = Userdetail.objects.all()
    rank_list = [] 
    i = 1
    if cmp(choice,"1") == 0:
        string = "准确率"
        #need sort here according to choice (this is just an example)
        for item in userdetail_list:
            rank_list.append({'rank':i,'name':item.username,'content':item.precision})
            i = i + 1
        #need sort here according to choice
    if cmp(choice,"2")==0:
        string = "答题数量"
        #need sort here according to choice (this is just an example)
        for item in userdetail_list:
            rank_list.append({'rank':i,'name':item.username,'content':item.number})
            i = i + 1
        #need sort here according to choice
    if cmp(choice,"3")==0:
        string = "算法复杂度"
        #need sort here according to choice (this is just an example)
        for item in userdetail_list:
            rank_list.append({'rank':i,'name':item.username,'content':item.algorithm})
            i = i + 1
        #need sort here according to choice
    if cmp(choice,"4")==0:
        string = "答题速度"
        #need sort here according to choice (this is just an example)
        for item in userdetail_list:
            rank_list.append({'rank':i,'name':item.username,'content':item.speed})
            i = i + 1
        #need sort here according to choice
    if cmp(choice,"5")==0:
        string = "综合"
        #need sort here according to choice (this is just an example)
        for item in userdetail_list:
            rank_list.append({'rank':i,'name':item.username,'content':item.sumrank})
            i = i + 1
        #need sort here according to choice
    return render_to_response('rank.html',{'rank_list':rank_list,'string':string},context_instance=RequestContext(req))

def grouprank(req):
    #need sort here (this is just an example)
    grouprank_list = Groupdetail.objects.all()
    #need sort here
    return render_to_response('grouprank.html',{'grouprank_list':grouprank_list},context_instance=RequestContext(req))

def problemshow(req):
    choice = req.GET["id"]
    problem = HOJ_Problems.objects.get(id=choice)
    return render_to_response('problemshow.html',{'problem':problem},context_instance=RequestContext(req))

'''

