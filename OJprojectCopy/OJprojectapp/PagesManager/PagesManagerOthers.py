#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from OJprojectapp.models import *

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
