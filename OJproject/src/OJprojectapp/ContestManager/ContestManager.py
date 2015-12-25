#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
#from django import forms
from OJprojectapp.models import *
from OJprojectapp.UserManager import UserInit
from OJprojectapp.DataManager import DataManager
import ContestTools
import ContestRank
#from django.templatetags.i18n import language

from django import forms

class UserLoginForm(forms.Form): 
    contest_password = forms.CharField(label='contest_password',widget=forms.PasswordInput())

def confirmed(username, contest_id, req):
    ctest = contest.objects.get(id=contest_id)
    if (ctest.password is None) or (ctest.password == ""):
        return True
    s = username + '+' + contest_id
    s = req.COOKIES.get(s,'')
    if s == None or s is "":
        return False
    return True

def running(contest_id):
    ctest = contest.objects.get(id=contest_id)
    print datetime.now()
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S %f') < ctest.begintime.strftime('%Y-%m-%d %H:%M:%S %f')

def contest_confirm(req):
    username, Flag = UserInit.init(req)
    if "id" in req.GET:
        contest_id = req.GET["id"]
        response = HttpResponseRedirect('/contest_confirm/')
        #将username写入浏览器cookie,失效时间为3600
        response.set_cookie('contest_id', contest_id, 3600)
        return response
    else:
        contest_id = req.COOKIES.get('contest_id','')
        if username == None or username is "":
            return HttpResponseRedirect('/contestlist/')
    print 'contest_id =', contest_id
    #if not confirmed(username, contest_id, req):
    #    return HttpResponseRedirect('/contest_confirm/?id=%s' % contest_id)
    show = False
    warning = ""
    ctest = contest.objects.get(id=contest_id)
    if 'password' in req.GET:
        password = req.GET['password']
        print 'Get password :', password, ctest.password
        if password == ctest.password:
            print 'Confirm passed'
            response = HttpResponseRedirect('/contestshow/?id=%s' % contest_id)
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie(username + '+' + contest_id, 'confirmed', 3600)
            return response
        HttpResponseRedirect('/contest_confirm/')
    List = ContestTools.get_contest_problems_list(contest_id = contest_id)
    problem_id = List[0].id
    return render_to_response('contestcertification.html', {'username' : username, 
                                                            'MapList' : List, 
                                                            'acontest' : ctest, 
                                                            'Flag' : Flag, 
                                                            'problem_id' :problem_id, 
                                                            'show' : show, 
                                                            'contest_id' : contest_id, 
                                                            'warning' : warning, }, 
                              context_instance = RequestContext(req))

