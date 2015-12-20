#coding=utf-8
'''
Created on 2015年12月20日

@author: Rhapsody
'''
import urllib
import urllib2
import cookielib
import re

hostaddr = 'http://acm.hit.edu.cn/hoj/problem/view'
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
#httpHandler = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
header = {'User-Agent': 'IE10'}

def html(text):
    f = open('res.html', 'wb')
    f.write(text)
    f.close()
    
def GetTitle(page):
    title = re.findall(r'<h1>(.*?)</h1>', page)
    tl = re.findall(r'<td><strong>Time limit</strong> : (.*?)</td>', page)
    tm = re.findall(r'<td><strong>Memory limit</strong> : (.*?)</td>', page)
    print title, tl, tm
    return title, tl, tm

def GetPage(pid):
    postData = {'id': pid} # 构造POST数据
    postData = urllib.urlencode(postData)
    print 'postData = ', postData
    request = urllib2.Request(hostaddr + '?' + postData, headers=header)
    response = urllib2.urlopen(request, timeout=5)
    if response.getcode() != 200 and response.getcode() != 302:
        print 'login web error!'
        return False # 访问失败
    ans = response.read()
    html(ans)
    title, time_limit, mem_limit = GetTitle(ans)
    OJ = 'hoj'
    problemID = pid
    description
    inputs
    output
    sample_input
    sample_output
    hint
    pics
    
if __name__ == '__main__':
    GetPage(1005)