#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from models import *
from linker import Maneger, SubmitCode, CodeManager
from UserManager import UserManager
from django.templatetags.i18n import language
from ProblemManager import ProblemList, StatusList, Display
from OJprojectapp.Discuss import Discuss

import linker.Maneger
check = linker.Maneger.Judge()
#首页
def oj(req):
    return UserManager.index(req)
#注册
def regist(req):
    return UserManager.regist(req)
#登陆
def login(req):
    return UserManager.login(req)
#退出
def logout(req):
    return UserManager.logout(req)

def enter(req):
    return UserManager.enter(req)

def problemss(req):
    return ProblemList.problemss(req)

def statuss(req):
    return StatusList.statuss(req)

def problemshow(req):
    return Display.problemshow(req)

def discuss(req):
    return Discuss.discuss(req)

def usershow(req):
    return UserManager.usershow(req)

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
