#-*- coding:utf8 -*-
from django.db import models
from django.contrib import admin
# Create your models here.

class User(models.Model):
    userID = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    signature = models.TextField(max_length=200)
    school = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    register_time= models.DateTimeField()

class Status(models.Model):
    problemID = models.CharField(max_length=15)
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

class ProblemsList(models.Model):
    OJ = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    ratio = models.CharField(max_length=50)
    source = models.CharField(max_length=50)

class Problems(models.Model):
    problemID = models.CharField(max_length=15)
    OJ = models.CharField(max_length=20)
    SID = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    time_limit = models.CharField(max_length=15)
    mem_limit = models.CharField(max_length=15)
    description = models.TextField()
    input = models.TextField()
    output = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    hint = models.TextField()


