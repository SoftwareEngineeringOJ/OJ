#-*- coding:utf8 -*-
import sys
import requests
from lxml import etree
import re

reload(sys)
sys.setdefaultencoding("utf-8")
'''
url = "http://codeforces.com/problemset/page/3"
html = requests.get(url)
page = etree.HTML(html.text,parser=etree.HTMLParser(encoding='utf-8'))

for i in range(2, 10):
    ID = page.xpath('//*[@id="pageContent"]/div[2]/div[6]/table//tr[%d]/td[1]/a/text()'%i)[0]
    href = page.xpath('//*[@id="pageContent"]/div[2]/div[6]/table//tr[%d]/td[2]/div[1]/a/@href'%i)[0]
    title = page.xpath('//*[@id="pageContent"]/div[2]/div[6]/table//tr[%d]/td[2]/div[1]/a/text()'%i)[0]
    ratio = ""

    print title,ID,href

url = "http://codeforces.com/problemset/problem/550/C"
html = requests.get(url)
page = etree.HTML(html.text, parser=etree.HTMLParser(encoding='utf-8'))
#file_object = open('file.txt', 'w')
#file_object.write(html.text)

title = page.xpath('//*[@id="content"]/h1/text()')[0]
time_limit = page.xpath('//*[@id="request"]/table//tr[2]/td[2]')[0].xpath('string(.)')
mem_limit = page.xpath('//*[@id="request"]/table//tr[2]/td[4]')[0].xpath('string(.)')
description = page.xpath('//*[@id="problem-detail"]')[0].xpath('string(.)')
_input = page.xpath('/html/body/table[2]//tr/td/div[5]')[0].xpath('string(.)')
_output = page.xpath('/html/body/table[2]//tr/td/div[6]')[0].xpath('string(.)')
sample_input = page.xpath('//*[@id="problem-detail"]/pre[2]/text()')[0]
sample_output = page.xpath('//*[@id="problem-detail"]/pre[2]/text()')[0]
hint = ""#page.xpath('/html/body/table[2]//tr/td/div[7]/text()')[0]
print title,time_limit,mem_limit
print description

#print sample_input
#print sample_output
'''

url = "http://poj.org/problem?id=1099"
html = requests.get(url)
page = etree.HTML(html.text, parser=etree.HTMLParser(encoding='utf-8'))
pic_urls = page.xpath("//center/img/@src")
i = 0
for pic_url in pic_urls:
    purl = "http://poj.org/" + str(pic_url)
    pic = requests.get(purl)
    fp = open(str(i) + ".gif","wb")
    fp.write(pic.content)
    fp.close()
    i+=1