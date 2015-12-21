#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from OJprojectapp.models import user_status
import CodeManager
import SubmitCode
import urllib

def submit(req):
    username = req.COOKIES.get('username', '')
    sid = req.GET["sid"]
    oj = req.GET["oj"]
    title = req.GET["title"]
    lan = CodeManager.GetOJ(oj).map()
    global check
    if req.POST:
        page = req.POST
        new = user_status(submit_time = datetime.now(), 
                     isprivate = (req.POST["share"] is 'Yes'), 
                     username = username, 
                     language = page['language'], 
                     runID = sid, 
                     result = 'Pending', 
                     OJ = oj, 
                     contestID = 'hello')
        code=req.POST["answer"]
        new.save()
        RunID = new.id
        CodeManager.SaveFile(code, RunID)
        check.push(new)
        postData = {'user': username, 
                    'oj': 'all'} # 发送POST
        postData = urllib.urlencode(postData)
        #print 'To', '/mystatus' + '?' + postData
        return HttpResponseRedirect('/mystatus' + '?' + postData)
    return render_to_response('mysubmitcode.html',{'username':username,'title':title, 'lan':lan},context_instance=RequestContext(req))
