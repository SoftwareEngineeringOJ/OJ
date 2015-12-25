#coding=utf-8
'''
Created on 2015骞�11鏈�23鏃�

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
        # 绛夊緟鐘舵��
        self.hostaddr = 'http://poj.org'
        self.loginaddr = '/login'
        self.submaddr = '/submit'
        self.statusaddr = '/status'
        # 瀵瑰簲鐨勯摼鎺�
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        #httpHandler = urllib2.HTTPHandler(debuglevel=1)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        # 棰勫鐞�
        
        self.header = {'User-Agent': 'IE10'}
        self.username = 'raft_oj'
        self.password = 'wd55wd'
        # 璐﹀彿瀵嗙爜
        
        
    def login(self):
        postData = {'user_id1': self.username, 
                    'password1': self.password, 
                    'B1': 'login', 
                    'url' : '/'} # 鏋勯�燩OST鏁版嵁
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.loginaddr, postData, self.header)
        try:
            response = urllib2.urlopen(request, timeout=10)
        except:
            return False
        if response.getcode() != 200 and response.getcode() != 302:
            print 'login web error!'
            return False # 璁块棶澶辫触
        ans = response.read()
        if ans.find("Log Out") == -1:
            print 'login fail'
            return False # 鐧诲綍澶辫触
        print 'login successful'
        return True # 鐧诲綍鎴愬姛
    
    def find_status(self, page):
        #page = page.encode('utf-8')
        res = re.findall(r'user_id=raft_oj>raft_oj</a>(.*?)showsource', page)
        #fout = open('res.html', 'wb')
        #fout.write(page)
        #fout.close()
        if (len(res) <= 0):
            return 'Judge Error'
        tmp = res[0]
        str = tmp.split('<td>')
        time = str[-2]
        time = time.split('<')[0]
        mem = str[-3]
        mem = mem.split('<')[0]
        status = re.findall(r'<font(.*?)</font>', str[-4])[0].split('>')[1]
        return [status, time, mem] # 瀵绘壘杩斿洖鐘舵��
    
    def querystatus(self):
        postData = {'problem_id': '',
                    'user_id': self.username,
                    'result': '',
                    'language': ''} # 鏋勯�燩OST
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.statusaddr + '?' + postData, headers=self.header)
        try:
            response = urllib2.urlopen(request, timeout=10)
        except:
            return ['Judge Error', '', '']
        if response.getcode() != 200 and response.getcode() != 302:
            print 'query web error!'
            return ['Judge Error', '', ''] # 鏌ヨ澶辫触
        return self.find_status(response.read()) # 杩斿洖鍗虫椂鐖櫕缁撴灉
    
    def map(self):
        ans = {'G++' : 0, 
               'GCC' : 1, 
               'Java' : 2, 
               'Pascal' : 3, 
               'C++' : 4, 
               'C' : 5, 
               'Fortran' : 6}
        return ans # 杩斿洖璇█鏄犲皠鍏崇郴
    
    def submit(self, pid, lan, code):
        if not self.login():
            return ['Judge Error', '', '']
        code = base64.b64encode(code) # encode
        pid = pid.encode('utf-8')
        lan = self.map()[lan]
        code = code.encode('utf-8')
        postData = {'problem_id': pid,
                    'language': lan,
                    'source': code,
                    'encoded': 1, 
                    'submit': 'submit'} # 鏋勯�燩OST锛� 浠ｇ爜閮ㄥ垎鏄渶瑕佸姞瀵嗙殑
        postData = urllib.urlencode(postData)
    
        request = urllib2.Request(self.hostaddr + self.submaddr, postData, self.header)
        response = urllib2.urlopen(request, timeout=10)
        if response.getcode() != 200 and response.getcode() != 302:
            print 'subbmit web error!'
            return ['Judge Error', '', ''] # 鎻愪氦澶辫触
        print 'Subbmit Done!'
        time.sleep(5) #绛夊緟涓�娈垫椂闂村悗鍐嶇埇铏�
        ans = self.querystatus()
        while ans[0] in self.std: # 濡傛灉杩樻湭璇勬祴瀹屾垚
            time.sleep(1)
            ans = self.querystatus()
        return ans