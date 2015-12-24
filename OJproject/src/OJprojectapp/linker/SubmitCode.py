#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
#from datetime import datetime
from django.utils import timezone
from OJprojectapp.models import user_status, user, contest_problem
import CodeManager
import urllib

def submit(req, check):
    username = req.COOKIES.get('username', '')
    contestID = 'hello'
    if 'contest_id' in req.GET:
        pid = req.GET['problem_id']
        contestID = req.GET['contest_id']
        aim = contest_problem.objects.get(id = pid)
        sid = aim.pids
        oj = aim.sojs
    else:
        sid = req.GET["sid"]
        oj = req.GET["oj"]
    title = req.GET["title"]
    lan = CodeManager.GetOJ(oj).map()
    man = user.objects.get(username = username)
    if req.POST:
        page = req.POST
        new = user_status(submit_time = timezone.now(), 
                          is_code_private = page["sharecode"] == "Yes", 
                          userID = man.id, 
                          username = username, 
                          language = page['language'], 
                          problemID = sid, 
                          result = 'Pending', 
                          problemTitle = title, 
                          OJ = oj, 
                          contestID = contestID, 
                          is_user_private = True)
        code=req.POST["answer"]
        new.save()
        RunID = new.id
        CodeManager.SaveFile(code, RunID)
        check.push(new)
        postData = {'user' : username, 
                    'oj': 'all'} # 发送POST
        postData = urllib.urlencode(postData)
        #print 'To', '/mystatus' + '?' + postData
        #如果是比赛，那么需要跳转到比赛的status
        return HttpResponseRedirect('/status' + '?' + postData)
    return render_to_response('mysubmitcode.html',{'username':username,'title':title, 'lan':lan},context_instance=RequestContext(req))
