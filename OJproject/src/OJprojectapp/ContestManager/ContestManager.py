#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
from django.shortcuts import render, render_to_response
from django.template import RequestContext
#from datetime import date, datetime
#from django import forms
from OJprojectapp.models import *
#from django.templatetags.i18n import language


def get_contest_show(req):
    username = req.COOKIES.get('username','')
    if "id" in req.GET:
        contest_id = req.GET["id"]
        print contest_id
    ctest = contest.objects.get(id=contest_id)
    problems_list = ctest.list.all()
    pro = []
    for i in problems_list:
        pro.append(problemslist.objects.filter(OJ=i.sojs).get(SID=i.pids))
    status = user_status.objects.filter(contestID=contest_id)
    return render_to_response("contestshow.html", {'username':username,
                                                   'problems_list':pro,
                                                   'acontest':ctest,
                                                   'status_list':status},context_instance=RequestContext(req))

def get_contestproblem(req):
    username = req.COOKIES.get('username','')
    if "contest_id" in req.GET:
        contest_id = req.GET["contest_id"]
    if "problem_id" in req.GET:
        problem_id = req.GET["problem_id"]
        problem = problemslist.objects.get(id=problem_id)
        return render_to_response("contestproblem.html", {'username':username,'problem':problem,
                                                   'contest_id':contest_id},context_instance=RequestContext(req))