def get_contest_show(req):
    username, Flag = UserInit.init(req)
    if "id" in req.GET:
        contest_id = req.GET["id"]
        print contest_id
    if not confirmed(username, contest_id, req):
        return HttpResponseRedirect('/contest_confirm/?id=%s' % contest_id)
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
    if not confirmed(username, contest_id, req):
        return HttpResponseRedirect('/contest_confirm/?id=%s' % contest_id)
    if running(contest_id):
        return HttpResponseRedirect('/contestshow/?id=%s' % contest_id)
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
    if not confirmed(username, contest_id, req):
        return HttpResponseRedirect('/contest_confirm/?id=%s' % contest_id)
    if running(contest_id):
        return HttpResponseRedirect('/contestshow/?id=%s' % contest_id)
    oj_show = ['all']
    oj_show += DataManager.SuportOJList()
    result_show = DataManager.ResultList()
    language_show = ['all']
    language_show += DataManager.LanguageList()
    
    user_show = "", 
    if req.POST:
        print 'POST'
        if cmp(req.POST["oj"],"all") != 0:
            status_list=status_list.filter(OJ=req.POST["oj"]).order_by('-id')
        find=oj_show.index(req.POST["oj"])
        first=oj_show[0]
        oj_show[0]=req.POST["oj"]
        oj_show[find]=first
        if cmp(req.POST["language"],"all") != 0:
            status_list=status_list.filter(language=req.POST["language"]).order_by('-id')
        find=language_show.index(req.POST["language"])
        first=language_show[0]
        language_show[0]=req.POST["language"]
        language_show[find]=first
        if cmp(req.POST["result"],"all") != 0:
            status_list=status_list.filter(result=req.POST["result"]).order_by('-id')
        find=result_show.index(req.POST["result"])
        first=result_show[0]
        result_show[0]=req.POST["result"]
        result_show[find]=first
        if cmp(req.POST["user"],"") != 0:
            status_list=status_list.filter(username=req.POST["user"]).order_by('-id')
        print 'Get =', req.POST['user']
        user_show=req.POST["user"]
    else:
        GET = req.GET
        if ('oj' not in GET) or cmp(GET["oj"],"all") == 0:
            status_list=status_list.order_by('-id')
            tmp = 'all'
        else:
            status_list=status_list.objects.filter(OJ=GET["oj"]).order_by('-id')
            tmp = GET['oj']
        find=oj_show.index(tmp)
        first=oj_show[0]
        oj_show[0]=tmp
        oj_show[find]=first
        tmp = 'all'
        if ('language' in GET) and cmp(GET["language"],"all") != 0:
            status_list=status_list.filter(language=GET["language"]).order_by('-id')
            tmp = GET["language"]
        find = language_show.index(tmp)
        first = language_show[0]
        language_show[0] = tmp
        language_show[find] = first
        tmp = 'all'
        if ('result' in GET) and cmp(GET["result"],"all") != 0:
            status_list=status_list.filter(result=GET["result"]).order_by('-id')
            tmp = GET['result']
        find=result_show.index(tmp)
        first=result_show[0]
        result_show[0]=tmp
        result_show[find] = first
        if ('user' in GET) and cmp(GET["user"],"") != 0:
            status_list=status_list.filter(username=GET["user"]).order_by('-id')
            user_show = GET["user"]
    if req.POST:
        if ('ProID' in req.POST) and cmp(req.POST["ProID"],"") != 0:
            ProID_show = req.POST["ProID"]
            status_list = status_list.filter(problemID = ProID_show)
    else:
        if ('ProID' in req.GET):
            ProID_show = req.GET["ProID"]
            status_list = status_list.filter(problemID = ProID_show)

    return render_to_response("conteststatus.html", {'username' : username, 
                                                      'Flag' : Flag, 
                                                      'contest_id' : contest_id, 
                                                      'status_list' : status_list, 
                                                      'problem_id' : problem_id, 
                                                      'oj_show' : oj_show, 
                                                      'result_show' : result_show, 
                                                      'language_show' : language_show, 
                                                      'user_show' : user_show, }, 
                                  context_instance=RequestContext(req))

def get_contest_rank(req):
    username, Flag = UserInit.init(req)
    if "contest_id" in req.GET:
        contest_id = req.GET["contest_id"]
        mycontest = contest.objects.get(id = contest_id)
        ProblemsList = ContestTools.get_contest_problems_list(contest_id = contest_id)
        problem_id = ProblemsList[0].id
        StatusList = user_status.objects.filter(contestID = contest_id).order_by('id')
        rank_list = ContestRank.GeneratorRank(ProblemsList, StatusList, mycontest.begintime, mycontest.endtime)
    if not confirmed(username, contest_id, req):
        return HttpResponseRedirect('/contest_confirm/?id=%s' % contest_id)
    if running(contest_id):
        return HttpResponseRedirect('/contestshow/?id=%s' % contest_id)
    return render_to_response("contestrank.html", {'username' : username,
                                                   'Flag' : Flag,
                                                   'contest_id' : contest_id,
                                                   'problem_id':problem_id,
                                                   'rank_list':rank_list
                                                   },
                                  context_instance=RequestContext(req))
