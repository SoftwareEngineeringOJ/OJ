#coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#from datetime import date, datetime
#from django import forms
from models import *
from linker import SubmitCode, CodeManager
from UserManager import UserManager, CodeDisplay
#from django.templatetags.i18n import language
from ProblemManager import ProblemList, StatusList, Display
from Discuss import Discuss
from ContestManager import ContestEditor, ContestManager

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
#修改
def modify(req):
    return UserManager.modify(req);
    
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
    username = req.COOKIES.get('username', '')
    choice = req.GET["id"]
    auser = user.objects.get(userID = choice)
    return render_to_response('myusershow.html', {'auser' : auser, 
                                                  'username' : username}, 
                              context_instance = RequestContext(req))

def mysubmitcode(req):
    return SubmitCode.submit(req, check)

def mycodeshow(req):
    return CodeDisplay.mycodeshow(req)

def contestlist(req):
    return ContestEditor.get_contest_list(req)

def delete_contest_problems(req):
    return ContestEditor.delete_contest_problems(req)

def editcontest(req):
    return ContestEditor.editcontest(req)

def addcontest(req):
    return ContestEditor.addcontest(req)

def contest_show(req):
    return ContestManager.get_contest_show(req)

def contest_problem(req):
    return ContestManager.get_contestproblem(req)

def contest_status(req):
    return ContestManager.get_contest_status(req)

def contest_rank(req):
    return ContestManager.get_contest_rank(req)

def contest_confirm(req):
    return ContestManager.contest_confirm(req)
