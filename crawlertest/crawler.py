#-*- coding:utf8 -*-
import sys
import requests
from lxml import etree
reload(sys)
sys.setdefaultencoding("utf-8")


url = "http://poj.org/problemlist"
html = requests.get(url)
page = etree.HTML(html.text.encode('GB2312'),parser=etree.HTMLParser(encoding='utf-8'))

for i in range(2, 102):
    ID = page.xpath('/html/body/table[2]//tr[%d]/td[1]/text()'%i)
    href = page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/@href'%i)
    title = page.xpath('/html/body/table[2]//tr[%d]/td[2]/a/text()'%i)
    ratio = page.xpath('/html/body/table[2]//tr[%d]/td[3]'%i)[0].xpath('string(.)')
    
    print ID,title,ratio

url = "http://poj.org/problem?id=1000"
html = requests.get(url)
page = etree.HTML(html.text.encode('utf8'), parser=etree.HTMLParser(encoding='utf-8'))
#file_object = open('file.txt', 'w')
#file_object.write(html.text)
hint = page.xpath('//table[2]//tr/td//div[5]/text()')
print hint