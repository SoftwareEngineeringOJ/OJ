#coding=utf-8
'''
Created on 2015年12月22日

@author: Rhapsody
'''
def init(req):
    username = req.COOKIES.get('username','')
    Flag = True
    if username == None or username is "":
        Flag = False
    return username, Flag