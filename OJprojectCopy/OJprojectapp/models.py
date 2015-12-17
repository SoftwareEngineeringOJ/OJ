#coding=utf-8
from django.db import models
from django.contrib import admin
# Create your models here.

class user(models.Model):
    userID = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    signature = models.TextField(max_length=200)
    school = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    register_time= models.DateTimeField()

class status(models.Model):
    runID = models.CharField(max_length=15)
    username = models.CharField(max_length=30)
    OJ = models.CharField(max_length=20)
    result = models.CharField(max_length=30)
    memory = models.CharField(max_length=15)
    time = models.CharField(max_length=15)
    language = models.CharField(max_length=10)
    code_file = models.CharField(max_length=50)
    submit_time = models.DateTimeField()
    userID = models.CharField(max_length=30)
    contestID = models.CharField(max_length=10)
    isprivate = models.BooleanField()

class contest(models.Model):
    title = models.CharField(max_length = 50) #比赛标题
    description = models.TextField() #比赛介绍
    announcement = models.TextField() #比赛申明
    password = models.CharField(max_length = 50) #比赛密码，如果为空，则加入空串
    owner = models.CharField(max_length = 50) #创建者ID
    pcnt = 0 #题目数量统计
    ptitles = [models.CharField(max_length = 50)] * 26 #修改的标题，注意和原来的题目可能不一样
    pids = [models.CharField(max_length = 15)] * 26 #题目编号
    sojs = [models.CharField(max_length = 20)] * 26 #来源OJ
    begintime = models.DateTimeField() #开始时间
    endtime = models.DateTimeField() #结束时间

class problemslist(models.Model):
    OJ = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    ratio = models.CharField(max_length=50)
    source = models.CharField(max_length=50)

class problems(models.Model):
    problemID = models.CharField(max_length=15)
    OJ = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    time_limit = models.CharField(max_length=15)
    mem_limit = models.CharField(max_length=15)
    description = models.TextField()
    inputs = models.TextField()
    output = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField(max_length=250)
    hint = models.TextField()
    pics = models.TextField()

class userdetail(models.Model): 
    username = models.CharField(max_length=50)
    precision = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    algorithm = models.CharField(max_length=10)
    speed = models.CharField(max_length=10)
    sumrank = models.CharField(max_length=50)
    problems = models.ManyToManyField(problems)

class groupdetail(models.Model):
    groupname = models.CharField(max_length=50)
    sumrank = models.CharField(max_length=50)
    competedate = models.DateTimeField()

class useradmin(admin.ModelAdmin):
    list_display = ('username','username')
class statusadmin(admin.ModelAdmin):
    list_display = ('runID','userID')
class problemslistadmin(admin.ModelAdmin):
    list_display = ('OJ','source')
class userdetailadmin(admin.ModelAdmin):
    list_display = ('username','sumrank')
class groupdetailadmin(admin.ModelAdmin):
    list_display = ('groupname','sumrank')
class problemsadmin(admin.ModelAdmin):
    list_display = ('OJ','title')


admin.site.register(user,useradmin)
admin.site.register(status,statusadmin)
admin.site.register(problemslist,problemslistadmin)
admin.site.register(problems,problemsadmin)
admin.site.register(userdetail,userdetailadmin)
admin.site.register(groupdetail,groupdetailadmin)