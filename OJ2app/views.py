#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import user,user_status
from models import problemslist,discussion


problem_pagenumber=0
myproblem_pagenumber=0
status_pagenumber=0
mystatus_pagenumber=0

#from spider import PojSpider, HojSpider
'''
poj = PojSpider()
problemslist.objects.filter(OJ="POJ").delete()
poj.save_allpage()

hoj = HojSpider()
problemslist.objects.filter(OJ="HOJ").delete()
hoj.save_allpage()
'''


#用户表单
class UserRegisterForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    signature = forms.CharField(label='Signature',max_length=100)
    school = forms.CharField(label='School         ',max_length=100)
    email = forms.EmailField(max_length=50)
    register_time = forms.DateTimeField()
class UserLoginForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())


#首页
def oj(req):
    return render_to_response('oj.html')

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserRegisterForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            signature = uf.cleaned_data['signature']
            school = uf.cleaned_data['school']
            email = uf.cleaned_data['email']
            register_time = uf.cleaned_data['register_time']
            #添加到数据库
            user.objects.create(username= username,password=password,signature=signature,school=school,email=email,register_time=register_time)
            response = HttpResponseRedirect('/enter/')
            response.set_cookie('username',username,3600)
            return response
    else:
        uf = UserRegisterForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserLoginForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            auser = user.objects.filter(username= username,password= password)
            if auser:
                #比较成功，跳转index
                response = HttpResponseRedirect('/enter/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/')
    else:
        uf = UserLoginForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))


