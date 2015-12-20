#coding=utf-8
'''
Created on 2015年12月17日

@author: Rhapsody
'''
import time
import base64
import urllib
import urllib2
import cookielib
import re

class Submit(object):
    def __init__(self):
        self.std = ['Queuing', 'Compiling', 'Running & Judging', 'Running'] #还有正在编译没有确认
        # 等待状态
        self.hostaddr = 'http://acm.hit.edu.cn'
        self.loginaddr = '/hoj/system/login'
        self.submaddr = '/hoj/problem/submit'
        self.statusaddr = '/hoj/problem/status'
        # 对应的链接
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        #httpHandler = urllib2.HTTPHandler(debuglevel=1)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        # 预处理
        
        self.header = {'User-Agent': 'IE10'}
        self.username = 'addfoj'
        self.password = 'wd55wd'
        # 账号密码
        
    def html(self, text):
        f = open('res.html', 'wb')
        f.write(text)
        f.close()
        
    def login(self):
        postData = {'user': self.username, 
                    'password': self.password, 
                    'submit': 'Login'} # 构造POST数据
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.loginaddr, postData, self.header)
        response = urllib2.urlopen(request, timeout=10)
        if response.getcode() != 200 and response.getcode() != 302:
            print 'login web error!'
            return False # 访问失败
        ans = response.read()
        if ans.find("Logout") == -1:
            print 'login fail'
            return False # 登录失败
        print 'login successful'
        return True # 登录成功
    
    def find_status(self, page):
        self.html(page)
        res = page.split('<tbody>')[2].split('</tbody>')[0]
        rec = res.split('</tr>')[0]
        rec = re.findall(r'<td(.*?)</td>', rec)
        result = rec[2].split('>')[1]
        time = rec[3].split('>')[1]
        memory = rec[4].split('>')[1]
        return [result, time, memory] # 寻找返回状态
    
    def querystatus(self):
        postData = {'author' : self.username} # 构造POST
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.hostaddr + self.statusaddr + '?' + postData, headers=self.header)
        response = urllib2.urlopen(request, timeout=10)
        if response.getcode() != 200 and response.getcode() != 302:
            print 'query web error!'
            return ['Judge Error', '', ''] # 查询失败
        return self.find_status(response.read()) # 返回即时爬虫结果
    
    def map(self):
        ans = {'C++' : 'C++', 
               'C89' : 'C89', 
               'Java' : 'Java', 
               'Pascal' : 'Pascal'}
        return ans # 返回语言映射关系
    
    def submit(self, pid, lan, code):
        self.login()
        pid = pid.encode('utf-8')
        lan = self.map()[lan]
        #code = code.encode('utf-8')
        postData = {'Proid': pid,
                    'Language': lan,
                    'Source': code} # 构造POST， 代码部分是需要加密的
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

if __name__ == '__main__':
    fin = open('a.txt', 'r')
    code = fin.read()
    Submit().submit('1001', 'C++', code)
