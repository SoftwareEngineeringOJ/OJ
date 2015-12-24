#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from OJprojectapp.models import *
from OJprojectapp.linker import CodeManager

def mycodeshow(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username == None or username is "":
        Flag = False
    Private = Flag
    choice = req.GET["id"]
    astatus = user_status.objects.get(id = choice)
    if astatus.is_code_private:
        Private = True
    code = CodeManager.GetFile(RunID = choice)
    return render_to_response('mycodeshow.html',{'astatus' : astatus, 
                                                 'Flag' : Flag, 
                                                 'Private' : Private, 
                                                 'code' : code, }, 
                              context_instance = RequestContext(req))
