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
from django.templatetags.i18n import language

def discuss(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username == None or username is "":
        Flag = False
    if not Flag:
        problemid = req.GET["id"]
        problem = problemslist.objects.get(id=problemid)
        discussion_list = discussion.objects.filter(problemID=problemid)
        return render_to_response('discussion.html',{'username':username,'discussion_list':discussion_list,'problem':problem},context_instance=RequestContext(req))

    if req.GET:
        problemid = req.GET["id"]
        problem = problemslist.objects.get(id=problemid)
        addid = req.GET["addid"]
        if cmp(addid,"-1")!=0:
            add_discussion = discussion.objects.get(id=addid)
            discussion.objects.filter(id=addid).update(like=(int(add_discussion.like) + 1))
    if req.POST:
        speak=req.POST["speak"]
        auser = user.objects.get(username = username)
        discussion.objects.create(userID = auser.id, 
                                  username = username, 
                                  problemID = problemid, 
                                  problemTitle = problem.title, 
                                  speak = speak, 
                                  submit_time = datetime.now(), 
                                  like = 0, )
    discussion_list = discussion.objects.filter(problemID = problemid)

    print 'Username =', username
    return render_to_response('discussion.html', 
                              {'problemid' : problemid, 
                               'Flag' : Flag, 
                               'username' : username, 
                               'discussion_list' : discussion_list, 
                               'problem' : problem}, 
                              context_instance = RequestContext(req))