def problemss(req):
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    global problem_pagenumber
    if req.POST:
        if cmp(req.POST["oj"],"all") == 0:
            problems_list=problemslist.objects.all().order_by('SID')
        else:
            problems_list=problemslist.objects.filter(OJ=req.POST["oj"]).order_by('SID')
        find=oj_show.index(req.POST["oj"])
        first=oj_show[0]
        oj_show[0]=req.POST["oj"]
        oj_show[find]=first
        if cmp(req.POST["sid"],"") != 0:
            problems_list=problems_list.filter(SID=req.POST["sid"]).order_by('SID')
        sid_show=req.POST["sid"]
        if cmp(req.POST["title"],"") != 0:
            problems_list=problems_list.filter(title=req.POST["title"]).order_by('SID')
        title_show=req.POST["title"]
        if cmp(req.POST["source"],"") != 0:
            problems_list=problems_list.filter(source=req.POST["source"]).order_by('SID')
        source_show=req.POST["source"]
        if req.POST.has_key("1"):
            problems_list=problems_list[problem_pagenumber+20:problem_pagenumber+40]
        if req.POST.has_key("2"):
            problems_list=problems_list[problem_pagenumber+40:problem_pagenumber+60]
        if req.POST.has_key("3"):
            problems_list=problems_list[problem_pagenumber+60:problem_pagenumber+80]
        if req.POST.has_key("4"):
            problems_list=problems_list[problem_pagenumber+80:problem_pagenumber+100]
        if req.POST.has_key("5"):
            problems_list=problems_list[problem_pagenumber+100:problem_pagenumber+120]
        if req.POST.has_key("nextpage"):
            problems_list=problems_list[problem_pagenumber+120:problem_pagenumber+140]
            problem_pagenumber+=100
        if req.POST.has_key("previouspage"):
            if(problem_pagenumber>=100):
               problem_pagenumber-=100
               problems_list=problems_list[problem_pagenumber:problem_pagenumber+20]
        if req.POST.has_key("filter"):
            problems_list=problems_list[0:20]
            problem_pagenumber=0
        value1=str(problem_pagenumber+1020)
        value2=str(problem_pagenumber+1040)
        value3=str(problem_pagenumber+1060)
        value4=str(problem_pagenumber+1080)
        value5=str(problem_pagenumber+1100)
    else:
        problems_list=problemslist.objects.all().order_by('SID')[0:20]
        sid_show=""
        title_show=""
        source_show=""
        value1="1020"
        value2="1040"
        value3="1060"
        value4="1080"
        value5="1100"
        problem_pagenumber=0
    return render_to_response('problems.html',{'problems_list':problems_list,'oj_show':oj_show,'sid_show':sid_show,'title_show':title_show,'source_show':source_show,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def statuss(req):
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    result_show=["all","Accept","Wrong answer","Compilation Error","Presentation Error","Submit Failed","Memory limit exceeded","Time Limit Exceeded","Output Limit Exceeded"]
    language_show=["all","C","C++","C#","Python","Java"]
    global status_pagenumber
    if req.POST:
        if cmp(req.POST["oj"],"all") == 0:
            status_list=user_status.objects.all().order_by('-id')
        else:
            status_list=user_status.objects.filter(OJ=req.POST["oj"]).order_by('-id')
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
        user_show=req.POST["user"]
        if req.POST.has_key("1"):
            status_list=status_list[status_pagenumber+20:status_pagenumber+40]
        if req.POST.has_key("2"):
            status_list=status_list[status_pagenumber+40:status_pagenumber+60]
        if req.POST.has_key("3"):
            status_list=status_list[status_pagenumber+60:status_pagenumber+80]
        if req.POST.has_key("4"):
            status_list=status_list[status_pagenumber+80:status_pagenumber+100]
        if req.POST.has_key("5"):
            status_list=status_list[status_pagenumber+100:status_pagenumber+120]
        if req.POST.has_key("nextpage"):
            status_list=status_list[status_pagenumber+120:status_pagenumber+140]
            status_pagenumber+=100
        if req.POST.has_key("previouspage"):
            if(status_pagenumber>=100):
               status_pagenumber-=100
               status_list=status_list[status_pagenumber:status_pagenumber+20]
        if req.POST.has_key("filter"):
            status_list=status_list[0:100]
            status_pagenumber=0
        value1=str(status_pagenumber+1020)
        value2=str(status_pagenumber+1040)
        value3=str(status_pagenumber+1060)
        value4=str(status_pagenumber+1080)
        value5=str(status_pagenumber+1100)
    else:
        status_list=user_status.objects.all().order_by('-id')[0:20]
        user_show=""
        value1="1020"
        value2="1040"
        value3="1060"
        value4="1080"
        value5="1100"
        status_pagenumber=0
    return render_to_response('status.html',{'status_list':status_list,'oj_show':oj_show,'result_show':result_show,'language_show':language_show,'usershow':usershow,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def problemshow(req):
    choice = req.GET["id"]
    problem = problemslist.objects.get(id=choice)
    return render_to_response('problemshow.html',{'problem':problem},context_instance=RequestContext(req))

def discuss(req):
    username = req.COOKIES.get('username','')
    problemid = req.GET["id"]
    problem = problemslist.objects.get(id=problemid)
    discussion_list = discussion.objects.filter(problemID=problemid)
    return render_to_response('discussion.html',{'username':username,'discussion_list':discussion_list,'problem':problem},context_instance=RequestContext(req))

def usershow(req):
    choice = req.GET["id"]
    auser = user.objects.get(id=choice)
    return render_to_response('usershow.html',{'auser':auser},context_instance=RequestContext(req))

def logout(req):
    response = HttpResponseRedirect('/oj/')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def enter(req):
    username = req.COOKIES.get('username','')
    if cmp("",username)==0:
        return render_to_response('oj.html')
    else:
       return render_to_response('enter.html' ,{'username':username})

def myoj(req):
    username = req.COOKIES.get('username','')
    return render_to_response('myoj.html',{'username':username})

def myproblemss(req):
    username = req.COOKIES.get('username','')
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    global myproblem_pagenumber
    if req.POST:
        if cmp(req.POST["oj"],"all") == 0:
            problems_list=problemslist.objects.all().order_by('SID')
        else:
            problems_list=problemslist.objects.filter(OJ=req.POST["oj"]).order_by('SID')
        find=oj_show.index(req.POST["oj"])
        first=oj_show[0]
        oj_show[0]=req.POST["oj"]
        oj_show[find]=first
        if cmp(req.POST["sid"],"") != 0:
            problems_list=problems_list.filter(SID=req.POST["sid"]).order_by('SID')
        sid_show=req.POST["sid"]
        if cmp(req.POST["title"],"") != 0:
            problems_list=problems_list.filter(title=req.POST["title"]).order_by('SID')
        title_show=req.POST["title"]
        if cmp(req.POST["source"],"") != 0:
            problems_list=problems_list.filter(source=req.POST["source"]).order_by('SID')
        source_show=req.POST["source"]
        if req.POST.has_key("1"):
            problems_list=problems_list[myproblem_pagenumber+20:myproblem_pagenumber+40]
        if req.POST.has_key("2"):
            problems_list=problems_list[myproblem_pagenumber+40:myproblem_pagenumber+60]
        if req.POST.has_key("3"):
            problems_list=problems_list[myproblem_pagenumber+60:myproblem_pagenumber+80]
        if req.POST.has_key("4"):
            problems_list=problems_list[myproblem_pagenumber+80:myproblem_pagenumber+100]
        if req.POST.has_key("5"):
            problems_list=problems_list[myproblem_pagenumber+100:myproblem_pagenumber+120]
        if req.POST.has_key("nextpage"):
            problems_list=problems_list[myproblem_pagenumber+120:myproblem_pagenumber+140]
            myproblem_pagenumber+=100
        if req.POST.has_key("previouspage"):
            if(myproblem_pagenumber>=100):
               myproblem_pagenumber-=100
               problems_list=problems_list[myproblem_pagenumber:myproblem_pagenumber+20]
        if req.POST.has_key("filter"):
            problems_list=problems_list[0:100]
            myproblem_pagenumber=0
        value1=str(myproblem_pagenumber+1020)
        value2=str(myproblem_pagenumber+1040)
        value3=str(myproblem_pagenumber+1060)
        value4=str(myproblem_pagenumber+1080)
        value5=str(myproblem_pagenumber+1100)
    else:
        problems_list=problemslist.objects.all().order_by('SID')[0:20]
        sid_show=""
        title_show=""
        source_show=""
        value1="1020"
        value2="1040"
        value3="1060"
        value4="1080"
        value5="1100"
        myproblem_pagenumber=0
    return render_to_response('myproblems.html',{'problems_list':problems_list,'username':username,'oj_show':oj_show,'sid_show':sid_show,'title_show':title_show,'source_show':source_show,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def mystatuss(req):
    username = req.COOKIES.get('username','')
    oj_show=["all","POJ","HOJ","NOJ","ZOJ","TYVJ"]
    result_show=["all","Accept","Wrong answer","Compilation Error","Presentation Error","Submit Failed","Memory limit exceeded","Time Limit Exceeded","Output Limit Exceeded"]
    language_show=["all","C","C++","C#","Python","Java"]
    global mystatus_pagenumber
    if req.POST:
        if cmp(req.POST["oj"],"all") == 0:
            status_list=user_status.objects.all().order_by('-id')
        else:
            status_list=user_status.objects.filter(OJ=req.POST["oj"]).order_by('-id')
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
        user_show=req.POST["user"]
        if req.POST.has_key("1"):
            status_list=status_list[mystatus_pagenumber+20:mystatus_pagenumber+40]
        if req.POST.has_key("2"):
            status_list=status_list[mystatus_pagenumber+40:mystatus_pagenumber+60]
        if req.POST.has_key("3"):
            status_list=status_list[mystatus_pagenumber+60:mystatus_pagenumber+80]
        if req.POST.has_key("4"):
            status_list=status_list[mystatus_pagenumber+80:mystatus_pagenumber+100]
        if req.POST.has_key("5"):
            status_list=status_list[mystatus_pagenumber+100:mystatus_pagenumber+120]
        if req.POST.has_key("nextpage"):
            status_list=status_list[mystatus_pagenumber+120:mystatus_pagenumber+140]
            mystatus_pagenumber+=100
        if req.POST.has_key("previouspage"):
            if(mystatus_pagenumber>=100):
               mystatus_pagenumber-=100
               status_list=status_list[mystatus_pagenumber:mystatus_pagenumber+20]
        if req.POST.has_key("filter"):
            status_list=status_list[0:20]
            mystatus_pagenumber=0
        value1=str(mystatus_pagenumber+1020)
        value2=str(mystatus_pagenumber+1040)
        value3=str(mystatus_pagenumber+1060)
        value4=str(mystatus_pagenumber+1080)
        value5=str(mystatus_pagenumber+1100)
    else:
        status_list=user_status.objects.all().order_by('-id')[0:20]
        user_show=""
        value1="1020"
        value2="1040"
        value3="1060"
        value4="1080"
        value5="1100"
        mystatus_pagenumber=0
    return render_to_response('mystatus.html',{'status_list':status_list,'username':username,'oj_show':oj_show,'result_show':result_show,'language_show':language_show,'usershow':usershow,'value1':value1,'value2':value2,'value3':value3,'value4':value4,'value5':value5},context_instance=RequestContext(req))

def myproblemshow(req):
    username = req.COOKIES.get('username','')
    choice = req.GET["id"]
    problem = problemslist.objects.get(id=choice)
    return render_to_response('myproblemshow.html',{'problem':problem,'username':username},context_instance=RequestContext(req))

def myusershow(req):
    choice = req.GET["id"]
    auser = user.objects.get(id=choice)
    return render_to_response('myusershow.html',{'auser':auser},context_instance=RequestContext(req))

def mycodeshow(req):
    choice = req.GET["id"]
    astatus = user_status.objects.get(id=choice)
    return render_to_response('mycodeshow.html',{'astatus':astatus},context_instance=RequestContext(req))

def mysubmitcode(req):
    username = req.COOKIES.get('username','')
    sid = req.GET["sid"]
    oj = req.GET["oj"]
    title = req.GET["title"]
    problemid = req.GET["id"]

    if req.POST:
        answer=req.POST["answer"]
        language=req.POST["language"]
        share =req.POST["share"]
    return render_to_response('mysubmitcode.html',{'username':username,'title':title,'problemid':problemid},context_instance=RequestContext(req))

def mydiscuss(req):
    username = req.COOKIES.get('username','')
    problemid = req.GET["id"]
    problem = problemslist.objects.get(id=problemid)
    if req.POST:
        speak=req.POST["speak"]
        auser = user.objects.get(username=username)
        discussion.objects.create(userID= auser.id,username=username,problemID=problemid,problemTitle=problem.title,speak=speak)
    discussion_list = discussion.objects.filter(problemID=problemid)
    return render_to_response('mydiscussion.html',{'username':username,'discussion_list':discussion_list,'problem':problem},context_instance=RequestContext(req))


