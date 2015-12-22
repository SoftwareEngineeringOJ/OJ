#coding=utf-8
'''
Created on 2015年12月21日

@author: Rhapsody
'''
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import date, datetime
from django import forms
from OJprojectapp.models import *

def problemshow(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username is "" or username is None:
        Flag = False
    choice = req.GET["id"]
    problem = problemslist.objects.get(id=choice)
    pic_addr = problem.pic.split()
    return render_to_response('problemshow.html', {'problem' : problem, 
                                                   'pic_addr' : pic_addr, 
                                                   'username' : username, 
                                                   'Flag' : Flag}, 
                              context_instance = RequestContext(req))
