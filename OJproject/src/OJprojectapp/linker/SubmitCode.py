#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from OJprojectapp.models import user_status, user
import CodeManager
import urllib

def submit(req, check):
    username = req.COOKIES.get('username', '')
    sid = req.GET["sid"]
    oj = req.GET["oj"]
    title = req.GET["title"]
    lan = CodeManager.GetOJ(oj).map()
    man = user.objects.get(username = username)
    if req.POST:
        page = req.POST
        new = user_status(submit_time = datetime.now(), 
                     is_code_private = (req.POST["sharecode"] is 'Yes'), 
                     userID = man.id, 
                     username = username, 
                     language = page['language'], 
                     problemID = sid, 
                     result = 'Pending', 
                     OJ = oj, 
                     contestID = 'hello', 
                     is_user_private = True)
        code=req.POST["answer"]
        new.save()
        RunID = new.id
        CodeManager.SaveFile(code, RunID)
        check.push(new)
        postData = {'user': username, 
                    'oj': 'all'} # 发送POST
        postData = urllib.urlencode(postData)
        #print 'To', '/mystatus' + '?' + postData
        return HttpResponseRedirect('/status' + '?' + postData)
    return render_to_response('mysubmitcode.html',{'username':username,'title':title, 'lan':lan},context_instance=RequestContext(req))
