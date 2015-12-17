#coding=utf-8
'''
Created on 2015年11月23日

@author: Rhapsody
'''

import time
import base64
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
        self.std = ['Waiting', 'Compiling', 'Running & Judging']
        # 等待状态
        self.hostaddr = 'http://poj.org'
        self.loginaddr = '/login'
        self.submaddr = '/submit'
        self.statusaddr = '/status'
        # 对应的链接
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        #httpHandler = urllib2.HTTPHandler(debuglevel=1)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        # 预处理
        
        self.header = {'User-Agent': 'IE10'}
        self.username = 'raft_oj'
        self.password = 'wd55wd'
        # 账号密码
        
        
    def login(self):
        postData = {'user_id1': self.username, 
                    'password1': self.password, 
                    'B1': 'login', 
                    'url' : '/'} # 构造POST数据
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.loginaddr, postData, self.header)
        response = urllib2.urlopen(request, timeout=10)
        if response.getcode() != 200 and response.getcode() != 302:
            print 'login web error!'
            return False # 访问失败
        ans = response.read()
        if ans.find("Log Out") == -1:
            print 'login fail'
            return False # 登录失败
        print 'login successful'
        return True # 登录成功
    
    def find_status(self, page):
        page = page.encode('utf-8')
        res = re.findall(r'user_id=raft_oj>raft_oj</a>(.*?)showsource', page)
        fout = open('res.html', 'wb')
        fout.write(page)
        fout.close()
        if (len(res) <= 0):
            return 'Judge Error'
        tmp = res[0]
        str = tmp.split('<td>')
        time = str[-2]
        time = time.split('<')[0]
        mem = str[-3]
        mem = mem.split('<')[0]
        status = re.findall(r'<font(.*?)</font>', str[-4])[0].split('>')[1]
        return [status, time, mem] # 寻找返回状态
    
    def querystatus(self):
        postData = {'problem_id': '',
                    'user_id': self.username,
                    'result': '',
                    'language': ''} # 构造POST
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.statusaddr + '?' + postData, headers=self.header)
        response = urllib2.urlopen(request, timeout=10)
        if response.getcode() != 200 and response.getcode() != 302:
            print 'query web error!'
            return ['Judge Error', '', ''] # 查询失败
        return self.find_status(response.read()) # 返回即时爬虫结果
    
    def map(self):
        ans = {'G++' : 0, 
               'GCC' : 1, 
               'Java' : 2, 
               'Pascal' : 3, 
               'C++' : 4, 
               'C' : 5, 
               'Fortran' : 6}
        return ans # 返回语言映射关系
    
    def submit(self, pid, lan, code):
        self.login()
        code = base64.b64encode(code) # encode
        pid = pid.encode('utf-8')
        lan = self.map()[lan]
        code = code.encode('utf-8')
        postData = {'problem_id': pid,
                    'language': lan,
                    'source': code,
                    'encoded': 1, 
                    'submit': 'submit'} # 构造POST， 代码部分是需要加密的
        postData = urllib.urlencode(postData)
    
        request = urllib2.Request(self.hostaddr + self.submaddr, postData, self.header)
        response = urllib2.urlopen(request, timeout=10)
        if response.getcode() != 200 and response.getcode() != 302:
            print 'subbmit web error!'
            return ['Judge Error', '', ''] # 提交失败
        print 'Subbmit Done!'
        time.sleep(5) #等待一段时间后再爬虫
        ans = self.querystatus()
        while ans[0] in self.std: # 如果还未评测完成
            time.sleep(1)
            ans = self.querystatus()
        return ans