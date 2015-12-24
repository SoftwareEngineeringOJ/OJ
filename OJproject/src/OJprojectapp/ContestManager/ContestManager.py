#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#from datetime import date, datetime
#from django import forms
from OJprojectapp.models import *
from OJprojectapp.UserManager import UserInit
import ContestTools
#from django.templatetags.i18n import language

def get_contest_show(req):
    username, Flag = UserInit.init(req)
    if "id" in req.GET:
        contest_id = req.GET["id"]
        print contest_id
    ctest = contest.objects.get(id=contest_id)
    List = ContestTools.get_contest_problems_list(contest_id = contest_id)
    problem_id = List[0].id

    return render_to_response("contestshow.html", {'username' : username,
                                                   'MapList' : List,
                                                   'acontest' : ctest, 
                                                   'Flag' : Flag,
                                                   'problem_id' :problem_id
                                                   },
                              context_instance=RequestContext(req))

def get_contestproblem(req):
    username, Flag = UserInit.init(req)
    if "contest_id" in req.GET:
        contest_id = req.GET["contest_id"]
    if "problem_id" in req.GET:
        problem_id = req.GET["problem_id"]
        tmp = contest_problem.objects.get(id = problem_id)
        problem = problemslist.objects.get(OJ = tmp.sojs, SID = tmp.pids)
        return render_to_response("contestproblem.html", {'username' : username, 
                                                          'problem' : problem, 
                                                          'Flag' : Flag, 
                                                          'problem_id' : problem_id, 
                                                          'contest_id' : contest_id, }, 
                                  context_instance=RequestContext(req))

def get_contest_status(req):
    username, Flag = UserInit.init(req)
    if "contest_id" in req.GET:
        contest_id = req.GET["contest_id"]
        status_list = user_status.objects.filter(contestID=contest_id)
        List = ContestTools.get_contest_problems_list(contest_id = contest_id)
        problem_id = List[0].id
    return render_to_response("conteststatus.html", {'username' : username,
                                                      'Flag' : Flag,
                                                      'contest_id' : contest_id,
                                                      'status_list':status_list,
                                                      'problem_id':problem_id},
                                  context_instance=RequestContext(req))
def get_contest_rank(req):
    username, Flag = UserInit.init(req)
    if "contest_id" in req.GET:
        contest_id = req.GET["contest_id"]
        List = ContestTools.get_contest_problems_list(contest_id = contest_id)
        problem_id = List[0].id
        rank_list = []
    return render_to_response("contestrank.html", {'username' : username,
                                                   'Flag' : Flag,
                                                   'contest_id' : contest_id,
                                                   'problem_id':problem_id,
                                                   'rank_list':rank_list
                                                   },
                                  context_instance=RequestContext(req))
