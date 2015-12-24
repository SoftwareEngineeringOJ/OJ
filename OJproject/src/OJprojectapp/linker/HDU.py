#coding=utf-8
'''
Created on 2015/11/22

@author: Rhapsody
'''

import time
import urllib
import urllib2
import cookielib
import re

class Submit(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.std = ['Queuing', 'Compiling', 'Running']

        self.hostaddr = 'http://acm.hdu.edu.cn'
        self.loginaddr = '/userloginex.php?action=login'
        self.submaddr = '/submit.php?action=submit'
        self.statusaddr = '/status.php'
        
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        #httpHandler = urllib2.HTTPHandler(debuglevel=1)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        
        self.header = {'User-Agent': 'IE10'}
        self.username = 'addf400'
        self.password = 'wd55wd'
        
        
    def login(self):
        postData = {'username': self.username,
                    'userpass': self.password,
                    'submit': 'Sign In'}
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.loginaddr, postData, self.header)
        try:
            response = urllib2.urlopen(request, timeout=10)
        except:
            return False
        if response.getcode() != 200 and response.getcode() != 302:
            print 'login web error!'
            return False
        ans = response.read()
        if ans.find("Sign Out") == -1:
            print 'login fail'
            return False
        print 'OK'
        return True
    
    def find_status(self, page):
        res = re.findall(r'<font color(.*?)</font>', page)
        if (len(res) <= 2):
            return 'Judge Error'
        Ans = []
        Ans.append(res[2].split('>')[1]) # find the status
        res = re.findall(r'showproblem(.*?)MS</td>', page)
        tmp = res[0]
        tmp = tmp.split('>')[-1] + 'MS'
        Ans.append(tmp) # find the Exe.Time
        res = re.findall(r'MS</td><td>(.*?)</td><td><a href', page)
        Ans.append(res[0]) # find the Exe.Memory
        return Ans
    
    def querystatus(self):
        postData = {'user': self.username,
                    'lang': 0,
                    'first': '',
                    'pid': '',
                    'status': 0}
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.statusaddr + '?' + postData, headers=self.header)
        try:
            response = urllib2.urlopen(request, timeout=10)
        except:
            return ['Judge Error', '', '']
        if response.getcode() != 200 and response.getcode() != 302:
            print 'query web error!'
            return ['Judge Error', '', '']
        return self.find_status(response.read())
    
    def map(self):
        ans = {'G++' : 0, 
               'GCC' : 1, 
               'C++' : 2, 
               'C' : 3, 
               'Pascal' : 4, 
               'Java' : 5, 
               'C#' : 6}
        return ans
    
    def submit(self, pid, lan, code):
        '''
        lan = language
        0 G++
        1 GCC
        2 C++
        3 C
        4 Pascal
        5 Java
        6 C#
        '''
        if not self.login():
            return ['Judge Error', '', '']
        postData = {'problemid': pid,
                    'language': lan,
                    'usercode': code,
                    'check': 0}
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.submaddr, postData, self.header)
        response = urllib2.urlopen(request, timeout=10)
        if response.getcode() != 200 and response.getcode() != 302:
            print 'subbmit web error!'
            return ['Judge Error', '', '']
        print 'Subbmit Done!'
        time.sleep(5)
        ans = self.querystatus()
        while ans[0] in self.std:
            time.sleep(1)
            print 'Status:', ans[0]
            ans = self.querystatus()
        return ans