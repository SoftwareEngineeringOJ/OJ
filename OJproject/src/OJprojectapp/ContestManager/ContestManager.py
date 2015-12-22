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
#from django.templatetags.i18n import language