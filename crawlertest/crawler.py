#-*- coding:utf8 -*-
import sys
import requests
from lxml import etree
reload(sys)
sys.setdefaultencoding("utf-8")

url = "http://poj.org/problemlist"
html = requests.get(url)
page = etree.HTML(html.text,parser=etree.HTMLParser(encoding='utf-8'))

for i in range(2, 102):
    ID = page.xpath('/html/body/table[2]//tr[%d]/td[1]/text()'%i)[0]
    href = page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/@href'%i)[0]
    title = page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/text()'%i)[0]
    ratio = page.xpath('/html/body/table[2]//tr[%d]/td[3]'%i)[0].xpath('string(.)')
    
    print ID,href, title,ratio


url = "http://poj.org/problem?id=1015"
html = requests.get(url)
page = etree.HTML(html.text, parser=etree.HTMLParser(encoding='utf-8'))
#file_object = open('file.txt', 'w')
#file_object.write(html.text)
title = page.xpath('/html/body/table[2]//tr/td/div[2]/text()')[0]
time_limit = page.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[1]')[0].xpath('string(.)')
mem_limit = page.xpath('/html/body/table[2]//tr/td/div[3]/table//tr[1]/td[3]')[0].xpath('string(.)')
description = page.xpath('/html/body/table[2]//tr/td/div[4]')[0].xpath('string(.)')
_input = page.xpath('/html/body/table[2]//tr/td/div[5]')[0].xpath('string(.)')
_output = page.xpath('/html/body/table[2]//tr/td/div[6]')[0].xpath('string(.)')
sample_input = page.xpath('/html/body/table[2]//tr/td/pre[1]/text()')[0]
sample_output = page.xpath('/html/body/table[2]//tr/td/pre[2]/text()')[0]
hint = page.xpath('/html/body/table[2]//tr/td/div[7]/text()')[0]
print title,time_limit,mem_limit
print description
print "input:" + str(_input)
print _output
print sample_input
print sample_output
print hint